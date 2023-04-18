import socket as s

class Server:
    host = "127.0.0.1"
    port = 64325
    server = s.socket(s.AF_INET,s.SOCK_STREAM)

    def __init__(self):
        self.server.bind((self.host,self.port))
        print("Server oluşturuldu")
        self.server.listen(1)
        print("Client dinleniyor")
        self.client,self.client_adrs = self.server.accept()
        print(f"Bağlanan bilgisayar ip ve port: {self.client_adrs}")
        print("_______________________________________________________________________________")


    def msj_set(self,msj):
        msj = str(msj)
        self.client.send(msj.encode())


    def msj_get(self):
        gelen_mesaj = self.client.recv(1024).decode()
        return gelen_mesaj
    

    def konturol(self):
        print("*** çıkmak için kapat | şifrelemek için sifrele | çözmek için coz yazınız ***")
        while True:
           print()
           istem =  input("Hangi işlemi yapmak istersiniz: ")
           print()
           if istem == "kapat":
               self.msj_set(istem)
               break
           elif istem == "sifrele":
               self.msj_set(istem)
           elif istem == "coz":
               self.msj_set(istem)
           else:
               print("Yanlış istem girişi TEKRAR DENEYİN")          
            
               
               
           

if __name__ == "__main__":
    a = Server()
    a.konturol()



        