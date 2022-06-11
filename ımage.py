from PIL import Image

def sinüs_bulma():
    img = Image.open('/home/ahmtfurkan/Desktop/Fonksiyonlar Python/Stalk/TrigonometriDikUcgen.jpg')
    img.show()
    a = int(input("Lütfen A Kenarını Giriniz :"))
    hip = int(input("Lütfen Hipotenüs Kenarını Giriniz: "))
    sonuç = a / hip
    print(sonuç)
    print("Sonuç : ", a , "/" , hip)