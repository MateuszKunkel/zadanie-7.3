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
        return f"Card(imie = {self.imie}, nazwisko = {self.nazwisko}, email = {self.email})"

    def contact(self):
        print(
            f"Wybieram numer +48 {self.telefon} i dzwonię do {self.imie} {self.nazwisko}"
        )

    @property
    def label_length(self):
        self._label_length = len(self.imie) + len(self.nazwisko)
        print(self._label_length)


class BusinessContact(BaseContact):
    def __init__(self, stanowisko, firma, telefonsluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefonsluzbowy = telefonsluzbowy

    def __repr__(self):
        return f"BusinessCard(imie = {self.imie}, nazwisko = {self.nazwisko}, email = {self.email}, stanowisko = {self.stanowisko})"

    def contact(self):
        print(
            f"Wybieram numer służbowy +48 {self.telefonsluzbowy} i dzwonię do {self.imie} {self.nazwisko}, na funkcji {self.stanowisko}"
        )


def create_contacts(typ, ilosc):

    remaining_cards = int(ilosc)

    index_number = 1

    if typ == "N":
        while remaining_cards > 0:
            czlowiek = BaseContact(
                imie=fake.first_name(),
                nazwisko=fake.last_name(),
                telefon=random.randint(100000000, 999999999),
                email=fake.email(),
            )
            list.append(czlowiek)
            index_number += 1
            remaining_cards -= 1

    elif typ == "B":
        while remaining_cards > 0:
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
            index_number += 1
            remaining_cards -= 1

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

    # drukowanie listy.

    print(list)

    # poniższy kod dodaje do programu pytanie sprawdzające funkcję "contact" i zwraca połączenie z wybraną osobą.

    person = int(input("wybierz do kogo z kolei na liście chcesz zadzwonić:"))
    list[person - 1].contact()

    # poniższy kod dodaje do programu pytanie sprawdzające atrybut "label_length" i zwraca wyliczoną długość.

    person = int(input("wybierz czyją z kolei na liście długość imienia i nazwiska chcesz poznać:"))
    list[person - 1].label_length

    # odblokuj poniższe aby dodać do programu sortowanie listy po konkretnych parametrach i wydrukowanie jej w celu sprawdzenia poprawności.

    # by_imie = sorted(list, key=lambda Card: Card.imie)
    # print(by_imie)
    # by_nazwisko = sorted(list, key=lambda Card: Card.nazwisko)
    # print(by_nazwisko)
    # by_email = sorted(list, key=lambda Card: Card.email)
    # print(by_email)
