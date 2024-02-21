DataNilai = {
    1: {'nama': 'Kaila', 'pelajaran': 'Matematika', 'ujian': 92, 'tugas': 85},
    2: {'nama': 'Tyfal', 'pelajaran': 'Bahasa Inggris', 'ujian': 90, 'tugas': 87},
    3: {'nama': 'Lala', 'pelajaran': 'Fisika', 'ujian': 95, 'tugas': 85},
    4: {'nama': 'Roby', 'pelajaran': 'Matematika', 'ujian': 88, 'tugas': 90},
    5: {'nama': 'Hafiz', 'pelajaran': 'Fisika', 'ujian': 95, 'tugas': 79}
}

RecycleBin = {}

def main():
    while True:
        try:
            menu_option = int(input('''
    DATA NILAI SISWA KELAS VII
    Main Menu:
    1. Buka Data Siswa
    2. Tambah Data Siswa
    3. Edit Data Siswa
    4. Hapus Data Siswa
    5. Buka Recycle Bin
    6. Exit Program

    Input Menu Option : '''))

            if menu_option == 1:
                daftar_data_siswa()
            elif menu_option == 2:
                buat_data_siswa()
            elif menu_option == 3:
                update_data_siswa()
            elif menu_option == 4:
                delete_data_siswa()
            elif menu_option == 5:
                open_recycle_bin()
            elif menu_option == 6:
                break
            else:
                print("\n\tMohon maaf, input menu yang Anda masukkan salah.")
        except ValueError:
            print("\n\tMohon maaf, input menu harus berupa angka.")
        

