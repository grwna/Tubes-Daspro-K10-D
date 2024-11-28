from src import randomNumberGenerator,functions

def potion (monsterAgent:list,inventory_user:list,id_potion:str, HPAgent:str) -> tuple:

    monster = monsterAgent[1] # Mengambil nama monster
    b = [0,0,0]
    for i in range (len(inventory_user)):
        if inventory_user[i][1] == "strength":
            b[0] = int(inventory_user[i][2])
        elif inventory_user[i][1] == "resilience":
            b[1] = int(inventory_user[i][2])
        else:
            b[2] = int(inventory_user[i][2])
    if b == [0,0,0]: # Tidak ada potion karena array tidak terisi
        print( "Anda tidak memiliki Potion dalam inventory!\n")
        return (monsterAgent, inventory_user, id_potion, HPAgent)
    else:
        
        while True: # Selama input belum valid/tidak ada potion
            print (f"""
============ POTION LIST ============
1. Strength Potion (Qty: {b[0]}) - Increases ATK Power
2. Resilience Potion (Qty: {b[1]}) - Increases DEF Power
3. Healing Potion (Qty: {b[2]}) - Restores Health
4. Cancel""")
            a = input()
            if a == "4":
                return (monsterAgent, inventory_user, id_potion, HPAgent)
            elif a == "1" or a == "2" or a == "3":
                if b[int(a)-1] == 0: # Selama tidak ada potion, harus mengulang
                    print ("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!\n")
                else:
                    break
            else:
                print ("Input tidak valid! Ulangi.\n")
                
        if int(a)-1 == 0:
            if id_potion[0] == True: # Potion str belum dikonsumsi
                print (f"Setelah mengkonsumsi potion ini, tiba-tiba keluar sinar cahaya dari {monster} seakan-akan monster terlahir baru kembali.\n ATK POWER + 5%\n")
                for i in range (len(inventory_user)):
                    if inventory_user[i][1] == "strength":
                        inventory_user[i][2] = str(b[0] - 1) # Mengurangi jumlah potion
                monsterAgent[2] = str(round(int(monsterAgent[2])*21/20)) # Peningkatan 5% dari stats
                id_potion[0] = False # Tanda sudah dikonsumsi
            else:
                print (f"{monster} menolak ramuan ini mentah-mentah, seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
        elif int(a)-1 == 1:
            if id_potion[1] == True: # Potion resilience belum dikonsumsi
                print (f"Sebuah gelembung tameng tiba-tiba muncul melingkupi {monster} yang membuatnya semakin tangguh dan sulit dilukai. \n DEF POWER + 5%\n")
                for i in range (len(inventory_user)):
                    if inventory_user[i][1] == "resilience":
                        inventory_user[i][2] = str(b[1] - 1)
                monsterAgent[3] = str(round(int(monsterAgent[3])*21/20))
                id_potion[1] = False
            else:
                print (f"{monster} menolak ramuan ini mentah-mentah, seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
        elif int(a)-1 == 2:
            if id_potion[2] == True: # Potion HP belum dikonsumsi pada battle
                print (f"Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {monster} sembuh dengan cepat. Dalam sekejap, {monster} terlihat kembali prima dan siap melanjutkan pertempuran. \n HP + 25%\n")
                for i in range (len(inventory_user)):
                    if inventory_user[i][1] == "healing":
                        inventory_user[i][2] = str(b[2] - 1)
                HPAgent = HPAgent*5/4 # 25% recovery
                if HPAgent > int(monsterAgent[4]): # Batasan max health
                    HPAgent = int(monsterAgent[4])
                id_potion[2] = False
            else:
                print (f"{monster} menolak ramuan ini mentah-mentah, seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.\n")
        return monsterAgent, inventory_user, id_potion, HPAgent  # Return 2 variabel yaitu stat monster dan array konfirmasi


def hitungDamage(atkPower:str, defPower:str) -> int:
    # Mengubah variabel menjadi integer
    atkPower = int(atkPower)
    defPower = int(defPower)

    # Menghitung rentang serangan
    minAtk = atkPower - (atkPower * 0.3)
    maxAtk = atkPower + (atkPower * 0.3)

    # Menggunakan rng untuk mendapat attack power secara random
    seed = randomNumberGenerator.formula(a=4871, c=0, m=2**31-1, seed=None)
    attack = randomNumberGenerator.randomNumberGenerator(seed, numRange=[minAtk, maxAtk])

    # Menghitung damage dengan adanya value defense power
    damage = round(attack * ((100 - defPower) / 100))
    return damage

def hitungAtribut(baseAtk:str, baseDef:str, baseHP:str, level:str) -> tuple:
    # Mengubah variabel menjadi integer
    baseAtk = int(baseAtk)
    baseDef = int(baseDef)
    baseHP = int(baseHP)
    # Fungsi untuk menghitung atribut monster berdasarkan level
    multipilier = 1 + ((int(level) - 1) * 0.1)
    return baseAtk * multipilier, baseDef * multipilier, baseHP * multipilier

# Fungsi untuk mengonversi kolom HP menjadi integer
def konversi_hp_ke_integer(monster_db:list)-> list:
    for i in range(1, len(monster_db)):  # Mulai dari 1 untuk menghindari header
        # Konversi HP dari string ke integer
        monster_db[i][4] = int(monster_db[i][4])
    return monster_db

def seleksimonster (monster_user:list,monster_db:list)->tuple:
    # Mencetak pilihan monster ke agent
    print(f"""<=== CHOOSE YOUR MONSTER ===>""")
    num = 0
    for row in monster_user:
        for mow in monster_db:
            if row[1] == mow[0]:
                print(f"{num+1}. {(mow)[1]} " + " "*(14-len((mow)[1])) + f"| Level : {row[2]}")
                num += 1
    print()
    while True:
        chooseMonster = input(functions.clr("Pilih monster anda : ",'cyan',''))
        if not functions.isInteger(chooseMonster):
            print('Masukan berupa integer!\n')
            continue           
    
    # Inisialisasi variabel untuk memulai battle dan mengecek apakah battle bisa dimulai
        jumlahMonster = functions.hitungJumlahBaris(monster_user)
        if 1 <= int(chooseMonster) <= jumlahMonster :
            ids = monster_user[int(chooseMonster)-1][1]
            monsterAgent = monster_db[int(ids)-1]
            level = (monster_user[int(chooseMonster)-1][2])
            break
        else :
            print("Pilihan monster tidak tersedia! Silahkan pilih kembali!\n")
    return monsterAgent, level

def startBattle(monster_db, inventory_user, monsterAgent, levelMusuh, levelAgent) -> int:
    # Inisialisasi seed untuk RNG dalam pemilihan monster lawan
    seed = randomNumberGenerator.formula(a=4871, c=0, m=2**31-1, seed=None)

    # Menghitung jumlah monster dalam database
    jumlahMonster = len(monster_db)
    
    # Gacha monster lawan berdasarkan indeks
    indeksMusuh = randomNumberGenerator.randomNumberGenerator(seed, numRange=[0, jumlahMonster])

    # Mengambil monster dengan mencocokkan indeks
    monsterMusuh = None
    i = 0
    for monster in monster_db :
        if i == indeksMusuh :
            monsterMusuh = monster
            break
        i += 1
    HPAgent = int(monsterAgent[4])
    HPMusuh = int(monsterMusuh[4])
    atkPower, defPower, HPAgent = hitungAtribut(monsterAgent[2], monsterAgent[3], HPAgent, levelAgent)

    atkMusuh, defMusuh, HPMusuh = hitungAtribut(monsterMusuh[2], monsterMusuh[3], HPMusuh, levelMusuh)
    
    # Mencetak hasil gacha monster lawan sebagai pesan awal masuknya battle stage  
    print(f"""
OMAGAAA monster {monsterMusuh[1]} muncul !!!

<===Battle Start===>
Name : {monsterMusuh[1]}
ATK Power : {atkMusuh}
DEF Power : {defMusuh}
HP : {HPMusuh}
Level : {levelMusuh}
""")
    mulaiBattle = True
    # Inisialisasi HP dari monster agent dan monster musuh sebagai tolak ukur dalam memulai battle
   
    # Memulai Battle
    turn = 1
    id_potion = [True, True, True]  # Inisialisasi di luar loop
    # Inisialisasi variabel damage yang diterima dan diberikan oleh agent
    totalDamageDiberikan = 0
    totalDamageDiterima = 0
    while mulaiBattle :
        print(f"<====Turn {turn} ({monsterAgent[1]})====>\n"
              "1. Attack\n"
              "2. Potion\n"
              "3. Quit")
        action = input(functions.clr("Pilih perintah : ",'cyan',''))
        if not functions.isInteger(action):
            print("Input tidak valid, silahkan coba lagi\n")
            continue

        if action == '2':
            monsterAgent, inventory_user, id_potion, HPAgent = potion(monsterAgent, inventory_user, id_potion, HPAgent)
        elif action == '3':
            print("Anda berhasil kabur dari pertarungan\n")
            break
        elif action == '1':
            # Menghitung terlebih dahulu atribut monster berdasarkan levelnya
            atkPower, defPower, _ = hitungAtribut(monsterAgent[2], monsterAgent[3], HPAgent, levelAgent)

            atkMusuh, defMusuh, _ = hitungAtribut(monsterMusuh[2], monsterMusuh[3], HPMusuh, levelMusuh)
            # Menghitung damage yang diberikan musuh
            damageMusuh = hitungDamage(atkMusuh, defMusuh)
            # Menghitung damage
            damage = hitungDamage(atkPower, defPower)

            # Memberi damage ke musuh
            HPMusuh -= damage
            totalDamageDiberikan += damage
            print(f"BOOM {monsterAgent[1]} menyerang {monsterMusuh[1]} dengan damage "+ functions.clr(f'{damage}','red',''))

            # Cek Apakah musuh masih hidup
            if HPMusuh <= 0 :
                print(f"VERY NIICE {monsterMusuh[1]} berhasil dikalahkan !!!")
                mulaiBattle = False
                break
            else :
                print(f"Sisa HP musuh {monsterMusuh[1]} sebesar " + functions.clr(f'{HPMusuh}\n','green',''))

        # Giliran Musuh menyerang
            print(f"RAWRRR Giliran {monsterMusuh[1]} menyerang!!!")
            
            HPAgent -= damageMusuh
            totalDamageDiterima += damageMusuh
            print(f"{monsterMusuh[1]} menyerang {monsterAgent[1]} dengan damage " + functions.clr(f'{damageMusuh}','red',''))
        
            # Cek apakah monster agent masih hidup
            if HPAgent <= 0 :
                mulaiBattle = False
            else :
                print(f"Sisa HP dari {monsterAgent[1]} sebesar " + functions.clr(f"{HPAgent}\n",'green',''))
            turn += 1

    if HPMusuh <= 0:
        win_stat = "menang"
    elif HPAgent <= 0:
        win_stat = "kalah"
    else:
        win_stat = "kabur"
    return totalDamageDiberikan, totalDamageDiterima, inventory_user, win_stat

def battle (owca_coin:str, monster_user:list, monster_db:list, inventory_user:list)->tuple:
    seed = randomNumberGenerator.formula(a=4871, c=0, m=2**31-1, seed=None)
    levelMusuh = randomNumberGenerator.randomNumberGenerator(seed, numRange=[1, 5])
    monsterAgent, levelAgent = seleksimonster(monster_user,monster_db)
    _,_, inventory_user, win_stat = startBattle(monster_db, inventory_user, monsterAgent, levelMusuh, levelAgent)
    if win_stat == "menang":
        coinDidapat = randomNumberGenerator.randomNumberGenerator(seed, numRange=[20,100])
        owca_coin = str(int(owca_coin)+ coinDidapat)
        print(f"Anda mendapatakan " +functions.clr(f'{coinDidapat} OC\n','yellow',''))
        print('\nKeluar dari battle...\n')
    elif win_stat == "kalah":
        print(f"hiks hiks {monsterAgent[1]} telah dikalahkan, jangan putus asa tetap semangat!\n")
        print('\nKeluar dari battle...\n')
    else:
        print ("Exiting battle...\n")
    return owca_coin, inventory_user