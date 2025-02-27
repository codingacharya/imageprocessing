import streamlit as st
import cv2
import numpy as np
from PIL import Image

def process_image(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    return gray_image

def main():
    st.title("Image Processing App")
    st.write("Upload an image to process it.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Process Image"):
            processed_image = process_image(image)
            st.image(processed_image, caption="Processed Image (Grayscale)", use_column_width=True, channels="GRAY")

if __name__ == "__main__":
    main()
