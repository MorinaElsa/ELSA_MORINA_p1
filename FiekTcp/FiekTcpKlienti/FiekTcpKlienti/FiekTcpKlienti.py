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
'HOST - per paraqitjen e emrit te hostit.\n'
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
'NRTHJESHTE - Tregon nese numri i dhene eshte numer primar.\n'
'Formati:NRTHJESHTE hapsire numrin per te ditur nese eshte primar apo jo.\n'
'PERIMETRI - Paraqet perimetrin e rrethit.\n'
'Formati:PERIMETRI hapsire vleren per rrezen qe deshironi te dini perimetrin.\n')


while True:
    socketClient = socket(AF_INET, SOCK_STREAM)
    socketClient.connect((Host, Port))
    kerkesa = input("Shkruani kerkesen tuaj: ")

    if(kerkesa=='MBYLLE'):
        print('Ju keni kerkuar te shkeputeni nga linja')
        socketClient.close()

        break
    else:
        socketClient.send(kerkesa.encode('utf-8'))
        message = socketClient.recv(1024)
        print("Rezultati --> ", message.decode('utf-8'))
        print('')


    

