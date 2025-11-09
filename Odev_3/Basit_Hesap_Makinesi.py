def toplama(x, y):
    result = x + y
    return result
def cikarma(x, y):
    return x - y
def carpma(x, y):
    return x * y
def bölme(x, y):
    return x / y
while True:  # Menü
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    secim = int(input("Yapmak istediğiniz işlemi seçiniz (1-4): "))
    if secim == 1:
        x = float(input("1. sayıyı giriniz: "))
        y = float(input("2. sayıyı giriniz: "))
        a = toplama(x, y)
        print(f"Toplama işleminin sonucu = {a}")
    elif secim == 2:
        x = float(input("1. sayıyı giriniz: "))
        y = float(input("2. sayıyı giriniz: "))
        b = cikarma(x, y)
        print(f"Çıkarma işleminin sonucu = {b}")
    elif secim == 3:
        x = float(input("1. sayıyı giriniz: "))
        y = float(input("2. sayıyı giriniz: "))
        c = carpma(x, y)
        print(f"Çarpma işleminin sonucu = {c}")
    elif secim == 4:
        x = float(input("1. sayıyı giriniz: "))
        y = float(input("2. sayıyı giriniz: "))
        if y == 0:
            print("Bölen sayı 0 olamaz")
        else:
            d = bölme(x, y)
            print(f"Bölme işleminin sonucu = {d}")
    cevap = input("\nDevam etmek istiyor musun? (evet/hayır): ").lower()
    if cevap == "hayır":
        print("Programdan çıkılıyor.")
        break 
