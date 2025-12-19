# Nhập vào số tiền cần phân tích
so_tien = int(input("Nhập vào số tiền: "))

# Danh sách các mệnh giá tiền hiện có
menh_gia = [50000, 20000, 10000, 5000, 2000, 1000]

print("Phân tích số tờ tiền:")

# Duyệt qua từng mệnh giá trong danh sách
for m in menh_gia:  
    so_to = so_tien // m   # Tính số tờ của mệnh giá m (chia lấy phần nguyên)
    if so_to > 0:          # Nếu có ít nhất 1 tờ
        print(so_to, "tờ", m)
    so_tien = so_tien % m  # Cập nhật lại số tiền còn lại sau khi trừ đi phần đã đổi

# Nếu sau khi đổi xong mà vẫn còn dư (nhỏ hơn 1000)
if so_tien > 0:
    print("Số tiền còn dư không chia hết cho 1000:", so_tien)
