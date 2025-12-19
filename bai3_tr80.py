def is_armstrong(n):
    digits = [int(d) for d in str(n)]  # tách các chữ số
    k = len(digits)                     # số chữ số
    return sum(d**k for d in digits) == n
if __name__ == '__main__':
    while True:
        try:
            # Nhập số từ bàn phím
            num = int(input("Nhập một số để kiểm tra: "))
            break
        except ValueError:
            print(" Đã xảy ra một ngoại lê !!!!")
    # Kiểm tra
    if is_armstrong(num):
        print(f"{num} là số Armstrong ")
    else:
        print(f"{num} không phải là số Armstrong ")
