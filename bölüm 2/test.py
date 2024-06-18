num = int(input("Bir sayı giriniz:"))
if num <=1:
    print(num, "asal sayı değildir")
else:
    asal_mi = True 
for i in range(2,num):
    if (num % i == 0):
        asal_mi = False
        break
if (asal_mi):
    print(num, "asal sayıdır")
else:
    print(num, "asal sayı degildir")