def buat_data_siswa():
    while True:
        menu_option = int(input('''
    Menambahkan Data Nilai Siswa
    1. Tambah Data
    2. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            id_tambah = int(input('''
    Tambah Data Nilai Siswa
    Masukkan ID data yang ingin ditambahkan: '''))

            if id_tambah in DataNilai:
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) sudah ada.".format(id_tambah))
            else:
                DataNilai[id_tambah] = {}

                print("\n\tTambah Data Nilai Siswa")
                while True:
                    nama_siswa = input("\tMasukkan Nama Siswa: ")
                    if nama_siswa.isalpha():
                        break
                    else:
                        print("\tNama Siswa harus berupa huruf saja.")
                while True:
                        mata_pelajaran = input("\tMasukkan Mata Pelajaran: ")
                        if mata_pelajaran.isalpha():
                            break
                        else:
                            print("\tMata Pelajaran harus berupa huruf saja.")
                while True:
                    try:
                        nilai_ujian = int(input("\tMasukkan Nilai Ujian: "))
                        break
                    except ValueError:
                        print("\tNilai Ujian harus berupa angka.")

                while True:
                    try:
                        nilai_tugas = int(input("\tMasukkan Nilai Tugas: "))
                        break
                    except ValueError:
                        print("\tNilai Tugas harus berupa angka.")

                simpan_data = input("\tApakah Anda yakin menambahkan data yang baru Anda masukkan untuk ID: {}? "
                                    .format(id_tambah))

                if simpan_data.lower() == "ya":
                    print("\n\tSukses, data berhasil ditambahkan.")
                    DataNilai[id_tambah]['nama'] = nama_siswa
                    DataNilai[id_tambah]['pelajaran'] = mata_pelajaran
                    DataNilai[id_tambah]['ujian'] = nilai_ujian
                    DataNilai[id_tambah]['tugas'] = nilai_tugas
                else:
                    print("\n\tMohon maaf, data tidak berhasil ditambahkan.")

        elif menu_option == 2:
            break
        else:
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def daftar_data_siswa():
    border = '=' * 60

    while True:
        menu_option = int(input('''
    Menampilkan Data Nilai Siswa
    1. Tampilkan Seluruh Data
    2. Cari Data Berdasarkan Index
    3. Tampilkan Seluruh Data dengan Urutan Nilai Ujian Tertinggi
    4. Tampilkan Seluruh Data dengan Urutan Nilai Tugas Tertinggi
    5. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            if len(DataNilai) == 0:
                print("\n\tMohon maaf, tidak ada data nilai siswa yang dapat ditampilkan.")
            else:
                print("""
    Menampilkan Seluruh Data Nilai Siswa
    {}
    {:>5} | {:<15} | {:<15} | {:<12} | {:<12}
    {}""".format(border, "No", "Nama Siswa", "Mata Pelajaran", "Nilai Ujian", "Nilai Tugas", border))
                for i in DataNilai:
                  
                    print("\t{:>1} | {:<15} | {:<15} | {:<12} |{:<12}".format
                          (i, DataNilai[i]['nama'], DataNilai[i]['pelajaran'], DataNilai[i]['ujian'], DataNilai[i]['tugas']))


        elif menu_option == 2:
            id_cari = int(input('''
    Cari Data Berdasarkan ID
    Masukkan ID data yang ingin dicari: '''))

            if id_cari not in DataNilai.keys():
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_cari))
            else:
                print("""
    Menampilkan Data Nilai Siswa Berdasarkan ID: {}
    {}
    {} | {:<15} | {:<15} | {:<12} | {:<12}
    {}
    {:>2} | {:<15} | {:<15} | {:<12} | {:<12}
    {}""".format(id_cari, border, "No", "Nama Siswa", "Mata Pelajaran", "Nilai Ujian", "Nilai Tugas", border, id_cari,
                 DataNilai[id_cari]['nama'], DataNilai[id_cari]['pelajaran'], DataNilai[id_cari]['ujian'], DataNilai[id_cari]['tugas'], border))
        elif menu_option == 3:
            if len(DataNilai) == 0:
                print("\n\tMohon maaf, tidak ada data nilai siswa yang dapat ditampilkan.")
            else:
                print("""
    Menampilkan Seluruh Data Nilai Siswa dengan Urutan Nilai Ujian Tertinggi
    {}
    {:>5} | {:<15} | {:<15} | {:<12} | {:<12}
    {}""".format(border, "No", "Nama Siswa", "Mata Pelajaran", "Nilai Ujian", "Nilai Tugas", border))

                sorted_data = sorted(DataNilai.items(), key=lambda x: x[1]['ujian'], reverse=True)

                for i, (key, value) in enumerate(sorted_data, start=1):
                    print("\t{:>1} | {:<15} | {:<15} | {:<12} |{:<12}".format
                          (i, value['nama'], value['pelajaran'], value['ujian'], value['tugas']))
                          
        elif menu_option == 4:
            if len(DataNilai) == 0:
                print("\n\tMohon maaf, tidak ada data nilai siswa yang dapat ditampilkan.")
            else:
                print("""
    Menampilkan Seluruh Data Nilai Siswa dengan Urutan Nilai Ujian Tertinggi
    {}
    {:>5} | {:<15} | {:<15} | {:<12} | {:<12}
    {}""".format(border, "No", "Nama Siswa", "Mata Pelajaran", "Nilai Ujian", "Nilai Tugas", border))

                sorted_data = sorted(DataNilai.items(), key=lambda x: x[1]['tugas'], reverse=True)

                for i, (key, value) in enumerate(sorted_data, start=1):
                    print("\t{:>1} | {:<15} | {:<15} | {:<12} |{:<12}".format
                          (i, value['nama'], value['pelajaran'], value['ujian'], value['tugas']))

        elif menu_option == 5:
            break
        else:
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")


