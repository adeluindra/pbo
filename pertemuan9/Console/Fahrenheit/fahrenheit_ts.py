print("Konversi Suhu Fahrenheit")
def get_celcius(suhu):
    C = (5/9 * (float(suhu) - 32))
    return C

def get_reamur(suhu):
    R = (4/9 * (float(suhu) - 32))
    return R

def get_kelvin(suhu):
    K = (5/9 * (float(suhu) - 32)) + 273.15
    return K

suhu = input("Masukan Suhu Dalam Fahrenheit:")

C = get_celcius(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)

print(suhu + " fahrenheit sama dengan ")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")