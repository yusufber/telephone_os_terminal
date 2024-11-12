import subprocess

# Önceki mesajları saklayan liste
onceki_mesajlar = ["Merhaba!", "Nasılsın?", "Yarın görüşürüz."]

def uygulama_ac():
    print("Mesajlaşma Uygulamasına Hoş Geldiniz!")
    print("1. Önceki Mesajlarımı Göster")
    print("2. Mesaj Gönder")
    print("3. Çıkış")

    # Kullanıcıdan seçim alalım
    secim = input("Bir seçenek seçin: ")

    if secim == "1":
        onceki_mesajlari_goster()
    elif secim == "2":
        mesaj_gonder()
    elif secim == "3":
        uygulamadan_cik()
    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")
        uygulama_ac()

def onceki_mesajlari_goster():
    print("\nÖnceki Mesajlarınız:")
    for mesaj in onceki_mesajlar:
        print("- " + mesaj)
    print("\nAna menüye dönülüyor...\n")
    uygulama_ac()

def mesaj_gonder():
    yeni_mesaj = input("Göndermek istediğiniz mesajı yazın: ")
    onceki_mesajlar.append(yeni_mesaj)
    print("Mesaj gönderildi!")
    uygulama_ac()

def uygulamadan_cik():
    print("Uygulamadan çıkılıyor...")
    print("Ana sayfaya yönlendiriliyorsunuz... (app.py'ye dönüyor)\n")
    
    # app.py dosyasını çalıştır
    subprocess.run(["python", "app.py"])

# Uygulamayı aç
uygulama_ac()
