class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk


m1 = Mahasiswa('Udin', '10120371', 'Sistem Informasi', 2020)
m2 = Mahasiswa('Agnesta Linda sari', '5210411167', 'Informatika', 2021)
m3 = Mahasiswa('Bella Triana', '5210411175', 'Informatika', 2021)
m4 = Mahasiswa('Eusebia Nawang Ari', '5210411195', 'Informatika', 2021)
m5 = Mahasiswa('Veratina Fridayanti', '5210411174', 'Informatika', 2021)




data_mahasiswa = [m1, m2, m3, m4, m5]

print('Daftar Mahasiswa')
for i in data_mahasiswa:
        print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim}')