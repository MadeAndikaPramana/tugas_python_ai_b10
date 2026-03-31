print("=" * 50)
print("LIST")
print("=" * 50)

data = ["apel", 42, "mangga", 3.14, True, "jeruk"]
print("List awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])
print("Slicing [1:5:2]:", data[1:5:2])

data.append("pisang")
print("Setelah append:", data)

data.insert(2, "semangka")
print("Setelah insert di index 2:", data)

data.extend(["nanas", "anggur"])
print("Setelah extend:", data)

data.pop()
print("Setelah pop:", data)

data.remove("semangka")
print("Setelah remove 'semangka':", data)

print("\n" + "=" * 50)
print("TUPLE")
print("=" * 50)

koordinat = (10, 20, 30, 40, 50)
print("Tuple:", koordinat)
print("Panjang:", len(koordinat))
print("Akses index 2:", koordinat[2])

a, b, *rest = koordinat
print("Unpacking - a:", a, "| b:", b, "| rest:", rest)

print("\n" + "=" * 50)
print("SET")
print("=" * 50)

set_a = {1, 2, 3, 4, 5, 3, 2}
set_b = {4, 5, 6, 7, 8}
print("Set A (duplikat dihapus otomatis):", set_a)
print("Set B:", set_b)
print("Union (|):", set_a | set_b)
print("Intersection (&):", set_a & set_b)
print("Difference A-B (-):", set_a - set_b)
print("Symmetric difference (^):", set_a ^ set_b)

print("\n" + "=" * 50)
print("DICTIONARY")
print("=" * 50)

mahasiswa = {
    "nama": "Andika",
    "nim": "2308561121",
    "angkatan": 2023,
    "kota": "Denpasar"
}
print("Data awal:", mahasiswa)

mahasiswa["ipk"] = 3.85
print("Setelah tambah key 'ipk':", mahasiswa)

mahasiswa["kota"] = "Bali"
print("Setelah ubah 'kota':", mahasiswa)

del mahasiswa["angkatan"]
print("Setelah hapus 'angkatan':", mahasiswa)

print("Keys:", list(mahasiswa.keys()))
print("Values:", list(mahasiswa.values()))
print("Items:", list(mahasiswa.items()))
for key, value in mahasiswa.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 50)
print("NESTED STRUCTURES")
print("=" * 50)

buku = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
    {"judul": "Bumi Manusia", "penulis": "Pramoedya", "tahun": 1980},
    {"judul": "Perahu Kertas", "penulis": "Dee Lestari", "tahun": 2009},
    {"judul": "Negeri 5 Menara", "penulis": "Ahmad Fuadi", "tahun": 2009},
]

print("Semua judul:")
for b in buku:
    print(" -", b["judul"])

tahun_filter = 2005
hasil_filter = [b["judul"] for b in buku if b["tahun"] >= tahun_filter]
print(f"Buku terbit >= {tahun_filter}:", hasil_filter)

print("\n" + "=" * 50)
print("COMPREHENSION")
print("=" * 50)

angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x ** 2 for x in angka]
print("Angka genap 1-20:", genap)
print("Kuadrat 1-20:", kuadrat)

parity = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Dict paritas 1-10:", parity)

kalimat = "belajar python itu menyenangkan"
huruf_unik = {c for c in kalimat.lower() if c != " "}
print("Huruf unik dari kalimat:", huruf_unik)

print("\n" + "=" * 50)
print("KEANGGOTAAN DAN PENCARIAN")
print("=" * 50)

buah = ["apel", "mangga", "jeruk", "pisang", "anggur"]
cari = "mangga"
print(f"'{cari}' ada dalam list:", cari in buah)
print(f"Posisi '{cari}':", buah.index(cari))

angka_set = {10, 20, 30, 40, 50}
print("25 ada dalam set:", 25 in angka_set)
print("30 ada dalam set:", 30 in angka_set)
