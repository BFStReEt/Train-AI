import pandas as pd

data = [
    {"Thời gian": "2025-02-19 15:30", "Tên khách hàng": "Mr.Hùng", "Mặt hàng": "Microsoft 365 Copilot", "Số lượng": "1", "Giá": "8.752.000 VNĐ"},
]

df = pd.DataFrame(data)
df.to_excel("../data/output.xlsx", index=False)
print("✅ Đã xuất file Excel!")
