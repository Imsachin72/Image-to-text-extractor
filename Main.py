import streamlit as st
import streamlit.components.v1 as components
import pytesseract
from PIL import Image
import pyperclip as clip
import pandas as pd

def save_to_csv(text):
    df = pd.DataFrame({'Text':[text]})
    csv_file = 'text.csv'
    df.to_csv(csv_file, index=False)
    st.success(f'Text saved to {csv_file}')
    
def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    with open('index.html') as f:
        styles = f.read()
    components.html(styles)

    uploaded_file = st.file_uploader('Choose an image file ', type=["png", "jpg", "jpeg", "webp"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=False)

        st.write('Extracted Text : ')
        text = pytesseract.image_to_string(image=image, lang='eng')
        st.text(text)
        
        col1, col2 = st.columns(2) 
        with col1 : 
            if st.button('copy'):
                clip.copy(text=text)
                st.success('Text copied Successfully!')
            
        # if st.button('save as csv'):
        #     save_to_csv(text)
        
        with col2:  
            st.download_button(
                label="Download Text File",
                data=text.encode('utf-8'),
                file_name="extracted_text.txt",
                mime="text/plain"
            )

if __name__ == '__main__':
    main()
