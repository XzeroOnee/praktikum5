# Agus Setiawan
# 312310597
# TI.23.A6

# Membuat Dictionary daftar kontak
kontak = {'Ari': '081267888', 'Dina': '087677776'}

# Menampilkan Kontak Ari
print("Kontak Ari", kontak['Ari'])

# Menambahkan kontak Riko
kontak['Riko'] = '087654544'

# Mengubah kontak Dina
kontak['Dina'] = '088999776'

# Tampilkan semua nama
for nama in kontak.keys():
    print(nama)

# Tampilkan semua nomor
for nomor in kontak.values():
    print(nomor)

# Tampilkan daftar Nama dan nomornya
for nama, nomor in kontak.items():
    print(f"{nama}: {nomor}")

# Menghapus kontak Dina
del kontak['Dina']