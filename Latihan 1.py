sisi = int(input("masukkan sisi : "))

def hitung_keliling_persegi(sisi):
    keliling = 4 * sisi
    print("keliling dari persegi :", str(keliling))

    def hitung_luas_persegi(sisi):
        luas = sisi*sisi
        print("luas persegi : ", str(luas))

    hitung_keliling_persegi(sisi)
    hitung_luas_persegi(sisi)


def keliling_persegi(sisi):
    return 4*sisi

def luas_persegi(sisi):
    return sisi * sisi

panjang = int(input("Masukkan panjang sisi :"))
print("Keliling Persegi :", keliling_persegi(panjang))
print("Luas Persegi :", luas_persegi(panjang))
