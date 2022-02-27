class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938)
buku2 = Buku('Psychology Of Money', 'Morgan Housel', 2022)
buku3 = Buku('Harry Potter', 'Mahabarata', 1997)


data_buku = [buku1, buku2, buku3]

print('Daftar Buku')
for b in data_buku:
    print(
        f'Buku {b.judul} karangan {b.pengarang} pertama kali diterbitkan tahun {b.tahun_terbit}')