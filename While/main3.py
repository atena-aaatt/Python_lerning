## 0-10 arası sayıların toplamını while ile bulan python programı:

sayac , toplam = 1 , 0

while (sayac <= 10):
    toplam += sayac
    sayac += 1

print("Sayılar Toplamı:",toplam)

from math import factorial # faktoriyel metodunu dahil ettik
sayi = int(input("Bir Sayı Gir: "))
print(factorial(sayi))
## fibonacci sayısı
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
fib(sayi)