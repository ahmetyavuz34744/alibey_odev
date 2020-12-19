

eposta = str(input("e posta adresini giriniz:"))
if "@" and ".com" in eposta:
    print("sifre giriniz.")
elif "@" and "edu.tr" in eposta:
    print("sifre giriniz.")
else:
    print("e posta yanlis!.")