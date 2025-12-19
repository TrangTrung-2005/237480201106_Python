def so_lon(a, b):
    # Dùng lambda để tìm số lớn hơn
    # Nếu x > y thì trả x, ngược lại trả y
    lon_hon = lambda x, y: x if x > y else y

    # Tìm số lớn hơn
    so_lon = lon_hon(a, b)
    # In số lớn hơn
    print(f"Số lớn hơn là: {so_lon}")

    # In bảng cửu chương của số lớn đó
    print(f"\nBảng cửu chương của {so_lon}:")
    # Lặp từ 1 đến 10
    for i in range(1, 11):
        # In từng dòng bảng cửu chương
        print(f"{so_lon} x {i} = {so_lon * i}")


if __name__ == "__main__":
    while True:
        try:
            a = int(input("nhap so thu nhat:"))
            b = int(input("nhap so thu hai:"))
            break
        except ValueError:
            print(" Đã xảy ra một ngoại lệ vui lòng nhập lại !")
    so_lon(a, b)
