def konversi_suhu(suhu, satuan):
     if satuan == "C":
        fahrenheit = (suhu * 9/5) + 32
        return fahrenheit
        elif satuan == "F":
        celsius = (suhu - 32) * 5/9
        return celsius
         else:
        return "Satuan tidak valid"
