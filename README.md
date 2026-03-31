# tugas_python_ai_b10

Repository ini berisi kumpulan tugas Python dalam rangka program AI Development B10.

---

## Tugas 4 - Python Data Structures

Tugas ini membahas struktur data dasar Python secara menyeluruh.

List digunakan untuk menyimpan koleksi data yang bisa diubah. Beberapa operasi yang dipraktikkan meliputi append, insert, extend, pop, dan remove. Selain itu, slicing dengan parameter start, stop, dan step memudahkan pengambilan subset data tanpa loop eksplisit.

Tuple bersifat immutable sehingga cocok untuk data yang tidak boleh berubah. Fitur unpacking memungkinkan pembongkaran nilai tuple ke beberapa variabel sekaligus, termasuk penggunaan *rest untuk menampung sisa elemen.

Set secara otomatis menghapus duplikat, menjadikannya struktur yang tepat untuk operasi himpunan. Union, intersection, difference, dan symmetric difference diimplementasikan menggunakan operator bawaan Python.

Dictionary menyimpan data dalam pasangan key-value, cocok untuk merepresentasikan objek terstruktur seperti data mahasiswa. Operasi tambah, ubah, dan hapus key dapat dilakukan secara langsung.

Nested structure menggabungkan list dan dictionary untuk merepresentasikan kumpulan data yang lebih kompleks. List comprehension digunakan untuk memfilter data berdasarkan kondisi tertentu secara ringkas.

Comprehension, baik list, dict, maupun set comprehension, terbukti efektif menggantikan loop konvensional untuk transformasi dan filter data sederhana.

---

## Tugas 5 - Python Function and Class

Tugas ini berfokus pada penulisan fungsi yang reusable dan pembuatan class sebagai representasi objek.

Fungsi greet, tambah, dan rata_rata dirancang dengan parameter default dan type hint agar lebih mudah dipahami dan digunakan kembali. Penanganan edge case seperti list kosong pada rata_rata mencegah error saat runtime.

Class Student mengencapsulasi data mahasiswa beserta logika perhitungan nilai. Method rata_nilai memanfaatkan fungsi rata_rata yang sudah didefinisikan sebelumnya, menunjukkan prinsip reuse antar komponen. Method status mengembalikan hasil kelulusan berdasarkan threshold yang bisa dikonfigurasi, dan __str__ memudahkan representasi objek saat di-print.

Penggunaan if __name__ == "__main__" memisahkan logika demo dari definisi fungsi dan class, sehingga file bisa diimpor oleh modul lain tanpa efek samping.

---

## Tugas 6 - Python Modules, File I/O, and OOP

Tugas ini mengintegrasikan library eksternal NumPy dan pandas dengan konsep OOP dan file I/O.

NumPy digunakan untuk komputasi statistik deskriptif pada data nilai ujian. Fungsi mean, median, std, min, dan max memberikan gambaran distribusi data secara cepat dibanding perhitungan manual.

pandas DataFrame mempermudah pengelolaan data tabular dengan kolom nama, nim, dan nilai. Penambahan kolom status dilakukan menggunakan apply dengan lambda, pendekatan yang lebih efisien dibanding iterasi baris per baris.

File I/O diimplementasikan untuk menyimpan ringkasan statistik ke file teks. Hasil dari analisis NumPy dan DataFrame ditulis secara terstruktur agar mudah dibaca.

Class GradeBook mengwrap DataFrame dan menyediakan method average, pass_rate, dan save_summary. Desain ini mengikuti prinsip enkapsulasi, di mana data dan operasi yang relevan disatukan dalam satu unit.
