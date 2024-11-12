print("Hesap makinesine hoş geldin! Sana verdiğin sayıların toplama, çıkarma, çarpma ve bölme işlemleri yapılacak.")

sayi1 = int(input("Sayı 1'i gir: "))
sayi2 = int(input("Sayı 2'yi gir: "))

print("Toplama:", sayi1 + sayi2)
print("Çıkarma:", sayi1 - sayi2)
print("Çarpma:", sayi1 * sayi2)

if sayi2 != 0:  # Bölme işleminde sıfıra bölme hatası kontrolü
    print("Bölme:", sayi1 / sayi2)
else:
    rint("Bölme işlemi yapılamaz (0'a bölme hatası).")
