from src import functions as fn
'''F01: 
PROGRAM REGISTER
{ Spesifikasi : Mendaftarkan pengguna baru dengan masukan username dan password.
Pengguna yang mendaftar otomatis memiliki role “agent”. 
Pastikan username unik, tidak dapat membuat user dengan role "admin".
Username hanya dapat mengandung alfabet A-Z, a-z, underscore, strip, dan angka 0-9.
Jika belum ada akun yang terdaftar dengan username yang diberikan, maka pengguna akan diharuskan memilih satu monster.}
'''

def cekusername(username:str) -> bool:
    stat=True
    validChars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-" 
    if len(username) == 0 :
        stat = False
        return stat
    for i in username:
        if i not in validChars :
            stat=False
            return stat
    return stat

def cekusernameall(username:str, df_user:list) -> bool:
    stat=True
    stat=cekusername(username)
    for i in df_user:
        if i[1]==username :
            stat=False
    return stat

def cekPassword(password:str) -> bool :
    stat = True
    if len(password) == 0:
        stat = False
    for char in password:
        if char == ';':
            stat = False
    return stat

def register(df_user:list,df_monster:list, df_monster_inventory:list) -> tuple : 
    # Mulai meminta input username akun untuk di register
    belumRegister = True
    while belumRegister :
        username=input("Masukan username: ")
        if cekusernameall(username, df_user) and cekusername(username):
            print(f"Username {username} telah berhasil register.\n")
            belumRegister = False
        elif not(cekusername(username)):
            print(f"Username {username} salah, silakan menggunakan username lain.\n")        
        else:
            print(f"Username {username} sudah terpakai, silakan menggunakan username lain.\n")

    # Mulai meminta input password akun 
    passBelumValid = True
    while passBelumValid :
        password=input("Masukan password: ")
        if cekPassword(password) :
            print(f"Password Valid.\n")
            passBelumValid = False
        else :
            print("Password tidak boleh kosong atau memakai ';' , silahkan input kembali.\n")

    # Mulai memilih monster
    print("""Silahkan pilih salah satu monster sebagai monster awalmu :)""")
    idx = 0
    for monster in df_monster :
        print(f"{monster[0]}. {monster[1]}")
        idx +=1
        if idx == 5:
            break

    indeksPilihanMonster = [str(i+1) for i in range(len(df_monster))]
    while True :
        monsterPilihan = input("\n>>> CHOOSE YOUR MONSTER: ")
        if fn.isInteger(monsterPilihan):
            if monsterPilihan not in indeksPilihanMonster :
                print('Input tidak valid!')
            else :
                monsterPilihan = int(monsterPilihan)
                break
        else:
            print("Input tidak valid :(")
    print('\n<'+66 *'=' + '>')
    print(f"Selamat datang Agent {username}!. Mari kita mengalahkan Dr. Asep Spakbor dengan {df_monster[monsterPilihan-1][1]}!")
    print("Masukkan command “HELP” untuk daftar command yang dapat kamu panggil.\n") # nanti dihubungin ke F04-Help di main
    idUserBaru = str(int(df_user[len(df_user)-1][0]) + 1)    
    databaseMonsterUser = [idUserBaru, str(monsterPilihan), str(1)]
    df_monster_inventory.append(databaseMonsterUser)                #Memasukkan data monster pilihan kedalam data monster_inventory
    df_user.append([idUserBaru, username, password, str("agent"), str(0)])
    idUserBaru = int(idUserBaru)
    # Variabel yang direturn merupakan variabel-variabel yang ada pada user.csv
    return idUserBaru, df_user, df_monster_inventory, "agent"


