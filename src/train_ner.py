import spacy
from spacy.training import Example
import json

# Load mô hình trắng (hoặc vi_core_news_lg nếu cần)
nlp = spacy.blank("vi")
ner = nlp.add_pipe("ner")

# Thêm nhãn mới vào mô hình
labels = ["PRODUCT", "PRICE", "QUANTITY", "CUSTOMER"]
for label in labels:
    ner.add_label(label)

# Đọc dữ liệu huấn luyện
with open("../data/train_data.json", "r", encoding="utf-8") as f:
    TRAIN_DATA = json.load(f)

# Chuyển đổi dữ liệu huấn luyện
examples = []
for data in TRAIN_DATA:
    doc = nlp.make_doc(data["text"])
    examples.append(Example.from_dict(doc, {"entities": data["entities"]}))

# Huấn luyện mô hình
nlp.begin_training()
for epoch in range(20):
    losses = {}
    nlp.update(examples, losses=losses)
    print(f"Epoch {epoch+1}, Loss: {losses}")

# Lưu mô hình đã huấn luyện
nlp.to_disk("../models/model_ner")
print("✅ Mô hình đã lưu vào thư mục 'models/model_ner'")
