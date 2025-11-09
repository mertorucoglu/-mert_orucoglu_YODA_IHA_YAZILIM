girilen_cümle=input("Bir cümle yaz: ")
girilen_cümle = girilen_cümle.lower() #hepsini küçük yaptım
kelime_uzunluğu = girilen_cümle.split() #split() yaparak bir liste haline getirdim kelimelerini ayıklayayım
a=len(kelime_uzunluğu) #toplam kelime sayısı
b=len(girilen_cümle) #toplam kaarkter sayısı
c = 0
for item in kelime_uzunluğu: #en uzun kelimeyi bulmak için for döngüsü
    if len(item) > c:
        c = len(item)
print(f"En uzun kelimenin uzunluğu= {c}")
kelime_sayilari = {}
for kelime in kelime_uzunluğu: #her kelime kaç defa geçiyor
    if kelime in kelime_sayilari:
        kelime_sayilari[kelime] = kelime_sayilari[kelime] + 1
    else:
        kelime_sayilari[kelime] = 1   
print(f"Toplam karakter sayısı boşluklar dahil= {b}")
print(f"Toplam kelime sayısı= {a}")
print(kelime_sayilari)