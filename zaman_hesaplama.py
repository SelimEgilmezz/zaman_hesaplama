""" fonksiyon ile istenilen sayı ve birim(dk,saniye,gün,vb.) ile sonucu verme """



def zaman_hesapla(sayi,birim):

    if birim == "saniye":
        return int(sayi)

    elif birim == "dakika":
        return int(int(sayi) / 60)

    elif birim == "saat":
        return int(int(sayi) / 3600)

    elif birim == "gün":
        return int(int(sayi) / 86400)

    else:
        return "Geçersiz işlem girdiniz lütfen tekrar deneyin"


while True:

    sayi = input("Sayınızı Giriniz(çıkış yapmak için 'q' giriniz) :")

    if str(sayi) == "q":
        print("Çıkış yapıldı")
        break
    else:
        birim = input("Dönüştürmek istediğiniz birimi seçin (dakika,gün,saniye,saat) :")

        sonuc = zaman_hesapla(sayi,birim)

        print("{} sayısı = {} {} denk gelmektedir.".format(sayi,sonuc,birim))

