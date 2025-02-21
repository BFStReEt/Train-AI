import spacy

# Load mô hình đã huấn luyện
nlp = spacy.load("../models/model_ner")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

sample_text = "Microsoft 365 Copilot giá 8.752.000 VNĐ"
print(extract_entities(sample_text))
