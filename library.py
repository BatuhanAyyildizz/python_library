class library:
    def __init__(self):
        self.file = open("book.txt", "a+")
    def list_kitap(self):
        self.file.seek(0) # her okuma yada yazmadan sonra dosya başına gitmek için kullandım
        kitaplar=self.file.readlines()  #dosyamı satır satır okur
        for kitap in kitaplar:
            kitap_list=kitap.split(",") # satırları virgüllerle ayrılmış yerlerden ayırarak lisyteye alır
            print(f"Kitabın adı : {kitap_list[0]} , Yazarı {kitap_list[1]}")
        print("-"*30)
    def kitap_ekle(self,kitap_adi,yazar_adi,yayinlanma_tarihi,sayfa_sayisi):
        kitap=f"{kitap_adi},{yazar_adi},{yayinlanma_tarihi},{sayfa_sayisi}\n"#\n koydum çünkü aynı satıra yazıyordu
        self.file.write(kitap)
        print("Kitabınız başarıyla eklendi")
    def kitap_sil(self,kitap_adi):
        self.file.seek(0)
        kitaplar = self.file.readlines()
        self.file.seek(0)
        self.file.truncate() # Dosyanın içi silinip yeniden yazılması için gerekli
        removed = False
        for kitap in kitaplar:
            if kitap_adi not in kitap:
                self.file.write(kitap)
            else:
                removed = True
        if removed:
            print(f"'{kitap_adi}' başlıklı kitap başarıyla kaldırıldı.")
        else:
            print(f"'{kitap_adi}' başlıklı kitap bulunamadı.")
        def __del__(self):
            self.file.close()



lib=library()


while True:
    print("*** MENÜ ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap kaldır")
    print("Eğer çıkmak istiyorsanız Q tuşuna basınız")
    secim = input("Seçiminiz: ")


    if secim == "1":
        lib.list_kitap()
    elif secim == "2":
        kitap_adi = input("Kitap Adı: ")
        yazar_adi = input("Yazarı: ")
        yayinlanma_tarihi = input("Yayın Tarihi: ")
        sayfa_sayisi = input("Sayfa Sayısı: ")
        lib.kitap_ekle(kitap_adi, yazar_adi, yayinlanma_tarihi, sayfa_sayisi)
    elif secim == "3":
        kitap_adi = input("Kaldırılacak Kitap Adı: ")
        lib.kitap_sil(kitap_adi)
    elif secim =="Q" or secim=="q":
        break
    
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
print("Kütüphanemizden başarıyla çıkış yaptınız")
        
    
        
        
        