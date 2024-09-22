import streamlit as st
import re
from commentary import sl_tokenization_pre_text
from commentary import sl_tokenization_post_text

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def tokenize(text):
    # Define special characters and punctuation marks
    special_chars = ['.', ',', '!', '?', ':', ';', '"', "'", '`', '(', ')', '[', ']', '{', '}', '-', '—', '–', '/', '\\', '@', '#', '$', '%', '^', '&', '*', '+', '=', '<', '>', '|', '~', '_', '•', '°', '…']
    
    # Escape special regex characters and join with |
    pattern = '|'.join(map(re.escape, special_chars))
    
    # Split on special characters or whitespace
    tokens = re.split(f'([{pattern}]|\s+)', text)
    
    # Remove empty tokens
    return [token for token in tokens if token.strip()]

def main():
    # Custom CSS for title and spacing
    st.markdown(
        """
        <style>
        .title {
            font-size: 24px;
        }
        .spacer {
            margin-top: 20px;
        }
        .section-title {
            font-size: 20px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<h1 class="title">📊 Data Preparation for LLM Training</h1>', unsafe_allow_html=True)
    
    # Commentary block with yellowish background color
    st.markdown(
        f"""
        <div style="background-color: #F7D3C6; padding: 10px; border-radius: 5px;">
            {sl_tokenization_pre_text}
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📚 Identify the corpus of data:</div>', unsafe_allow_html=True)
    
    with st.expander("Choose input method:"):
        option = st.radio("", ("Upload a text file", "Write text"))
        
        raw_text = ""
        
        if option == "Upload a text file":
            uploaded_file = st.file_uploader("Choose a text file", type="txt")
            if uploaded_file is not None:
                raw_text = uploaded_file.read().decode("utf-8")
                st.subheader("File Content")
                st.text_area("Content", raw_text, height=200)
        else:
            raw_text = st.text_area("Write your text here", height=200)
    
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔍 Break down the data into tokens:</div>', unsafe_allow_html=True)
    
    with st.expander("Generate top 50 Tokens"):
        if st.button("Tokenize"):
            if not raw_text:
                st.warning("Please Identify the corpus of data.")
            else:
                tokens = tokenize(raw_text)
                top_50_tokens = tokens[:50]
                formatted_tokens = ', '.join(f'"{token}"' for token in top_50_tokens)
                st.text_area("Tokens", formatted_tokens, height=200)
                st.write(f"Total tokens generated: {len(tokens)} tokens generated.")
    
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📖 Generate Dictionary:</div>', unsafe_allow_html=True)
    
    with st.expander("Generate Dictionary"):
        if st.button("Generate Dictionary"):
            if not raw_text:
                st.warning("Please Identify the corpus of data.")
            else:
                tokens = tokenize(raw_text)
                if not tokens:
                    st.warning("Please generate tokens.")
                else:
                    unique_tokens = sorted(set(tokens))
                    ranked_tokens = [f'{i+1} - "{token}"' for i, token in enumerate(unique_tokens)]
                    formatted_ranked_tokens = ' || '.join(ranked_tokens)
                    dictionary_label = "Dictionary Length - "+str(len(ranked_tokens))
                    st.text_area(dictionary_label, formatted_ranked_tokens, height=200)


    # Custom CSS for title and spacing
    st.markdown(
        """
        <style>
        .title {
            font-size: 24px;
        }
        .spacer {
            margin-top: 20px;
        }
        .section-title {
            font-size: 20px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    
    # Commentary block with yellowish background color
    st.markdown(
        f"""
        <div style="background-color: #C5E3FD; padding: 10px; border-radius: 5px;">
            {sl_tokenization_post_text}
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()