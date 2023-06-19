def penjumlahan(angka1, angka2):
    return angka1 + angka2

def perkalian(angka1, angka2):
    return angka1 * angka2

def pembagian(angka1, angka2):
    return angka1 / angka2

def pengurangan(angka1, angka2):
    return angka1 - angka2

def pangkat(angka1, angka2):
    return angka1 ** angka2

def kalkulator():
    print("KALKULATOR")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pembagian")
    print("4. Pengurangan")
    print("5. Pangkat")

    pilihan = int(input("Masukkan pilihan: "))

    angka1 = int(input("Bilangan pertama: "))
    angka2 = int(input("Bilangan kedua: "))

    if pilihan == 1:
        hasil = penjumlahan(angka1, angka2)
        print("Hasil Penjumlahan:", hasil)
    elif pilihan == 2:
        hasil = perkalian(angka1, angka2)
        print("Hasil Perkalian:", hasil)
    elif pilihan == 3:
        hasil = pembagian(angka1, angka2)
        print("Hasil Pembagian:", hasil)
    elif pilihan == 4:
        hasil = pengurangan(angka1, angka2)
        print("Hasil Pengurangan:", hasil)
    elif pilihan == 5:
        hasil = pangkat(angka1, angka2)
        print("Hasil Pangkat:", hasil)
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

kalkulator()