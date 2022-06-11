sayı_list = list()
list =[]
def tekrar_input_toplama():
    tekrar = int(input("Ne kadar Sayı Toplayacağınızı Yazınız :"))
    while True:
        sayı = int(input("Lütfen sayıyı giriniz : "))
        sayı_list.append(sayı)
        tekrar -= 1
        if tekrar == 0 :
            print("Sayıların toplamı : ", sum(sayı_list))
            break

def tekrar_input_çıkarma():
    tekrar = int(input("Ne kadar Sayı Çıkaracağınızı Yazınız :"))
    sayı_bir = int(input("Lütfen ilk sayıyı yazınız : "))
    sayı_list.append(sayı_bir)
    tekrar -= 1
    while True:
        sayı_diğerleri = int(input("Diğer sayıları Giriniz : "))
        sayı_diğerleri *= -1
        tekrar -= 1
        sayı_list.append(sayı_diğerleri)
        if(tekrar == 0 ):
            print("İşlem Sonucu ", sum(sayı_list))
            break

def tekrar_input_çarpma():
    tekrar = int(input("Ne kadar sayı çarpmak istiyorsunuz : "))
    while True:
        sayı = int(input("Çarpmak İstediğiniz Sayıyı Giriniz : "))
        list.append(sayı)
        tekrar -= 1
        if tekrar == 0 :
            sonuç = 1
            for i in list:
                sonuç = sonuç * i
                print(sonuç)

def bölme():
    x = int(input("Birinci Sayıyı Giriniz : "))
    y = int(input("İkinci Sayıyı Giriniz :"))

    sonuç = x / y
    print(sonuç)


def üs_alma():
    x = int(input("Üsü alınacak sayıyı giriniz : "))
    y = int(input("Sayının Üsünü Giriniz : "))
    sonuç = x ** y
    print(sonuç)


def kök_alma():
    x = int(input("Kökünü bulmak istediğiniz sayıyı giriniz : "))
    sonuç = x ** 0.5
    print(sonuç)

def logaritma():
    x = int(input("Logaritmasını almak istediğiniz sayıyı girin : "))
    for i in range(1,x+1):
        sayı_list.append(i)
        sonuç = 1
    for j in sayı_list:
        sonuç = sonuç * j
        print(sonuç)


def derece_radyan():
    print("""
    
    pi sayısı 3,14 kabul edilmiştir.
    
    """)
    x = int(input("Dereceyi giriniz :"))

    y = x *(3.14 / 180)
    print(y)


def radyan_derece():
    print("""

    pi sayısı 3,14 kabul edilmiştir.

    """)
    x = int(input("Radyanı giriniz :"))

    y = x * (180 / 3.14)
    print(y)























