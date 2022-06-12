from PIL import Image

def sinüs_bulma():
    img = Image.open('#Trigonometri konum ')
    img.show()
    a = int(input("Lütfen A Kenarını Giriniz :"))
    hip = int(input("Lütfen Hipotenüs Kenarını Giriniz: "))
    sonuç = a / hip
    print(sonuç)
    print("Sonuç : ", a , "/" , hip)
