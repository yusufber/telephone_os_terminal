import subprocess  

name = input("Merhabalar isim giriniz: ")
print("Merhabalar", name, "Telefona hoşgeldin.")

while True:
    print("\n--- Uygulamalar ---")
    print("1. Hesap Makinesi")
    print("2. Mesajlar")
    print("3. Rehber")
    print("4. Çıkış")

    girilecek_uygulama = input("Hangi uygulamaya girmek istersin? (1-4): ")

    if girilecek_uygulama == "1":
        print("Hesap makinesi açılıyor...")
        subprocess.run(["python", "apps/calculator.py"])  

    elif girilecek_uygulama == "2":
        print("Mesajlar açılıyor...")
        subprocess.run(["python", "apps/messages.py"])

    elif girilecek_uygulama == "3":
        print("Rehber açılıyor...")
        subprocess.run(["python", "apps/contacts.py"])  # Rehber uygulamasını çalıştır

    elif girilecek_uygulama == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Bu uygulama bulunamadı. Lütfen geçerli bir seçenek girin.")
