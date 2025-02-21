import json

# Đọc nội dung từ tệp input.txt
with open("../data/input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Chuyển đổi nội dung thành định dạng JSON
train_data = []
for line in lines:
    if line.startswith("KH:"):
        text = line[3:].strip()
        entities = []
        if "Microsoft 365 Copilot" in text:
            entities.append({"start": text.find("Microsoft 365 Copilot"), "end": text.find("Microsoft 365 Copilot") + len("Microsoft 365 Copilot"), "label": "PRODUCT"})
        if "8.752.000 VNĐ" in text:
            entities.append({"start": text.find("8.752.000 VNĐ"), "end": text.find("8.752.000 VNĐ") + len("8.752.000 VNĐ"), "label": "PRICE"})
        if "HP Pro Tower 280 G9" in text:
            entities.append({"start": text.find("HP Pro Tower 280 G9"), "end": text.find("HP Pro Tower 280 G9") + len("HP Pro Tower 280 G9"), "label": "PRODUCT"})
        if "8.950.000 VNĐ" in text:
            entities.append({"start": text.find("8.950.000 VNĐ"), "end": text.find("8.950.000 VNĐ") + len("8.950.000 VNĐ"), "label": "PRICE"})
        train_data.append({"text": text, "entities": entities})

# Lưu dữ liệu đã chuyển đổi vào tệp train_data.json
with open("../data/train_data.json", "w", encoding="utf-8") as f:
    json.dump(train_data, f, ensure_ascii=False, indent=4)

print("✅ Đã chuyển đổi dữ liệu và lưu vào tệp 'train_data.json'")
