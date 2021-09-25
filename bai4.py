print(" Nhap vao 1 so nguyen duong: ")
while True:
    a = int(input())
    if a<0:
        print("Nhap sai, moi ban nhap lai:")
    else:
        break

TongCacChuSo = 0
thuong = a
while True:
    du = Thuong %10
    Thuong = int(Thuong/10)
    TongCacChuSo += du
    if thuong==0:
        break
print("Tong cac chu so cua so", a, "la:", TongCacChuSo)