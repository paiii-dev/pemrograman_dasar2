while True:
    input_user = input("masukkan angka (atau ketik 'keluar' untuk berhenti): ")
    if input_user.lower() == 'keluar':
        print("program selesai")
        break

    try:
        angka = int(input_user)
        if angka % 2 ==0:
            print(f"-> angka {angka} adalah bilangan GENAP.\n")
            