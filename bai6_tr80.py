def chuoi_ngan_nhat(lst):
    if not lst:  # kiểm tra list rỗng
        return None
    ngan_nhat = min(lst, key=len)  # tìm chuỗi có độ dài nhỏ nhất
    return ngan_nhat

if __name__ == '__main__':
    n = int(input("nhap vào so phan tu cho chuoi:"))
    lst =[]
    for i in range(n):
         x = input("nhap vao ")