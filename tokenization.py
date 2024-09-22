import re

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
    file_path = "the-verdict.txt"
    raw_text = read_file(file_path)
    tokens = tokenize(raw_text)
    
    # Print tokens for verification
    print(tokens)

if __name__ == "__main__":
    main()