def kalkulator():
    while True:
        print("\n=== Kalkulator Sederhana ===")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Keluar")

        pilihan = input("Pilih operasi (1/2/3/4/5): ")

        if pilihan == '5':
            print("Terima kasih, program selesai!")
            break

        if pilihan in ('1', '2', '3', '4'):
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Error: Masukkan angka yang valid!")
                continue

            if pilihan == '1':
                hasil = a + b
                print(f"Hasil: {a} + {b} = {hasil}")
            elif pilihan == '2':
                hasil = a - b
                print(f"Hasil: {a} - {b} = {hasil}")
            elif pilihan == '3':
                hasil = a * b
                print(f"Hasil: {a} * {b} = {hasil}")
            elif pilihan == '4':
                if b != 0:
                    hasil = a / b
                    print(f"Hasil: {a} / {b} = {hasil}")
                else:
                    print("Error: Tidak bisa dibagi dengan nol!")
        else:
            print("Pilihan tidak valid, coba lagi!")

kalkulator()
