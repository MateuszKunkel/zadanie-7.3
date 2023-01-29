import sys
import logging
import random
from faker import Faker

fake = Faker()


class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

        self._label_length = 0

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.email}"

    def __repr__(self):
        return f"Card(imie = {self.imie}, nazwisko = {self.nazwisko}. email = {self.email})"

    def contact(self):
        print(
            f"Wybieram numer +48 {self.telefon} i dzwonię do {self.imie} {self.nazwisko}"
        )

    @property
    def label_length(self):
        print(len(self.imie))
        print(len(self.nazwisko))
        self._label_length = len(self.imie) + len(self.nazwisko)
        print(self._label_length)
        return self._label_length


class BusinessContact(BaseContact):
    def __init__(self, stanowisko, firma, telefonsluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefonsluzbowy = telefonsluzbowy

    def contact(self):
        print(
            f"Wybieram numer służbowy +48 {self.telefonsluzbowy} i dzwonię do {self.imie} {self.nazwisko}, na funkcji {self.stanowisko}"
        )

    @property
    def label_length(self):

        self._label_length = len(self.imie) + len(self.nazwisko)
        print(self._label_length)
        return self._label_length


def create_contacts(typ, ilosc):

    remainingCards = int(ilosc)

    indexNumber = 1

    if typ == "N":
        while remainingCards > 0:
            czlowiek = "człowiek" + str(indexNumber)
            czlowiek = BaseContact(
                imie=fake.first_name(),
                nazwisko=fake.last_name(),
                telefon=random.randint(100000000, 999999999),
                email=fake.email(),
            )
            list.append(czlowiek)
            indexNumber += 1
            remainingCards -= 1

    elif typ == "B":
        while remainingCards > 0:
            czlowiek = "człowiek" + str(indexNumber)
            czlowiek = BusinessContact(
                imie=fake.first_name(),
                nazwisko=fake.last_name(),
                telefon=random.randint(100000000, 999999999),
                email=fake.email(),
                stanowisko=fake.job(),
                firma=fake.company(),
                telefonsluzbowy=random.randint(100000000, 999999999),
            )
            list.append(czlowiek)
            indexNumber += 1
            remainingCards -= 1

    else:
        print("zła litera?")


if __name__ == "__main__":

    list = []

    create_contacts(
        input(
            "proszę wybrać rodzaj karty ('N' dla BaseContact lub 'B' dla BusinessContact):"
        ),
        input(
            "oraz ilość kart do wygenerowania:"
        ),
    )

    # poniższy kod należy do nieobowiązkowej częsci polecenia. Można go "odhaszować" w celu sprawdzenia poprawnosci działania programu.

    # odblokuj poniższe aby dodać do programu pytanie sprawdzające funkcję "contact" i zwrócić połączenie z wybraną osobą.

    # person = int(input("wybierz do kogo z kolei na liście chcesz zadzwonić:"))
    # list[person].contact()

    # odblokuj poniższe aby dodać do programu pytanie sprawdzające atrybut "label_length" i zwrócić wyliczoną długość.

    # person = int(input("wybierz czyją z kolei na liście długość imienia i nazwiska chcesz poznać:"))
    # list[person].label_length

    # odblokuj poniższe aby dodać do programu sortowanie listy po konkretnych parametrach i wydrukowanie jej w celu sprawdzenia poprawności.

    # by_imie = sorted(list, key=lambda Card: Card.imie)
    # print(by_imie)
    # by_nazwisko = sorted(list, key=lambda Card: Card.nazwisko)
    # print(by_nazwisko)
    # by_email = sorted(list, key=lambda Card: Card.email)
    # print(by_email)
