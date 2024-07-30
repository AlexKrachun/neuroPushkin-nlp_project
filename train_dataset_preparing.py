import re

def clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = re.sub(r'\bСтраница \d+\b', '', text)
    text = re.sub(r'\bГлава \d+\b', '', text)
    text = re.sub(r'\[\d+\]', '', text)
    text = re.sub(r'[-]{2,}', '', text)
    text = re.sub(r'Популярность: \d+, Last-modified: .+? GmT', '', text, flags=re.IGNORECASE)
    text = re.sub(r'(\. ){2,}', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^а-яА-Я\s\.]', '', text)
    text = re.sub('\.+', '.', text)
    text = re.sub(r'\{d*\}', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.lower()
    return text

cleaned_text = clean_text('dataset/pushkin - full.txt')

with open('dataset/cleaned_text.txt', 'w', encoding='utf-8') as cleaned_file:
    cleaned_file.write(cleaned_text)
