def tinhgiaithua(n):
    giaithua = 1;
    if (n == 0 or n == 1):
        return giaithua;
    else:
        for i in range(2, n + 1):
            giaithua = giaithua * i;
        return giaithua;

n = int(input("Nhập số nguyên dương n = "));
if (n<0):
         print("Yêu cầu nhập lại số nguyên dương")
         n = int(input("Nhập số nguyên dương n = "));
         print("Giai thừa của", n, "là", tinhgiaithua(n));
else:
     print("Giai thừa của", n, "là", tinhgiaithua(n));