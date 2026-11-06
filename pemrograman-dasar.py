# Soal 1
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Soal 2
while True:
    nama = input("Masukan nama : ")
    print("Nama saya", nama)

    if nama == "python":
        print("goodbye python")
        break

#soal 3
nama = "lukman"

while nama != "python":
    nama = str(input("Masukan nama: "))
    print("Nama saya", nama)

print("goodbye", nama)


#ilustrasi 3
while True:
    nama = input("Masukkan nama :")
    if nama == "lukman":
        print("Nama saya lukman")
    if nama == "cahyo":
        print("Nama saya cahyo")
    if nama == "python":
        print("goodbye python")
        break