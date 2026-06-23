class Állatfaj:
    def __init__(self, fajnév, tömeg):
        self.fajnév = fajnév
        self.tömeg = tömeg

fajnév = input("mi az állat neve?: ")
tömeg = input("mennyi az állat tömege?: ")

állat = [Állatfaj(fajnév, tömeg)]

print(f"Az állat: {állat[0].fajnév}, {állat[0].tömeg} kg")