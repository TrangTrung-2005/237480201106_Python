def vi_tri_max(ds):
    # Kiểm tra xem list có rỗng không
    if not ds:
        return None  # Nếu rỗng thì không có vị trí nào, trả về None

    # Tìm giá trị lớn nhất trong list
    max_value = max(ds)

    # Trả về vị trí (chỉ số) đầu tiên của phần tử có giá trị lớn nhất
    return ds.index(max_value)


# --- Chương trình chính ---

if __name__ == '__main__':
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    ds = []

    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập phần tử thứ {i + 1}: "))
                ds.append(x)
                break
            except ValueError:
                print(" Vui lòng nhập số nguyên hợp lệ!")

    print("Danh sách vừa nhập là:", ds)
    a = vi_tri_max(ds)
    print(f" phần tủ lớn nhất trong danh sách ở vị trí thứ  {a+1}")# a chay tu 0 nen + 1