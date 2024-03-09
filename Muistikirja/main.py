# -*- coding: cp1252 -*-

import time
import os
import pickle


def muistio():
    tiedostonimi = "muistio.dat"
    if not os.path.exists(tiedostonimi):
        print("Virhe tiedostossa, luodaan uusi", tiedostonimi, ".")
        tiedosto = open(tiedostonimi, "wb")
        tiedosto.close()

    return tiedostonimi


def main():
    lista = []
    tiedostonimi = muistio()
    jatka = True
    while jatka:
        Valinta = int(input(
            "(1) Lue muistikirjaa \n(2) Lisää merkintä \n(3) Muokkaa merkintää \n(4) Poista merkintä \n(5) Tallenna ja lopeta \n\nMitä haluat tehdä?: "))

        if Valinta == 1:
            tiedosto = open(tiedostonimi, "rb")
            sisalto = pickle.load(tiedosto)
            tiedosto.close()
            for i in sisalto:
                print(i)

        elif Valinta == 2:
            tiedosto = open(tiedostonimi, "wb")
            lause = input("Kirjoita uusi merkintä: ")
            aika = time.strftime("%X %x")
            lisaa = lause + ":::" + aika
            lista.append(lisaa)
            pickle.dump(lista, tiedosto)
            tiedosto.close()

        elif Valinta == 3:
            tiedosto = open(tiedostonimi, "rb")
            sisalto = pickle.load(tiedosto)
            tiedosto.close()
            print("Listalla on", len(lista), "merkintää.")
            syote = int(input("Mitä niistä muutetaan?: ")) - 1
            print(sisalto[syote])
            korvaus = input("Anna uusi teksti: ")
            uusituote = korvaus + ":::" + time.strftime("%X %x")
            lista.pop(syote)
            lista.insert(syote, uusituote)
            tiedosto = open(tiedostonimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()

        elif Valinta == 4:
            tiedosto = open(tiedostonimi, "rb")
            sisalto = pickle.load(tiedosto)
            tiedosto.close()

            print("Listalla on", len(lista), "merkintää. ")
            syote = int(input("Mitä niistä poistetaan?: ")) - 1
            print("Poistettiin merkintä ", sisalto[syote])
            lista.pop(syote)
            tiedosto = open(tiedostonimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()

        elif Valinta == 5:
            print("Lopetetaan.")
            jatka = False


if __name__ == "__main__":
    main()
