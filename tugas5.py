def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"

    def __str__(self):
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )


if __name__ == "__main__":
    print("=" * 45)
    print("=== FUNCTIONS ===")
    print("=" * 45)

    print(greet("Arifian"))
    print("tambah(5, 7):", tambah(5, 7))
    print("tambah(10):", tambah(10))
    print("rata_rata([80, 90, 100]):", rata_rata([80, 90, 100]))
    print("rata_rata([]):", rata_rata([]))

    print("\n" + "=" * 45)
    print("=== CLASS STUDENT ===")
    print("=" * 45)

    s1 = Student("Andika", "2308561121")
    s1.tambah_nilai(85)
    s1.tambah_nilai(90)
    s1.tambah_nilai(78)
    print(s1)
    print("Rata-rata nilai:", s1.rata_nilai())
    print("Status:", s1.status())

    s2 = Student("Budi Santoso", "2308561200")
    s2.tambah_nilai(60)
    s2.tambah_nilai(55)
    s2.tambah_nilai(65)
    print(s2)
    print("Rata-rata nilai:", s2.rata_nilai())
    print("Status:", s2.status())
