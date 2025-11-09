import random 
random_number=random.randint(1,100)
remaining_attempts=10
attempt_count=0
while(remaining_attempts>0):
    guess=int(input("1 ile 100 arasında bir sayi tahmin et= ")) #kullanıcıdan bir sayı istedim
    if(guess<1 or guess>100):
        print("Adam  akilli oyna")  #eğer bu sayı 1 ile 100 arasımda değilse sıkınıt oluşturduğunu söyledim
        continue
    attempt_count+=1 # kaçınıcı deneme olduğu bilgisine +1 ekleme
    if(guess==random_number):
        print(f"tebrikler {attempt_count}. denemenizde bildiniz")  #kulllanıcı bildiyse tebrik ettim ve kaçıncı denemede bildiğini yazdım
        break
    elif(guess<random_number):
        print("Daha büyük bir sayı dene")  #tahmin ettiği sayı küçükse ona daha büyük sayı girmen gerek dedim
        
    elif(guess>random_number):
        print("Daha küçük bir sayı dene")  #tahmin ettiği sayı büyükse ona daha küçük sayı girmen gerek dedim
        
    remaining_attempts-=1 # kalan hakkında -1 azaltma
    if(remaining_attempts>0): 
        print(f"{remaining_attempts} deneme hakkınız kaldı") #kaç deneme hakkı kaldığını gösterme
    else:
        print("üzgünüm tüm haklarınız bitti") #hayat bitti
