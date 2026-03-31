nama_user = input("Masukkan nama Anda : ")
umur_user = int(input("Masukkan umur Anda : "))

umur        = umur_user
tinggi      = 172.5
is_student  = True
hobi        = ["coding", "membaca", "gaming", "hiking", "musik"]

print("=" * 45)
print("        INFORMASI VARIABEL")
print("=" * 45)
print(f"Nama      : {nama_user}")
print(f"Umur      : {umur}")
print(f"Tinggi    : {tinggi} cm")
print(f"Mahasiswa : {is_student}")
print(f"Hobi      : {hobi}")

print("\n" + "=" * 45)
print("        MANIPULASI STRING")
print("=" * 45)
sapaan = "Halo, " + nama_user + "!"
print(f"Gabungan string : {sapaan}")
print(f"Panjang nama    : {len(nama_user)} karakter")
print(f"Huruf besar     : {nama_user.upper()}")
print(f"Huruf kecil     : {nama_user.lower()}")

print("\n" + "=" * 45)
print("        OPERASI MATEMATIKA")
print("=" * 45)
a, b = 17, 5
print(f"a = {a}, b = {b}")
print(f"Penjumlahan     : {a} + {b} = {a + b}")
print(f"Pengurangan     : {a} - {b} = {a - b}")
print(f"Perkalian       : {a} * {b} = {a * b}")
print(f"Pembagian       : {a} / {b} = {a / b:.2f}")
print(f"Pembagian bulat : {a} // {b} = {a // b}")
print(f"Modulus (sisa)  : {a} % {b} = {a % b}")

print("\n" + "=" * 45)
print("        LIST DAN AKSES ELEMEN")
print("=" * 45)
print(f"List hobi awal  : {hobi}")
print(f"Elemen index 0  : {hobi[0]}")
print(f"Elemen index 2  : {hobi[2]}")
print(f"Elemen terakhir : {hobi[-1]}")
hobi.append("memasak")
print(f"Setelah append  : {hobi}")
hobi.remove("gaming")
print(f"Setelah remove  : {hobi}")
hobi.pop()
print(f"Setelah pop     : {hobi}")

print("\n" + "=" * 45)
print("        INPUT DARI USER")
print("=" * 45)
print(f"\nHalo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
print("=" * 45)
