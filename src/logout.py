'''F03: 
PROGRAM Logout
{ Spesifikasi : Pengguna yang sudah login bisa menggunakan fungsi ini untuk keluar dari akun.}'''

def logout(statusLogin : str) -> str :
    if statusLogin != "" :
        print("Dadah, anda sudah logout dari akun")
        statusLogin = ""
    else :
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return statusLogin