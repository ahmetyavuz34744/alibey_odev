url = str(input("url adresinizi giriniz:"))

if "www." and " .com" in url:
    print("Dogru bir url.")
elif "www." and ".org" in url:
    print("dogru bir url.")
elif "www." and ".net" in url:
    print("dogru bir url.")
else:
    print("Girdiginiz url yi kontrol ediniz.")