# contacts.py
from apps.rehber import Rehber

def rehber_menu():
    print("\n--- Rehber Menüsü ---")
    print("1. Kişi Ekle")
    print("2. Kişi Bul")
    print("3. Kişiyi Ara")
    print("4. Son Aramalarım")
    print("5. Çıkış")

def rehber_uygulamasi():
    rehber = Rehber()
    son_arama_listesi = []

    while True:
        rehber_menu()
        secim = input("Bir seçenek seçin (1-5): ")

        if secim == "1":
            isim = input("Kişi ismi: ")
            telefon = input("Telefon numarası: ")
            email = input("Email (isteğe bağlı): ")
            rehber.kisi_ekle(isim, telefon, email)

        elif secim == "2":
            isim = input("Aramak istediğiniz kişinin ismi: ")
            kisi = rehber.kisi_bul(isim)
            if kisi:
                print(f"Bu kişi mi? {kisi}")
            else:
                print("Kişi bulunamadı.")

        elif secim == "3":
            isim = input("Aramak istediğiniz kişinin ismi: ")
            kisi = rehber.kisi_bul(isim)
            if kisi:
                print(f"{kisi.isim} aranıyor...")
                son_arama_listesi.append(kisi)
            else:
                print("Kişi bulunamadı.")

        elif secim == "4":
            print("\nSon Aramalarım:")
            if son_arama_listesi:
                for kisi in son_arama_listesi:
                    print(kisi)
            else:
                print("Henüz bir arama yapılmadı.")

        elif secim == "5":
            print("Rehberden çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    rehber_uygulamasi()
