#mendefinisikan sebuah fungsi
import math 

#membuat sistem berjalan berulang-ulang
while True:

#menampilkan menu pilihan
    print("=== MENU LINGKARAN ===")
    print("1. hitung keliling lingkaran")
    print("2. hitung luas lingkaran")
    print("3. keluar")
    print("===============================")

#user memasukkan pilihan menu
    pilihan = input("masukkan pilihan anda (1,2, atau 3): ")

#mengeluarkan user dari program (pilihan 3)
    if pilihan == '3':
        print("program selesai, danke!")
        break  #menghentikan program

#mengonfirmasi apakah pilihan valid atau tidak
    if pilihan != "1" and pilihan != "2":
        print("pilihan tidak valid")
        continue  #kembali ke awal program

#meminta masukan nilai jari-jari (hanya pilihan 1 dan 2)
    try:
        jari_jari = float(input("masukkan nilai jari-jari lingkaran: "))
    except ValueError:  #berfungsi sebagai pengantisipasi bila terjadinya error
        print("input jari-jari harus berupa angka!\n")
        continue  #kembali ke awal program

#memproses pilihan user
    if pilihan == '1':
        #rumus keliling = 2 * pi * r
        keliling =  2 * math.pi * jari_jari
        print(f"-> keliling lingkaran dengan jari-jari {jari_jari} adalah: {keliling:.2f}\n")

    elif pilihan == '2':
        #rumus luas lingkaran = pi * r^2
        luas = math.pi * (jari_jari ** 2)
        print(f"-> luas lingkaran dengan jari-jari {jari_jari} adalah: {luas:.2f}\n")

#if itu menyatakan jika
#elif itu menyatakan atau
#else itu pilihan terakhir ketika kondisi if dan elif tidak terpenuhi
#\n digunakan untuk membuat baris baru sama seperti <br> di HTML
#.1f itu satu angka dibelakang koma, kalau .2f itu dua angka di belakang koma begitu seterusnya karena fungsi utamanya digunakan untuk merapikan angka desimal agar tidak berantakan