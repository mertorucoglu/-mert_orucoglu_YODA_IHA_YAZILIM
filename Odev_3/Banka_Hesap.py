class Hesap:
    def __init__(self, sahip_adi):
        self.sahip_adi = sahip_adi  #hesap dahibinn adı
        self.bakiye = 0             #başlangıç bakiyesi 0 TL
    def para_yatir(self, miktar):  #para yatırma işlemi
        if miktar > 0:   
            self.bakiye += miktar  #bakiyeye ekleme yaptı
            print(f"{miktar} TL yatırıldı. Güncel bakiye = {self.bakiye} TL")
    def para_cek(self, miktar):  #para çekme işlemi
        if self.bakiye >= miktar:  # yeterli bakiye var mı kontrol
            self.bakiye -= miktar  # bakiye azaltıldı
            print(f"{miktar} TL çektiniz. Güncel bakiye = {self.bakiye} TL")
        else:
            print("Hesabınızda yeterli bakiye yok!")
    def bakiye_goster(self):  #bakiye görüntüleme
        print(f"{self.sahip_adi} hesabının güncel bakiyesi: {self.bakiye} TL")

sahip = input("Hesap sahibinin adı: ") # kulanıcıdan bilgi alma
hesap = Hesap(sahip)  # hesap sınıfından nesne oluşturma

while True:  # menü
    print("1. Para Yatır")
    print("2. Para Çek")
    print("3. Bakiye Görüntüle")
    print("4. Çıkış")
    secim = int(input("Yapmak istediğiniz işlemi seçiniz (1-4): "))

    if secim == 1:
        miktar = float(input("Yatırmak istediğiniz miktarı giriniz: "))
        hesap.para_yatir(miktar)
    elif secim == 2:
        miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
        hesap.para_cek(miktar)
    elif secim == 3:
        hesap.bakiye_goster()
    elif secim == 4:
        print("Çıkış")
        break
    else:
        print("Geçersiz seçim, lütfen 1-4 arası bir değer giriniz.")
