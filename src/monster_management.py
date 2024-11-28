from src import functions as fn

'''F13: Monster Management
{ Spesifikasi : Menu dimana admin dapat menambahkan monster baru}

Keluaran:
monster_db
monsterShop_db '''

# @Validasi belum
def inputDanCekMons(monster_db, monsterShop_db):
    brk = False # Inisialisasi Kondisi Terminasi
    while True: # @placeholder
        name = input('>>> Masukkan Type / Nama Monster: ')
        found = fn.cekUdahAda(name, monster_db, 1)
        if found:
            print('Nama sudah terdaftar, coba lagi!','\n')
        else:
            break

    while True:
        atkPower = input(fn.clr('>>> Masukkan ATK Power: ','cyan',''))
        if fn.isInteger(atkPower):
            if int(atkPower) >= 0:
                break
            else:
                print('ATK Power Power harus bernilai positif, coba lagi!','\n')
        else:
            print('Masukkan input bertipe Integer, Coba lagi!','\n')

    while True:
        defense = input(fn.clr('>>> Masukkan DEF Power: ','cyan',''))
        if fn.isInteger(defense):
            if int(defense) <= 50 and int(defense) >= 0:
                break
            else: # Diluar range
                print('DEF Power harus bernilai 0-50, coba lagi!','\n')
        else:   
            print('Masukkan input bertipe Integer, Coba lagi!','\n')

    while True:
        hp = input(fn.clr('>>> Masukkan HP: ','cyan',''))
        if fn.isInteger(hp):
            if int(hp) > 0:
                break
            else:
                print('HP harus lebih besar dari 0, coba lagi!','\n')
        else:
            print('Masukkan harus Integer, Coba lagi!','\n')

    # mencari id terbesar di list
    for line in monster_db:
        idLast = line[0]
    monster_db.append([str(int(idLast)+1),name,atkPower,defense,hp])
    monsterShop_db.append([str(int(idLast)+1),0,0])

    monsMenu = True
    return monsMenu,monster_db, monsterShop_db 


def monsterManagement(monster_db, monsterShop_db):
    # INIT
    monsMenu = True
    tipe = 'monster'
    # HEADER
    print('='*26 + ' OWCA-DEX ' + '='*26,'\n')
    print('	ʕ •̀ ω •́ ʔ SELAMAT DATANG DI OWCA-DEX!!!')

    while monsMenu: 
        monsMenu = False
        print('─'*55)
        print('Menu')
        print('> Lihat')
        print('> Tambah')
        print('> Keluar')

        while True:
            print('─'*55)
            mon_aksi = input(fn.clr('>>> Pilih Aksi: ','cyan',''))
            if mon_aksi == '1' or mon_aksi == '2' or mon_aksi == '3':
                break
            else:
                print('Pilih aksi yang valid!!')

        if mon_aksi == '1':
            print('─'*55)
            fn.printData(fn.appendHeader(monster_db,'monster'))
            print()
            monsMenu = True
            
        elif mon_aksi == '2':  
            print('─'*55)
            print('Memulai pembuatan Monster baru')
            monsMenu,monster_db,monsterShop_db = inputDanCekMons(monster_db,monsterShop_db )
        
        else: # mon_aksi 3
            print()
            print('	ヾ(•ω•`)o Selamat Tinggal!!! ')
            print()
    
    return monster_db, monsterShop_db
