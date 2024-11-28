from src import functions as fn
'''F02: 
PROGRAM Login
{ Spesifikasi : Agent dan Admin bisa melakukan login ke dalam sistem. 
Terdapat 3 jenis kesalahan yang mungkin terjadi ketika memanggil command ini: 
1. Username tidak terdaftar
2. Password salah
3. Pemanggilan command "help" ketika sudah logged in.}
'''

def login(df_user : list) -> list :
    print("===> SILAHKAN LOGIN <====")
    while True:
        username = input(fn.clr("Username : ",'cyan',''))
        password = input(fn.clr("Password : ",'cyan',''))
        notLogin = ""
        suksesLogin = False
        if str.lower(username) == 'keluar' or str.lower(password) == 'keluar':
            break
        while True:
            i = 0
            valid = False
            for i in range(len(df_user)) :
                if df_user[i][1] == username :
                    valid = True
                    indexBaris = i
                    if df_user[i][3] == "admin":
                        notLogin = "admin"
                        break
                    else:
                        notLogin = "agent"
                        break
            break
                    
        if not valid :
            print("Username tidak terdaftar! Silakan register terlebih dahulu atau gunakan username yang sudah ada.\n")
            continue
        else :
            while password != df_user[indexBaris][2] :
                print("Password salah! Harap login kembali dengan username dan password yang benar!\n")
                continue
            else :
                print('\n<'+66 *'=' + '>')
                print(f"Selamat datang, A{notLogin[1:]} {username}! Ayo kita kalahkan Dr. Asep Spakbor!!! ")
                print("Masukkan command “HELP” untuk daftar command yang dapat kamu panggil.\n") # nanti dihubungin ke F04-Help di main
                suksesLogin = True
                break
    if suksesLogin:
        return (indexBaris+1), notLogin
    else: 
        user_id = False
        return user_id,notLogin
