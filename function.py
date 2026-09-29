def konversi_suhu(suhu, satuan):
     if satuan == "C":
        fahrenheit = (suhu * 9/5) + 32
        return fahrenheit
        elif satuan == "F":
        celsius = (suhu - 32) * 5/9
        return celsius
         else:
        return "Satuan tidak valid"

print("25 C =", konversi_suhu(25, "C"), "F")
print("77 F =", konversi_suhu(77, "F"), "C")

import math
luas_lingkaran = lambda r: math.pi * r**2
jari_jari = 7
print("Luas lingkaran =", luas_lingkaran(jari_jari))

import math

luas_lingkaran = lambda r: math.pi * r**2

jari_jari = 7
print("Luas lingkaran =", round(luas_lingkaran(jari_jari), 2))

lambda r: math.pi * r**2