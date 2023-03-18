# Post-Test-3-ASD

Cara Kerja Program:
=========================================================================================================================================================
Program ini menggunakan kelas Node dan ToDoList untuk membuat struktur data linked list.
Ketika program dijalankan, daftar tugas diinisialisasi sebagai linked list kosong.
Pengguna dapat menambahkan tugas baru ke daftar menggunakan metode add_task dengan membuat node baru dan menambahkannya ke akhir linked list.
Pengguna juga dapat menghapus tugas dari daftar menggunakan metode delete_task, yaitu dengan mencari node yang memiliki data tugas yang ingin dihapus, dan menghapusnya dari linked list.
Pengguna dapat menandai tugas sebagai selesai menggunakan metode mark_as_done, yaitu dengan mencari node yang memiliki data tugas yang ingin ditandai, dan mengubah datanya menjadi "DONE: tugas".
Ketika pengguna ingin melihat daftar tugas, program mencetak data dari setiap node di linked list menggunakan metode print_tasks.



Fungsionalitas Program:
=========================================================================================================================================================
Program ini berfungsi untuk manajemen daftar tugas menggunakan struktur data linked list. Fungsionalitas yang tersedia meliputi menambahkan tugas baru, menghapus tugas, menandai tugas sebagai selesai, dan mencetak daftar tugas.



Bagaimana Aplikasi Bekerja:
=========================================================================================================================================================
Program ini menggunakan konsep linked list untuk menyimpan daftar tugas. Setiap tugas disimpan dalam sebuah node yang memiliki pointer ke node berikutnya. Ketika pengguna menambahkan tugas baru, node baru dibuat dan ditambahkan ke akhir linked list. Ketika pengguna menghapus tugas atau menandai tugas sebagai selesai, program mencari node yang sesuai dan melakukan operasi yang diinginkan. Ketika pengguna ingin melihat daftar tugas, program mencetak data dari setiap node di linked list.



Output Program:
=========================================================================================================================================================
Output program akan mencetak daftar tugas awal, kemudian mencetak daftar tugas setelah dilakukan perubahan. Berikut adalah contoh output program:

Daftar tugas awal:

Membuat laporan keuangan

Beli bahan makanan

Ambil paket di kantor pos

Kirim email ke klien

Daftar tugas setelah dihapus dan ditandai selesai:

Membuat laporan keuangan

Ambil paket di kantor pos

DONE: Kirim email ke klien



Elemen Penting yang Digunakan dalam Program:
=========================================================================================================================================================
1. Konsep linked list digunakan untuk menyimpan dan mengatur daftar tugas.

2. Kelas Node digunakan untuk membuat node baru.

3. Kelas ToDoList digunakan untuk mengatur operasi yang dapat dilakukan pada linked list, seperti menambahkan, menghapus, menandai, dan mencetak tugas.

4. Metode add_task, delete_task, mark_as_done, dan print_tasks digunakan untuk menambahkan, menghapus, menandai, dan mencetak tugas pada linked list.

5. Penggunaan conditional statements seperti if dan while digunakan untuk mencari node yang sesuai dan melakukan operasi yang diinginkan.
