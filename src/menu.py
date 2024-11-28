
from src import functions
def help (status_login: str)-> str:

    if status_login == "admin":
        # masih belum terdefinisi karena perlu diubah di login
        helpMenu = functions.clr('=========== HELP ===========','yellow','')+str(

"""

Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:

1. Logout: Keluar dari akun yang sedang digunakan
2. Shop Management: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent
3. Monster Management: Melakukan manajemen pada data & statistik monster
4. Save: Melakukan aksi penyimpanan data untuk digunakan di kemudian hari
5. Exit Game

Footnote: 
1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
2. Jangan lupa untuk memasukkan input yang valid!
"""            
        )

    elif status_login == "agent":
        helpMenu = functions.clr('=========== HELP ===========','yellow','')+str(
"""

Halo Agent! Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:

1. Logout: Keluar dari akun yang sedang digunakan
2. Inventory: Melihat owca-dex yang dimiliki oleh Agent
3. Battle: Melakukan pertarungan dengan monster untuk mendapatkan OC
4. Arena: Melakukan set berbagai battle secara berturut-turut
5. Shop: Toko dimana berbagai monster dan potion bisa dibeli menggunakan OC 
6. Laboratory: Melakukan upgrade/level up terhadap monster dengan OC
7. Save: Melakukan aksi penyimpanan data untuk digunakan di kemudian hari
8. Exit Game

Footnote: 
1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
2. Jangan lupa untuk memasukkan input yang valid!
"""
        )
    else:
        helpMenu = functions.clr('=========== HELP ===========','yellow','')+ str(
"""

Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.

1. Login: Masuk ke dalam akun yang sudah terdaftar
2. Register: Membuat akun baru

Footnote: 
1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
2. Jangan lupa untuk memasukkan input yang valid

"""
        )

    return helpMenu
