
from socket import *
from math import pi
from _thread import *
import sys
import time
import random
import math

print("--------------------Miresevini--------------------")
sPort = 12000
Host="127.0.0.1"

socketServer = socket(AF_INET,SOCK_STREAM)
socketServer.bind(('', sPort))

socketServer.listen(5)
print("Serveri eshte i gatshem per te pranuar kerkesen:\n\n")



while True:
    Konektimi, clientAddress = socketServer.accept()
    message = Konektimi.recv(1024)
    kerkesa = message.decode('utf-8').split(' ')
    
    def IPADRESA(): 
       try:
              print('Kerkesa eshte te dergohet Ip adresa!')
              adresa = gethostbyname(gethostname())
              if (adresa==' '):
                Konektimi.send(str("Adresa nuk mund te gjendet.").encode('utf-8'))
              else:
                Konektimi.send(str("Adresa eshte: " + adresa).encode('utf-8'))
                print('---Klienti ka pranuar pergjigjjen---\n\n')
       except:
               print('Funksioni ka ndalur,provoni perseri\n\n')

           
    def NUMRIIPORTIT():
        try:
             print('Kerkesa eshte te dergohet numri i portit!')
             Konektimi.send(str(str(clientAddress[1])).encode('utf-8'))
             print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
             print('Funksioni ka ndalur,provoni perseri\n\n')

    def BASHKETINGELLORE():
      try:
        print('Kerkesa eshte te numerohen bashketingelloret!')
        nrbashk=0
        zanoret = ['A', 'E', 'I', 'O', 'Y', 'a', 'e', 'i', 'o', 'u', 'y','U', ' ']
        for i in teksti:
            if i not in zanoret:
                nrbashk=nrbashk+1
        Konektimi.send(str("Numri i bashketingelloreve ne fjalen e dhene eshte: " +str(nrbashk)).encode('utf-8'))
        print('---Klienti ka pranuar pergjigjjen---\n\n')

      except:
               print('Funksioni ka ndalur,provoni perseri\n\n')

    def PRINTIMI():
        try:
         print('Kerkesa eshte te behet printimi i shenimit!')
         
         Konektimi.send(str(teksti).encode('utf-8'))
         print('---Klienti ka pranuar pergjigjjen---\n\n')

        except:
               print('Funksioni ka ndalur,provoni perseri\n\n')

    
    def EMRIIHOSTIT():
      try:
          print('Kerkesa eshte te dergohet emri i hostit!')
          hosti = gethostname()
          if (hosti==' '):
            Konektimi.send(str("Emri i hostit nuk mund te gjendet.").encode('utf-8'))
          else:
            Konektimi.send(str("Emri i hostit eshte: " + hosti).encode('utf-8'))
            print('---Klienti ka pranuar pergjigjjen---\n\n')
      except:
          print('Funksioni ka ndalur,provoni perseri\n\n')


    def KOHA():
        try:
            print('Kerkesa eshte te tregohet koha e sakte!')
            koha=time.strftime('%d/%b/%Y %X')
            Konektimi.send(str(str(koha)).encode('utf-8'))
            print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def LOJA():
        try:
            print('Kerkesa eshte te paraqiten 7 numra nga vargu [1,49]!')
            loja=[random.randint(1,49) for i in range(7)]
            Konektimi.send(str(str(loja)).encode('utf-8'))
            print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def FIBONACCI(numri):
        try:
            print('Kerkesa eshte te tregohet numri fibonacci!')
            a,b = 1,1
            for i in range(int(numri)-1):
                 a,b = b,a+b
            Konektimi.send(str("Numri FIBONACCI eshte: "+ str(a)).encode('utf-8'))
            print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def KONVERTIMI():
     try:
            
            if(teksti=="KilowattToHorsepower"):
                print('Kerkesa eshte te llogaritet KilowattToHorsepower!')
                vkonvertuar = float(numri)/ 0.745699872
                Konektimi.send(str(str(numri)+" Kilowatt = "+ str(vkonvertuar)+" Horsepower").encode('utf-8'))
                print('---Klienti ka pranuar pergjigjjen---\n\n')
            elif(teksti=="HorsepowerToKilowatt"):
                print('Kerkesa eshte te llogaritet HorsepowerToKilowatt!')
                vkonvertuar = float(numri)* 0.745699872
                Konektimi.send(str(str(numri)+" Horsepower = "+ str(vkonvertuar)+" Kilowatt").encode('utf-8'))
                print('---Klienti ka pranuar pergjigjjen---\n\n')
            elif(teksti=="DegreesToRadians"):
                print('Kerkesa eshte te llogaritet DegreesToRadians!')
                vkonvertuar = (float(numri)*0.0174533)
                Konektimi.send(str(str(numri)+" Degrees = "+ str(vkonvertuar)+" Radians").encode('utf-8'))
                print('---Klienti ka pranuar pergjigjjen---\n\n')
            elif(teksti=="RadiansToDegrees"):
                print('Kerkesa eshte te llogaritet RadiansToDegrees!')
                vkonvertuar = float(numri)/0.0174533
                Konektimi.send(str(str(numri)+" Radians = "+ str(vkonvertuar)+" Degrees").encode('utf-8'))
                print('---Klienti ka pranuar pergjigjjen---\n\n')
            elif(teksti=="GallonsToLiters"):
                print('Kerkesa eshte te llogaritet GallonsToLiters!')
                vkonvertuar = (float(numri)*3.78541)
                Konektimi.send(str(str(numri)+" Gallons = "+ str(vkonvertuar)+" Liters").encode('utf-8'))
                print('---Klienti ka pranuar pergjigjjen---\n\n')
            elif(teksti=="LitersToGallons"):
                print('Kerkesa eshte te llogaritet LitersToGallons!')
                vkonvertuar = (float(numri)/3.78541)
                Konektimi.send(str(str(numri)+" Liters = "+ str(vkonvertuar)+" Gallons").encode('utf-8'))
                print('---Klienti ka pranuar pergjigjjen---\n\n')
       
            else:
                Konektimi.send("Ju lutem shkruani kerkesen ne formatin KONVERTIMI llojikonvertimit numri".encode('utf-8'))
     except: 
        print('Funksioni ka ndalur,provoni perseri\n\n')
     
   
 
    def PERIMETRI(r):
        try:
             print('Kerkesa eshte te tregohet perimetri varesisht nga rrezja e dhene!')
             rrezja = float (r)
             perimetri = 2*pi*rrezja;
             Konektimi.send(str("Perimetri i numrit te kerkuar eshte " +str(perimetri)).encode('utf-8'))
             print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def KATRORINR(n):
        try:
             print('Kerkesa eshte te tregohet katrori i numrit!')
             nr = int (n)
             katrori=math.pow(nr,2)
             Konektimi.send(str("katrori i numrit te kerkuar eshte " +str(katrori)).encode('utf-8'))
             print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')
     
    funks =kerkesa[0]
    teksti = ""
    if(funks=="KONVERTIMI"):
        teksti =kerkesa[1]
        numri =kerkesa[2]
        KONVERTIMI()
    for i in range(len(kerkesa)):
        if(i==0):
            continue
        teksti += str(kerkesa[i] + " ")
        
    if (funks=="IPADRESA"):
        IPADRESA()
    elif (funks=="NUMRIIPORTIT"):
        NUMRIIPORTIT()
    elif (funks=="EMRIIHOSTIT"):
        EMRIIHOSTIT()
    elif (funks=="KOHA"):
        KOHA()
    elif(funks=="LOJA"):
        LOJA()
    elif( funks== 'BASHKETINGELLORE' ):
        BASHKETINGELLORE()
    elif(funks== "PRINTIMI"):
        PRINTIMI()
    elif(funks=="PERIMETRI"):
        PERIMETRI(teksti)
    elif(funks=="KATRORINR"):
        KATRORINR(teksti)
    elif(funks=="FIBONACCI"):
        FIBONACCI(teksti)
    else:
        Konektimi.send(str("Shtyp njeren nga metodat e larteshenuara!").encode('utf-8'))
        Konektimi.close()  
