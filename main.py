class Flugzeug:
    def __init__(self, flugzeugstyp, maximale_passagierkapazität, aktuelle_passagiersanzahl):
        self.flugzeugstyp = flugzeugstyp
        self.maximale_passagierkapazität = maximale_passagierkapazität
        self.aktuelle_passagiersanzahl = aktuelle_passagiersanzahl
        if self.aktuelle_passagiersanzahl > self.maximale_passagierkapazität:
            self.aktuelle_passagiersanzahl = 0
            print(f'Es gibt nur {self.maximale_passagierkapazität} sitzplätze im {self.flugzeugstyp}! '
                  f'Daten der Passagiersanzahl werden durch "0" ersetzen!')

    def __eq__(self, other):
        if isinstance(other, Flugzeug):
            return other.flugzeugstyp == self.flugzeugstyp

    def __add__(self, other):
        return self.aktuelle_passagiersanzahl + other

    def __sub__(self, other):
        return self.aktuelle_passagiersanzahl - other

    def __iadd__(self, other):
        self.aktuelle_passagiersanzahl += other
        return self.aktuelle_passagiersanzahl

    def __isub__(self, other):
        self.aktuelle_passagiersanzahl -= other
        return self.aktuelle_passagiersanzahl

    def __lt__(self, other):
        return self.aktuelle_passagiersanzahl < other.aktuelle_passagiersanzahl

    def __le__(self, other):
        return self.aktuelle_passagiersanzahl <= other.aktuelle_passagiersanzahl

    def __gt__(self, other):
        return self.aktuelle_passagiersanzahl > other.aktuelle_passagiersanzahl

    def __ge__(self, other):
        return self.aktuelle_passagiersanzahl >= other.aktuelle_passagiersanzahl

    def __str__(self):
        return f'{self.flugzeugstyp} {self.maximale_passagierkapazität}'

    def __int__(self):
        return self.aktuelle_passagiersanzahl


boeing = Flugzeug("Passagiersflugzeug", 189, 180)
boeing1 = Flugzeug("Passagiersflugzeug", 189, 189)

print(boeing == boeing1)
print(boeing.__lt__(boeing1))
print(boeing.__iadd__(-100))
print(boeing1.__lt__(boeing))
print(boeing.__str__())
print(boeing.__int__())