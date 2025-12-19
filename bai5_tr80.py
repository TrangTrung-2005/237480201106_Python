def vi_tri_dautien (lst,k):
    if not lst:
        return -1
    else:
        for i in range(len(lst)):
            if lst[i] == k:
                return i
        return -1

# --- Chương trình chính ---
# Nhập list số nguyên từ bàn phím, các số cách nhau bằng dấu cách
#lst = list(map(int, input("Nhập các số nguyên, cách nhau bằng dấu cách: ").split()))
if __name__ == '__main__':
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    lst = []

    for i in range(n):
        while True:
            try:
                x = int(input(f"Nhập phần tử thứ {i}: "))
                lst.append(x)
                break
            except ValueError:
                print(" da xay ra mot ngoai le!!!")


    lst.append(vi_tri_dautien(lst,i))
    # tìm phần tử k trong danh sách
    k = int(input("Nhập k để tìm kiếm :"))
    # Gọi hàm và in kết quả ra màn hình

    vitri  = vi_tri_dautien(lst,k)
    if vitri != -1:# nếu tìm thấy trả ra vi trí
        print(f"Vị trí của {k} là :", vitri)
    else: # còn không thì trả None : không nằm trong danh sách
        print (f"{k} không nằng trong danh sách")