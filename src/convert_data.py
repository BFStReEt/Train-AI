import json

# Load the data from output.json
with open("../data/output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Function to convert data to the required format
def convert_data(data):
    converted_data = []
    for item in data:
        text = f"{item['Thoi_gian_bat_dau']} - {item['Thoi_gian_ket_thuc']}, {item['Ten_kinh_doanh']}, {item['Ten_khach_hang']}, {item['Mat_hang']}, {item['So_luong']}, {item['Gia']}, {item['Ket_qua_ban_hang']}"
        entities = [
            {"start": text.find(item['Thoi_gian_bat_dau']), "end": text.find(item['Thoi_gian_bat_dau']) + len(item['Thoi_gian_bat_dau']), "label": "START_TIME"},
            {"start": text.find(item['Thoi_gian_ket_thuc']), "end": text.find(item['Thoi_gian_ket_thuc']) + len(item['Thoi_gian_ket_thuc']), "label": "END_TIME"},
            {"start": text.find(item['Ten_kinh_doanh']), "end": text.find(item['Ten_kinh_doanh']) + len(item['Ten_kinh_doanh']), "label": "BUSINESS_NAME"},
            {"start": text.find(item['Ten_khach_hang']), "end": text.find(item['Ten_khach_hang']) + len(item['Ten_khach_hang']), "label": "CUSTOMER"},
            {"start": text.find(item['Mat_hang']), "end": text.find(item['Mat_hang']) + len(item['Mat_hang']), "label": "PRODUCT"},
            {"start": text.find(str(item['So_luong'])), "end": text.find(str(item['So_luong'])) + len(str(item['So_luong'])), "label": "QUANTITY"},
            {"start": text.find(item['Gia']), "end": text.find(item['Gia']) + len(item['Gia']), "label": "PRICE"},
            {"start": text.find(item['Ket_qua_ban_hang']), "end": text.find(item['Ket_qua_ban_hang']) + len(item['Ket_qua_ban_hang']), "label": "SALE_RESULT"}
        ]
        converted_data.append({"text": text, "entities": entities})
    return converted_data

# Convert the data
converted_data = convert_data(data)

# Save the converted data to a new JSON file
with open("../data/converted_output.json", "w", encoding="utf-8") as f:
    json.dump(converted_data, f, ensure_ascii=False, indent=4)

print("✅ Data converted and saved to 'converted_output.json'")