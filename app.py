import streamlit as st
from deep_translator import GoogleTranslator

# Set page configuration
st.set_page_config(page_title=".development of an App that translates French to English for primary school students", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f9f9f9;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .header {
        background-color: #ffcc00;
        color: #333;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stButton {
        background-color: #ffcc00;
        color: #333;
        border-radius: 5px;
    }
    .stButton:hover {
        background-color: #e6b800;
    }
    .stTextArea {
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    h1, h2 {
        font-family: 'Arial', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Main App
def main():
    st.markdown("<div class='header'><h1>French to English Translator</h1></div>", unsafe_allow_html=True)
    
    st.subheader("Enter French Text Below:")
    french_text = st.text_area("French Text", "", height=150)

    if st.button("Translate"):
        if french_text:
            try:
                # Use deep translator to translate the text
                translated_text = GoogleTranslator(source='fr', target='en').translate(french_text)
                
                # Check if the translation is empty
                if translated_text.strip():
                    st.subheader("Translated Text:")
                    st.write(translated_text)
                else:
                    st.error("Translation not found. Please enter a valid French phrase.")
                    
            except Exception as e:
                st.error("An error occurred while translating. Please try again.")
        else:
            st.warning("Please enter some text to translate.")

    # Daily Challenge (optional)
    st.subheader("Daily Challenge")
    st.write("Practice translating French words to English!")

    # Additional Vocabulary Learning Section (optional)
    st.subheader("Tips for Learning French")
    st.write("1. Practice regularly.")
    st.write("2. Engage with native speakers.")
    st.write("3. Use language learning apps.")

# Run the app
if __name__ == "__main__":
    main()
