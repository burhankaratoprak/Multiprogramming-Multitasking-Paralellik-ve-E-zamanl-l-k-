import numpy as np

def amdahl_yasa(paralel, islemci):
    islemci_sayi = islemci  
    hizlanma = 1 / ((1 - paralel) + (paralel / islemci))
    return islemci_sayi , hizlanma

islemci = 8
paralel = 0.8

islemci_sayi, hizlanma = amdahl_yasa(paralel, islemci)
print(f"İşlemci Sayıları: {islemci_sayi}")
print(f"Hızlanma Faktörleri: {hizlanma}")
