from socket import *
from math import pi
from socket import *
import socket
import sys
import time
import random
import math

print("--------------------Miresevini--------------------")
Port = 12000
nHost='localhost'
socketServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketServer.bind((nHost, Port))

print("Serveri eshte ne linje\n")

while True:
    pergj, clientAddress = socketServer.recvfrom(1024)
    print("Mesazhi -->" + pergj.decode('utf-8'))
    kerkesa = pergj.decode('utf-8').split(' ')


    
    def IPADRESA(): 
           try:
             
              socketServer.sendto(str("IP Adresa e klientit eshte:" +str(clientAddress[0]) + str("\n")).encode('utf-8') , clientAddress)
              print('---Klienti ka pranuar pergjigjjen---\n\n')
           except:
               print('Funksioni ka ndalur,provoni perseri\n\n')

    def NUMRIIPORTIT():
        try:
             
             socketServer.sendto(str("Numri i portit eshte: " +str(clientAddress[1])+ str("\n")).encode('utf-8'), clientAddress)
             print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
             print('Funksioni ka ndalur,provoni perseri\n\n')

    def BASHKETINGELLORE():
      try:
        
        nrbashk=0
        zanoret = ['A', 'E', 'I', 'O', 'Y', 'U', 'a', 'e', 'i', 'o', 'u', 'y',' ']
        for i in teksti:
            if i not in zanoret:
                nrbashk=nrbashk+1
        socketServer.sendto(str("Numri i bashketingelloreve ne fjalen e dhene eshte: " +str(nrbashk) + str("\n")).encode('utf-8'),clientAddress)
        socketServer.close()
        print('---Klienti ka pranuar pergjigjjen---\n\n')

      except:
               print('Funksioni ka ndalur,provoni perseri\n\n')

    def PRINTIMI():
        try:
            
           socketServer.sendto((str(teksti)+ str("\n")).encode('utf-8'), clientAddress)
    
           print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
               print('Funksioni ka ndalur,provoni perseri\n\n')
    
    def EMRIIHOSTIT():
        try:
           
            hosti = gethostname()
            if (hosti==' '):
                socketServer.sendto((str("Emri i hostit nuk mund te gjendet.")+ str("\n")).encode('utf-8'), clientAddress)
                socketServer.close()
            else:
                socketServer.sendto((str("Emri i hostit eshte: " + hosti)+ str("\n")).encode('utf-8'), clientAddress)
                socketServer.close()
                print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def KOHA():
        try:
            
            koha=time.strftime('%d/%b/%Y %X')
            socketServer.sendto(str("Koha e sakte eshte: "+str(koha)+ str("\n")).encode('utf-8'), clientAddress)
            socketServer.close()
            print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def LOJA():
        try:
            
            loja=[random.randint(1,49) for i in range(7)]
            socketServer.sendto(str(str(loja)+ str("\n")).encode('utf-8'), clientAddress)
            socketServer.close()
            print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def FIBONACCI(numri):
        try:
           
            a,b = 1,1
            for i in range(int(numri)-1):
                a,b = b,a+b
            socketServer.sendto(str("Numri FIBONACCI eshte: "+ str(a)+ str("\n")).encode('utf-8'), clientAddress)
            print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def KONVERTIMI():
        if(teksti=="KilowattToHorsepower"):
                
                vkonvertuar = float(numri)/ 0.745699872
                socketServer.sendto(str(str(numri)+" Kilowatt = "+ str(vkonvertuar)+" Horsepower"+ str("\n")).encode('utf-8'),clientAddress)
                print('---Klienti ka pranuar pergjigjjen---\n\n')
        elif(teksti=="HorsepowerToKilowatt"):
                
                vkonvertuar = float(numri)* 0.745699872
                socketServer.sendto(str(str(numri)+" Horsepower = "+ str(vkonvertuar)+" Kilowatt"+ str("\n")).encode('utf-8'),clientAddress)
                print('---Klienti ka pranuar pergjigjjen---\n\n')
        elif(teksti=="DegreesToRadians"):
                
                vkonvertuar = (float(numri)*0.0174533)
                socketServer.sendto(str(str(numri)+" Degrees = "+ str(vkonvertuar)+" Radians"+ str("\n")).encode('utf-8'),clientAddress)
                print('---Klienti ka pranuar pergjigjjen---\n\n')
        elif(teksti=="RadiansToDegrees"):
                
                vkonvertuar = float(numri)/0.0174533
                socketServer.sendto(str(str(numri)+" Radians = "+ str(vkonvertuar)+" Degrees"+ str("\n")).encode('utf-8'),clientAddress)
                print('---Klienti ka pranuar pergjigjjen---\n\n')
        elif(teksti=="GallonsToLiters"):
               
                vkonvertuar = (float(numri)*3.78541)
                socketServer.sendto(str(str(numri)+" Gallons = "+ str(vkonvertuar)+" Liters"+ str("\n")).encode('utf-8'),clientAddress)
                print('---Klienti ka pranuar pergjigjjen---\n\n')
        elif(teksti=="LitersToGallons"):
                
                vkonvertuar = (float(numri)/3.78541)
                socketServer.sendto(str(str(numri)+" Liters = "+ str(vkonvertuar)+" Gallons"+ str("\n")).encode('utf-8'),clientAddress)
                print('---Klienti ka pranuar pergjigjjen---\n\n')
   
    def PERIMETRI(r):
        try:
          
            rrezja = float (r)
            siperfaqja = 2*pi*rrezja;
            socketServer.sendto(str("Perimetri i rrethit eshte:" +str(siperfaqja)+ str("\n")).encode('utf-8'), clientAddress)
            print('---Klienti ka pranuar pergjigjjen---\n\n')
        except:
            print('Funksioni ka ndalur,provoni perseri\n\n')

    def KATRORINR(n):
        try:
            
            nr = int (n)
            katrori=math.pow(nr,2)
            socketServer.sendto(str("katrori i numrit te kerkuar eshte: " +str(katrori)+ str("\n")).encode('utf-8'), clientAddress)
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
    elif(funks=="KATRORINR"):
        KATRORINR(teksti)
    elif(funks=="PERIMETRI"):
        PERIMETRI(teksti)
    elif(funks=="FIBONACCI"):
        FIBONACCI(teksti)
    else:
         socketServer.sendto(str("Shtyp njeren nga metodat e larteshenuara!\n").encode('utf-8'), clientAddress) 