import math

def so_nguyento(a):
    if a <= 1:

        # Số <= 1 không phải số nguyên tố
        return False

        ## nd nhập va 5 : Cân 5 = 2.236 => 2+1 =3
    for i in range(2, int(math.sqrt(a)) + 1):
        # vì 5 không chia hết cho 3 nên => 5 là số nguyên tố
        if a % i == 0 :

            # Chia hết cho i → không phải nguyên tố
            return False
    return True

# Nhập số từ người dùng
if __name__ == '__main__':
    while True:
        try:
            a = int(input("Nhập một sô nguyên a bất kỳ: "))
            break
        except ValueError:
                print("đã xảy ra một ngoại lệ ! vui lòng nhập vào phải là số !!")

    if so_nguyento(a):
        print(f"{a} là số nguyên tố")
    else:
        print(f"{a} không phải là số nguyên tố")