import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image, UnidentifiedImageError
import pickle

# --- HARUS di bagian paling atas ---
st.set_page_config(
    page_title="Prediksi Penyakit Tanaman",
    page_icon="🌿",
    layout="centered"
)

# --- Load Model dan Label Map ---
model_path = 'Model.h5'
label_map_path = 'label_map.pkl'

# Load model tanpa pesan sukses
try:
    model = tf.keras.models.load_model(model_path)
except Exception as e:
    st.error(f"Gagal load model: {e}")
    st.stop()

# Load label map tanpa pesan sukses
try:
    with open(label_map_path, 'rb') as f:
        label_map = pickle.load(f)
    
    # Validasi format label map
    if not isinstance(label_map, dict) or len(label_map) == 0:
        raise ValueError("Label map tidak valid atau kosong")
    
    # Buat mapping index ke label
    idx_to_label = {v: k for k, v in label_map.items()}
except Exception as e:
    st.error(f"Gagal load label map: {e}")
    st.stop()

# --- Fungsi Prediksi ---
def predict_disease(img):
    img = img.resize((224, 224))  # sesuai input model InceptionV3
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array, verbose=0)  # nonaktifkan logging prediksi
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = np.max(prediction)

    # Cek jika kelas prediksi ada di mapping
    if predicted_class not in idx_to_label:
        available_classes = ", ".join(map(str, idx_to_label.keys()))
        raise ValueError(
            f"Predicted class {predicted_class} tidak ada di label map. "
            f"Kelas yang tersedia: {available_classes}"
        )

    return idx_to_label[predicted_class], confidence

# --- Streamlit UI ---
st.title("🌿🔍 Prediksi Penyakit Tanaman Pertanian")
st.markdown("Upload gambar daun tanaman, dan model akan memprediksi penyakitnya.")
st.markdown("---")

uploaded_file = st.file_uploader(
    "Pilih gambar daun...", 
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False
)

if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)
        
        # Tampilkan gambar dengan kompatibilitas versi
        try:
            st.image(img, caption="Gambar yang diupload", use_container_width=True)
        except TypeError:
            # Fallback untuk versi Streamlit lawas
            st.image(img, caption="Gambar yang diupload", width=300)
            
    except UnidentifiedImageError:
        st.error("File yang diupload bukan gambar yang valid. Mohon upload file JPG, JPEG, atau PNG.")
        st.stop()
    except Exception as e:
        st.error(f"Gagal memproses gambar: {e}")
        st.stop()

    if st.button("Prediksi", type="primary"):
        with st.spinner("Menganalisis gambar..."):
            try:
                label, confidence = predict_disease(img)
                
                # Tampilkan hasil dengan format menarik
                st.success(f"**Hasil Prediksi:** {label}")
                st.metric(
                    label="Tingkat Akurasi", 
                    value=f"{confidence*100:.2f}%",
                    delta="tinggi" if confidence > 0.75 else "sedang"
                )
                
                # Tampilkan emoji sesuai hasil
                if "sehat" in label.lower():
                    st.balloons()
                    st.success("🎉 Tanaman sehat! 🎉")
                else:
                    st.warning("⚠️ Terdeteksi penyakit! Perlu penanganan.")
                    
            except Exception as e:
                st.error(f"Error saat prediksi: {str(e)}")
                st.error("Silakan coba dengan gambar lain atau hubungi support.")
