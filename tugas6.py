import numpy as np
import pandas as pd

np.random.seed(42)


def rata_rata(angka: list) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return round(self.df["nilai"].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = (self.df["nilai"] >= threshold).sum()
        return round((lulus / len(self.df)) * 100, 2)

    def save_summary(self, path: str):
        lulus = (self.df["nilai"] >= 70).sum()
        tidak_lulus = len(self.df) - lulus
        with open(path, "a") as f:
            f.write("\n=== OOP GRADEBOOK SUMMARY ===\n")
            f.write(f"Jumlah data    : {len(self.df)}\n")
            f.write(f"Rata-rata nilai: {self.average()}\n")
            f.write(f"Pass rate      : {self.pass_rate()}%\n")
            f.write(f"Jumlah lulus   : {lulus}\n")
            f.write(f"Tidak lulus    : {tidak_lulus}\n")

    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average()})"


if __name__ == "__main__":
    print("=" * 45)
    print("=== NUMPY ===")
    print("=" * 45)

    nilai_array = np.array([88, 76, 55, 92, 67, 80, 45, 73, 95, 61])
    print("Data nilai:", nilai_array)
    print("Rata-rata :", round(np.mean(nilai_array), 2))
    print("Median    :", np.median(nilai_array))
    print("Std Dev   :", round(np.std(nilai_array), 2))
    print("Min       :", np.min(nilai_array))
    print("Max       :", np.max(nilai_array))

    print("\n" + "=" * 45)
    print("=== PANDAS ===")
    print("=" * 45)

    data = {
        "nama": [
            "Ida Bagus Made Andika",
            "Budi Santoso",
            "Sari Dewi",
            "Raka Pratama",
            "Lestari Putri"
        ],
        "nim": [
            "2308561121",
            "2308561200",
            "2308561201",
            "2308561202",
            "2308561203"
        ],
        "nilai": [88, 55, 76, 92, 67]
    }

    df = pd.DataFrame(data)
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")
    print(df.head())

    print("\n" + "=" * 45)
    print("=== OOP: GRADEBOOK ===")
    print("=" * 45)

    gb = GradeBook(df)
    print(gb)
    print("Rata-rata nilai :", gb.average())
    print("Pass rate       :", gb.pass_rate(), "%")
    gb.save_summary("ringkasan_tugas6.txt")
    print("Ringkasan tersimpan di ringkasan_tugas6.txt")

    lulus = (df["nilai"] >= 70).sum()
    tidak_lulus = len(df) - lulus
    with open("ringkasan_tugas6.txt", "w") as f:
        f.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        f.write(f"Rata-rata : {round(np.mean(nilai_array), 2)}\n")
        f.write(f"Median    : {np.median(nilai_array)}\n")
        f.write(f"Std Dev   : {round(np.std(nilai_array), 2)}\n")
        f.write(f"Min       : {int(np.min(nilai_array))}\n")
        f.write(f"Max       : {int(np.max(nilai_array))}\n")
        f.write("\n=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah baris  : {len(df)}\n")
        f.write(f"Jumlah lulus  : {lulus}\n")
        f.write(f"Tidak lulus   : {tidak_lulus}\n")

    gb.save_summary("ringkasan_tugas6.txt")
    print("Ringkasan lengkap tersimpan di ringkasan_tugas6.txt")
