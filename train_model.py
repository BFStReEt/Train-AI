import json

def load_preprocessed_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def train_model(data):
    # Thực hiện logic huấn luyện ở đây
    # Ví dụ: In ra dữ liệu
    print("Dữ liệu huấn luyện:", data)
    # Giả sử kết quả huấn luyện là một danh sách các từ điển
    results = []
    for item in data:
        result = {
            "Thoi_gian_bat_dau": item["Thoi_gian_bat_dau"],
            "Thoi_gian_ket_thuc": item["Thoi_gian_ket_thuc"],
            "Ten_kinh_doanh": item["Ten_kinh_doanh"],
            "Ten_khach_hang": item["Ten_khach_hang"],
            "Mat_hang": item["Mat_hang"],
            "So_luong": item["So_luong"],
            "Gia": item["Gia"],
            "Ket_qua_ban_hang": item["Ket_qua_ban_hang"]
        }
        results.append(result)
    return results

def save_results(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    preprocessed_data_path = 'data/train_data.json'
    output_file_path = 'output_results.json'
    
    training_data = load_preprocessed_data(preprocessed_data_path)
    results = train_model(training_data)
    save_results(results, output_file_path)
    print(f"Kết quả huấn luyện được lưu tại {output_file_path}")
