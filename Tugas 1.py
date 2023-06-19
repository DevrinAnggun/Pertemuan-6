#Nilai bilangan genap sdan ganjil
def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def main():
    bilangan = int(input("Masukkan bilangan: "))
    hasil = cek_ganjil_genap(bilangan)
    print("Bilangan yang Anda masukkan adalah", hasil)

main()
