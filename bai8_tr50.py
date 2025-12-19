n = int(input("Nhập vào số nguyên có 4 chữ số: "))

a = n // 1000          # Lấy chữ số hàng nghìn → 1
b = (n // 100) % 10    # Lấy chữ số hàng trăm  → 2
c = (n // 10) % 10     # Lấy chữ số hàng chục   → 3
d = n % 10             # Lấy chữ số hàng đơn vị → 4

tong = a + b + c + d
print("Tổng các chữ số của", n, "là:", tong)