def update_data_siswa():
    border = '=' * 60

    while True:
        menu_option = int(input('''
    Mengubah Data Nilai Siswa
    1. Ubah Data
    2. Kembali ke Menu Utama

    Input Menu Option : '''))

        if menu_option == 1:
            id_update = int(input('''
    Ubah Data Nilai Siswa
    Masukkan ID data yang ingin diubah: '''))

            if id_update not in DataNilai.keys():
                print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_update))
            else:
                
                print("""
    Menampilkan Data Nilai Siswa Berdasarkan ID: {}
    {}
    {} | {:<15} | {:<15} | {:<12} | {:<12}
    {}
    {:>2} | {:<15} | {:<15} | {:<12} | {:<12}
    {}""".format(id_update, border, "No", "Nama Siswa", "Mata Pelajaran", "Nilai Ujian", "Nilai Tugas", border, id_update,
                 DataNilai[id_update]['nama'], DataNilai[id_update]['pelajaran'], DataNilai[id_update]['ujian'],
                 DataNilai[id_update]['tugas'], border))

                print("\n\tUbah Data Nilai Siswa Untuk ID: {}".format(id_update))

                update_nama = input("\tApakah Anda ingin mengganti Nama Siswa? ")

                if update_nama.lower() == "ya":
                    while True:
                        nama_siswa = input("\tMasukkan Nama Siswa: ")
                        if nama_siswa.isalpha():
                            break
                        else:
                            print("\tNama Siswa harus berupa huruf saja.")
                else:
                    nama_siswa = DataNilai[id_update]['nama']

                update_pelajaran = input("\tApakah Anda ingin mengganti Mata Pelajaran? ")

                if update_pelajaran.lower() == "ya":
                    while True:
                        mata_pelajaran = input("\tMasukkan Mata Pelajaran: ")
                        if mata_pelajaran.isalpha():
                            break
                        else:
                            print("\tMata Pelajaran harus berupa huruf saja.")                   
                else:
                    mata_pelajaran = DataNilai[id_update]['pelajaran']

                update_ujian = input("\tApakah Anda ingin mengganti Nilai Ujian? ")

                if update_ujian.lower() == "ya":
                    while True:
                        try:
                            nilai_ujian = int(input("\tMasukkan Nilai Ujian: "))
                            break
                        except ValueError:
                            print("\tNilai Ujian harus berupa angka.")                 
                else:
                    nilai_ujian = DataNilai[id_update]['ujian']
   
                update_tugas = input("\tApakah Anda ingin mengganti Nilai Tugas? ")

                if update_tugas.lower() == "ya":
                    while True:
                        try:
                            nilai_tugas = int(input("\tMasukkan Nilai Tugas: "))
                            break
                        except ValueError:
                            print("\tNilai Tugas harus berupa angka.")                    
                else:
                    nilai_tugas = DataNilai[id_update]['tugas']

                print("\n\tSukses, data berhasil diubah.")
                DataNilai[id_update]['nama'] = nama_siswa
                DataNilai[id_update]['pelajaran'] = mata_pelajaran
                DataNilai[id_update]['ujian'] = nilai_ujian
                DataNilai[id_update]['tugas'] = nilai_tugas

        elif menu_option == 2:
            break
        else:
            print("\n\tMohon maaf, input menu yang Anda masukkan salah.")

def delete_data_siswa():
     
     while True:
         menu_option = int(input('''
     Menghapus Data Nilai Siswa
     1. Hapus Data
     2. Kembali ke Menu Utama

     Input Menu Option : '''))

         if menu_option == 1:
             id_delete = int(input('''
     Hapus Data Nilai Siswa
     Masukkan ID data yang ingin dihapus: '''))

             if id_delete not in DataNilai.keys():
                 print("\n\tMohon maaf, ID data yang Anda masukkan ({}) tidak ada.".format(id_delete))
             else:
                 hapus_data = input("\n\tApakah Anda yakin untuk menghapus data yang sesuai dengan ID: {}? "
                                    .format(id_delete))

                 if hapus_data.lower() == "ya":
                     print("\n\tSukses, data berhasil dihapus.")
                     del DataNilai[id_delete]
                 else:
                     print("\n\tMohon maaf, data tidak berhasil dihapus.")

         elif menu_option == 2:
             break
         else:
             print("\n\tMohon maaf, input menu yang Anda masukkan salah.")

def delete_data_siswa():
    while True:
        menu_option = int(input('''
    Delete Student Data
    1. Delete Data
    2. Back to Main Menu

    Input Menu Option : '''))

        if menu_option == 1:
            id_delete = int(input('''
    Delete Student Data
    Enter the ID of the data you want to delete: '''))

            if id_delete in DataNilai:
                move_to_recycle_bin(id_delete)
                print("\n\tData successfully moved to recycle bin.")
            else:
                print("\n\tID {} not found.".format(id_delete))
        elif menu_option == 2:
            break
        else:
            print("\n\tInvalid menu option. Please enter a valid option.")

def move_to_recycle_bin(student_id):
    RecycleBin[student_id] = DataNilai.pop(student_id)

def open_recycle_bin():
    while True:
        print("\nRecycle Bin:")
        for student_id, student_data in RecycleBin.items():
            print("\tID {}: {}".format(student_id, student_data))
        
        menu_option = int(input('''
    Recycle Bin Menu:
    1. Restore Data
    2. Back to Main Menu

    Input Menu Option : '''))

        if menu_option == 1:
            restore_data()
        elif menu_option == 2:
            break
        else:
            print("\n\tInvalid menu option. Please enter a valid option.")

def restore_data():
    id_restore = int(input('''
    Restore Data
    Enter the ID of the data you want to restore: '''))

    if id_restore in RecycleBin:
        DataNilai[id_restore] = RecycleBin.pop(id_restore)
        print("\n\tData successfully restored.")
    else:
        print("\n\tID {} not found in the recycle bin.".format(id_restore))



main()
