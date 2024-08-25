#Hesap Makinesi
print("""Hesap Makinesine Hoşgeldiniz!""")
IlkSayi=float(input("İlk Sayıyı Giriniz "))
IkinciSayi = float(input("İkinci Sayıyı Giriniz "))
islem=input("""Yapmak İstediğiniz İşlemi Giriniz: Toplama:+,Çıkarma:-,Çarpma:*,Bölme:/,İki Sayının Ortalamasını Alma:0""")
if islem=="+":
    print(str(IlkSayi+IkinciSayi))
if islem=="-":
    print(str(IlkSayi-IkinciSayi))
if islem=="*":
    print(str(IlkSayi*IkinciSayi))
if islem=="/":
    print(str(IlkSayi/IkinciSayi))
if islem=="0":
    print(str((IlkSayi+IkinciSayi)/2))
while True:
    pass