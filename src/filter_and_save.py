import spacy
import pandas as pd
import json

# Tải mô hình đã huấn luyện
nlp = spacy.load("../models/model_ner")

# Đọc dữ liệu cần lọc
with open("../data/data_to_filter.json", "r", encoding="utf-8") as f:
    data_to_filter = json.load(f)

# Lọc dữ liệu
filtered_data = []
for data in data_to_filter:
    doc = nlp(data["Mat_hang"])
    entities = {ent.label_: ent.text for ent in doc.ents}
    filtered_data.append(entities)

# Chuyển đổi dữ liệu đã lọc thành DataFrame
df = pd.DataFrame(filtered_data)

# Lưu dữ liệu đã lọc vào tệp Excel
df.to_excel("../data/chat_summary.xlsx", index=False)
print("✅ Đã lưu dữ liệu đã lọc vào tệp 'chat_summary.xlsx'")
