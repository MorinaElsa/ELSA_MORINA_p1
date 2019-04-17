from socket import *
import sys


print("--------------------Miresevini--------------------")
Host ='localhost' 
Port = 12000
print('Serveri eshte ne linje, ju mund te zgjedhni ndonjeren nga metodat: \n')
kerkesa=input('IPADRESA - per paraqijen e  IP adreses se klientit.\n'
'NUMRIIPORTIT - per paraqitjen e  portit te klientit.\n'
'BASHKETINGELLORE - per paraqijen e numrit te bashketingelloreve ne nje fjale.\n'
'Formati:BASHKETINGELLORE hapesire teksti per te cilin deshironi te gjeni numrin e bashketingelloreve.\n'
'PRINTIMI - per paraqitjen e fjalise se shtypur ne tekst.\n'
'Formati:PRINTIMI hapesire  fjalia qe deshironi ta printoni\n'
'EMRIIHOSTIT - per paraqitjen e emrit te hostit.\n'
'KOHA - per paraqitjen e kohes aktuale ne server. \n'
'LOJA - Paraqet 7 numra nga rangu[1,49].\n'
'FIBONACCI - paraqitje e numrit FIBONACCI, si rezultat i parametrit te dhene hyres.\n'
'Formati:FIBONACCI hapesire numri per parameter hyres.\n'
'KONVERTIMI - paraqitja e ndonjerit nga konvertimet(varesisht nga opcioni qe ju kerkoni): \n'
'\t\KilowattToHorsepower\n'
'\t\HorsepowerToKilowatt\n'
'\t\DegreesToRadians\n'
'\t\RadiansToDegrees\n'
'\t\GallonsToLiters\n'
'\t\LitersToGallons\n'
'Formati:KONVERTIMI hapesire lloji i konvertimit dhe numrin si vlere per tu konvertuar.\n'
'KATRORINR - Tregon katrorin e numrit te kerkuar.\n'
'Formati:KATRORINR hapsire numrin qe deshironi te dini katrorin e tij.\n'
'PERIMETRI - Paraqet perimetrin e rrethit.\n'
'Formati:PERIMETRI hapsire vleren per rrezen qe deshironi te dini perimetrin.\n'
'shtypni MBYLLE per te ndalur programin\n')

socketClient = socket(AF_INET, SOCK_DGRAM)

while True:
    kerkesa = input("Shkruani kerkesen tuaj: ")
    if(kerkesa=='MBYLLE'):
        print('Ju keni kerkuar te shkeputeni nga linja')
        socketClient.close()

        break
    socketClient.sendto(kerkesa.encode('utf-8'),(Host, Port))
    message = socketClient.recv(1024).decode('utf-8')
    print(message)

