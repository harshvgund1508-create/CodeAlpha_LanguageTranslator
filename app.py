import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Language Translator")
st.markdown("### Translate text into multiple languages instantly")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target = st.selectbox("Target Language", list(languages.keys()), index=1)

text = st.text_area(
    "Enter Text",
    placeholder="Type something here...",
    height=180
)

if st.button("🌍 Translate", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed!")

        st.text_area(
            "Translated Text",
            translated,
            height=180
        )