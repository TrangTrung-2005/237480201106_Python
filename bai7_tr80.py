from os.path import split

def tinh_TB(lst):
    if not lst:
        return None
    else:
        return  sum(lst)%len(lst)

if __name__ == '__main__':
    #lst = list(map(int, input("Nhập các số nguyên, cách nhau bằng dấu cách: ").split()))
    n = int(input(" nhap so luong phan tu cho  danh sach:"))
    lst =[]
    a =0
    for i in range(n):
        while True:
            try:
                x = int(input(f"nhap phan tu thu {i+1}:"))
                lst.append(x)
                break
            except ValueError:
                print(" da xay ra mot ngoai le!!!")
    print("danh sach vua nhap la:",lst)
    trung_binh = tinh_TB(lst)
    if trung_binh is not None:
        print("Giá trị trung bình của danh sách là:", trung_binh)
    else:
        print("Danh sách rỗng, không thể tính trung bình.")
