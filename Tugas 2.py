import math

def hitung_luas_dan_keliling(jari_jari):
    keliling = 2 * math.pi * jari_jari
    luas = math.pi * jari_jari ** 2
    print("Keliling Lingkaran:", keliling)
    print("Luas Lingkaran:", luas)

def main():
    jari_jari = float(input("Masukkan jari-jari: "))
    hitung_luas_dan_keliling(jari_jari)

main()