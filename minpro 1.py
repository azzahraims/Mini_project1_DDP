# Nama : Az-Zahra Imsawati Sugianto
# Nim : 2509116062
# Tugas : Minpro 1 Dasar Dasar Pemrograman

# List untuk kepanitiaan
kepanitiaan = []  


print("=== Sistem Manajemen Kepanitiaan Makrab FT 25 ===")

# Daftar divisi 
panitia = ["Ketua", "Sekretaris", "Bendahara", "Divisi Acara", "Divisi Humas", "Divisi PDD", "Divisi Keamanan", "Divisi Konsumsi", "Divisi Perkap"]


while True:
    print("\n === Kepanitiaan Makrab FT 25 ===")
    print("1. Tambah anggota")
    print("2. Tampilkan anggota")
    print("3. Hapus anggota")
    print("4. Keluar dari program")

    pilih_menu = input("Pilih Salah Satu dari Menu (1/2//3/4): ")


    # Create
    if pilih_menu == "1": 
        nama = input("Nama anggota: ")
        jabatan = input("Masukkan jabatan/divisi: ")
        tugas = input("Tugas dari jabatan/divisi: ")

        # Simpan Data Dalam Bentuk Tuple
        anggota = (nama, jabatan, tugas)
        kepanitiaan.append(anggota)

        print("Anggota berhasil ditambahkan")

    # Read
    elif pilih_menu == "2": 
        if len(kepanitiaan) == 0:
            print("Belum ada struktur kepanitiaan")
        else:
            print("\n Daftar kepanitiaan makrab. ")
            nomor = 1
            for anggota in kepanitiaan:
                print(f"{nomor}. Nama : {anggota[0]}, Jabatan : {anggota[1]}, Tugas : {anggota[2]}") 
                nomor += 1

    # Delate 
    elif pilih_menu == "3":
        if len(kepanitiaan) == 0:
            print("Struktur kepanitiaan masih kosong. Tidak ada data yang bisa dihapus")
        else:
            hapus_anggota = input("Masukkan nama anggota yang ingin dihapus: ")
            ketemu = False
        for i in range(len(kepanitiaan)):
            if kepanitiaan[i][0] == hapus_anggota:
                kepanitiaan.pop(i)
                print(f"{hapus_anggota} berhasil dihapus.")
                ditemukan = True
                break
            if not ketemu: 
                print("Anggota tidak ditemukan.")

# Exit
    elif pilih_menu == "4":
        print("Program ditutup. Semoga Kepanitiannya sukses!")
        break

    else:
        print("Pilihan tidak tersedia. Coba lagi.")



