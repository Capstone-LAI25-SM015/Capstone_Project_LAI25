import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image, UnidentifiedImageError
import pickle

# --- Load Model dan Label Map ---
model_path = 'Model.h5'
label_map_path = 'label_map.pkl'

# Load model dengan try-except
try:
    model = tf.keras.models.load_model(model_path)
except Exception as e:
    st.error(f"Gagal load model: {e}")
    st.stop()

# Load label map dengan validasi
try:
    with open(label_map_path, 'rb') as f:
        label_map = pickle.load(f)
    if not isinstance(label_map, dict) or len(label_map) == 0:
        raise ValueError("Label map tidak valid atau kosong")
except Exception as e:
    st.error(f"Gagal load label map: {e}")
    st.stop()

idx_to_label = {v: k for k, v in label_map.items()}

# --- Fungsi Prediksi ---
def predict_disease(img):
    img = img.resize((224, 224))  # sesuai input model InceptionV3
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = np.max(prediction)

    if predicted_class not in idx_to_label:
        raise ValueError(f"Predicted class {predicted_class} tidak ada di label map")

    return idx_to_label[predicted_class], confidence

# --- Streamlit UI ---
st.set_page_config(page_title="Prediksi Penyakit Tanaman Pertanian", layout="centered")

st.title("🧠🔍 Prediksi Penyakit Tanaman Pertanian")
st.markdown("Upload gambar Tanaman, dan model akan memprediksi penyakitnya.")

uploaded_file = st.file_uploader("Pilih gambar daun...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)
    except UnidentifiedImageError:
        st.error("File yang diupload bukan gambar yang valid.")
        st.stop()
    except Exception as e:
        st.error(f"Gagal membuka gambar: {e}")
        st.stop()

    st.image(img, caption="Gambar yang diupload", use_container_width=True)

    if st.button("Prediksi"):
        try:
            label, confidence = predict_disease(img)
            st.success(f"🌿 Prediksi: **{label}**")
            st.info(f"📊 Akurasi prediksi: {confidence*100:.2f}%")
        except Exception as e:
            st.error(f"Error saat prediksi: {e}")
