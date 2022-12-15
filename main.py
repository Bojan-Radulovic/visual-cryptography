import secrets
import os.path
from os import path
from PIL import Image, ImageDraw


def kriptiranje():
    unos_ispravan = False
    while not unos_ispravan:
        print("Upisite puno ime slike koju zelite kriptirati (mora se nalaziti u mapi programa): ")
        ime_slike = input().rstrip()
        unos_ispravan = True

        if ime_slike == "0":
            exit()

        if not path.exists(ime_slike):
            print("Ta slika ne postoji, probajte ponovo")
            unos_ispravan = False

        if not (ime_slike.endswith(".jpg") or ime_slike.endswith(".jpeg") or ime_slike.endswith(".png")):
            print("Taj format datoteke nije podrzan, probajte ponovo")
            unos_ispravan = False

    print("Molim pricekajte...")

    slika = Image.open(ime_slike).convert('1')

    ime_slike_bez_nastavka = os.path.splitext(ime_slike)[0]

    sirina_output = slika.size[0] * 2
    visina_output = slika.size[1] * 2

    output1 = Image.new('1', (sirina_output, visina_output))
    output2 = Image.new('1', (sirina_output, visina_output))
    draw1 = ImageDraw.Draw(output1)
    draw2 = ImageDraw.Draw(output2)

    uzorci = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 1))

    for x in range(0, int(sirina_output / 2)):
        for y in range(0, int(visina_output / 2)):
            pixel = slika.getpixel((x, y))
            pat = secrets.choice(uzorci)
            draw1.point((x * 2, y * 2), pat[0])
            draw1.point((x * 2 + 1, y * 2), pat[1])
            draw1.point((x * 2, y * 2 + 1), pat[2])
            draw1.point((x * 2 + 1, y * 2 + 1), pat[3])
            if pixel == 0:
                draw2.point((x * 2, y * 2), 1 - pat[0])
                draw2.point((x * 2 + 1, y * 2), 1 - pat[1])
                draw2.point((x * 2, y * 2 + 1), 1 - pat[2])
                draw2.point((x * 2 + 1, y * 2 + 1), 1 - pat[3])
            else:
                draw2.point((x * 2, y * 2), pat[0])
                draw2.point((x * 2 + 1, y * 2), pat[1])
                draw2.point((x * 2, y * 2 + 1), pat[2])
                draw2.point((x * 2 + 1, y * 2 + 1), pat[3])

    output1.save(ime_slike_bez_nastavka + "_1.png", 'PNG')
    output2.save(ime_slike_bez_nastavka + "_2.png", 'PNG')

    print("Slika kriptirana")
def dekriptiranje():
    iste = False
    while not iste:
        iste = True
        unos_ispravan = False
        while not unos_ispravan:
            print("Upisite puno ime 1. slike koju zelite dekriptirati (mora se nalaziti u mapi programa): ")
            ime_slike1 = input().rstrip()
            unos_ispravan = True

            if ime_slike1 == "0":
                exit()

            if not path.exists(ime_slike1):
                print("Ta slika ne postoji, probajte ponovo")
                unos_ispravan = False

            if not (ime_slike1.endswith(".jpg") or ime_slike1.endswith(".png")):
                print("Taj format datoteke nije podrzan, probajte ponovo")
                unos_ispravan = False

        unos_ispravan = False
        while not unos_ispravan:
            print("Upisite puno ime 2. slike koju zelite dekriptirati (mora se nalaziti u mapi programa): ")
            ime_slike2 = input().rstrip()
            unos_ispravan = True

            if ime_slike2 == "0":
                exit()

            if not path.exists(ime_slike2):
                print("Ta slika ne postoji, probajte ponovo")
                unos_ispravan = False

            if not (ime_slike2.endswith(".jpg") or ime_slike2.endswith(".png")):
                print("Taj format datoteke nije podrzan, probajte ponovo")
                unos_ispravan = False

        slika1 = Image.open(ime_slike1).convert('1')
        slika2 = Image.open(ime_slike2).convert('1')

        sirina = int(slika1.size[0]/2)
        duzina = int(slika1.size[1]/2)

        if not (sirina == int(slika2.size[0]/2) and duzina == int(slika2.size[1]/2)):
            print("Slike nisu istih velicina, probajte ponovo")
            iste = False

    print("Molim pricekajte...")

    ime_slike_bez_nastavka1 = os.path.splitext(ime_slike1)[0]
    ime_slike_bez_nastavka2 = os.path.splitext(ime_slike2)[0]

    output = Image.new('1', (sirina, duzina))
    draw = ImageDraw.Draw(output)

    for x in range(0, int(sirina*2), 2):
        for y in range(0, int(duzina*2), 2):
            pixel11 = slika1.getpixel((x, y))
            pixel12 = slika1.getpixel((x+1, y))
            pixel13 = slika1.getpixel((x, y+1))
            pixel14 = slika1.getpixel((x+1, y+1))
            pixel21 = slika2.getpixel((x, y))
            pixel22 = slika2.getpixel((x+1, y))
            pixel23 = slika2.getpixel((x, y+1))
            pixel24 = slika2.getpixel((x+1, y+1))

            if pixel11 == pixel21 and pixel12 == pixel22 and pixel13 == pixel23 and pixel14 == pixel24:
                draw.point((x/2, y/2), 1)
            else:
                draw.point((x/2, y/2), 0)

    output.save(ime_slike_bez_nastavka1 + "+" + ime_slike_bez_nastavka2 + ".png", 'PNG')
    print("Dekriptiranje zavrseno")

while 1:
    print("1) Kriptiranje slike")
    print("2) Dekriptiranje slike")
    print("0) Izlaz")
    print("Upisite vas odabir: ")
    unos = input();

    if unos == "0":
        exit()

    elif unos == "1":
        kriptiranje()

    elif unos == "2":
        dekriptiranje()

    else:
        print("Krivi unos, probajte ponovo")


