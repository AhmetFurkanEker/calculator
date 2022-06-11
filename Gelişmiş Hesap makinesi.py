import math
import modül
import ımage
print("""*********
Hesap Makinesi 
Toplama = 1
Çıkarma = 2
Çarpma = 3
Bölme = 4
Üs almak için = 5
Sayının karekökünü almak için = 6 
Sayının logaritması için = 7
dereceyi radyana çevirmek için = 8
radyanı dereceye çevirmek için = 9
sinüs ü bulmak için = 10

*********""")


while True :
    seçim = int(input("Seçiminizi Giriniz : "))

    if (seçim == "q" ):
        print("İşlem sonlanıdırılıyor")
        break

    elif(seçim == 1):
        modül.tekrar_input_toplama()

    elif(seçim == 2 ):
        modül.tekrar_input_çıkarma()

    elif seçim == 3 :
        modül.tekrar_input_çarpma(),

    elif seçim == 4 :
        modül.bölme()

    elif seçim == 5 :
        modül.üs_alma()

    elif seçim == 6 :
        modül.kök_alma()

    elif seçim == 7 :
        modül.logaritma()

    elif seçim == 8 :
        modül.derece_radyan()
    elif seçim == 9 :
        modül.radyan_derece()
    elif seçim == 10 :
        ımage.sinüs_bulma()
