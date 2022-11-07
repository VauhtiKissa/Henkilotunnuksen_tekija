import math
import random
tarkistusmerkit = [
                "0","1","2","3","4","5",
                "6","7","8","9","A","B",
                "C","D","E","F","H","J",
                "K","L","M","N","P","R",
                "S","T","U","V","W","X","Y"
                ]
#1800, 1900, 2000
vuosisadanluvut = ["+","-", "A"]

def RandomHenk():
    #Valitsee muuttujat satunnaisesti
    paiva = str(random.randint(1,30))
    
    kuukausi = str(random.randint(1,12))
    
    vuosi = str(random.randint(0,20))
    
    loppu = str(random.randint(2,899))
    
    vuosisadanluku = vuosisadanluvut[random.randint(0,2)]
    
    #Lisää nollat lukujen eteen jos ne ovat liian pieniä
    if(int(paiva) < 10):
        paiva = "0" + str(paiva)
        
    if(int(kuukausi) < 10):
        kuukausi = "0" + str(kuukausi)
        
    if(int(vuosi) < 10):
        vuosi = "0" + str(vuosi)
        
    if(int(loppu) < 10):
        loppu = "0" + str(loppu)
        
    if(int(loppu) < 100):
        loppu = "0" + str(loppu)
        
    #Tekee numeroista pätkän 
    numero = str(paiva) + str(kuukausi) + str(vuosi) + str(loppu)
    
    #Laskee tarkistusluvun
    tarkistusluku = tarkistusmerkit[ round((float(numero)/31 - math.floor(float(numero)/31)) * 31)]
    
    #Yhdistää kaiken yhteen henkilötunnukseksi
    henk = str(paiva) + str(kuukausi) + str(vuosi) + str(vuosisadanluku) + str(loppu) + str(tarkistusluku)
    
    print(henk)

def Henk(paiva, kuukausi, vuosi, vuosisata, loppu):
    
    #Lisää nollat lukujen eteen jos ne ovat liian pieniä
    if(int(paiva) < 10):
        paiva = "0" + str(paiva)
        
    if(int(kuukausi) < 10):
        kuukausi = "0" + str(kuukausi)
        
    if(int(vuosi) < 10):
        vuosi = "0" + str(vuosi)
        
    if(int(loppu) < 10):
        loppu = "0" + str(loppu)
        
    if(int(loppu) < 100):
        loppu = "0" + str(loppu)
    
    #Tekee numeroista pätkän 
    numero = str(paiva) + str(kuukausi) + str(vuosi) + str(loppu)
    
    #Laskee tarkistusluvun
    tarkistusluku = tarkistusmerkit[ round((float(numero)/31 - math.floor(float(numero)/31)) * 31)]
    
    #Yhdistää kaiken yhteen henkilötunnukseksi
    henk = str(paiva) + str(kuukausi) + str(vuosi) + str(vuosisadanluvut[vuosisata]) + str(loppu) + str(tarkistusluku)
    
    print(henk)
    
RandomHenk()
Henk(7,8,12,2,357)
