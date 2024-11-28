from src import functions as fn, shop

'''F12: Shop Management
{ Spesifikasi : Sebuah menu shop dimana Admin dapat melihat atau memanipulasi 
stok dan harga unit-unit yang ada di shop}

Note: monster.csv dan monster_shop.csv akan selalu memuat monster yang sama, menghapus monster dari shop berarti mengubah stok menjadi 0 saja.

Keluaran: 
monsterShop_db -> monster_shop.csv (mengubah stok dan harga)
itemShop_db -> item_shop.csv (mengubah stok dan harga)
'''

# @ -> tanda pengingat

# Kamus
# aksi_shopmng ---> Pilihan aksi utama
# monster_potion ---> Pilihan aksi hasil return fungsi

def database(monster_db:list,monsterDalamShop:list,itemDalamShop:list,itemShop_db:list,tipeList:list)-> tuple:
    # Menampilkan list database yang tidak termasuk dalam shop, sekaligus 
    listBaru = []
    indexDalamShop = []
    indexDatabase = []
    if tipeList == 'monster':
        listShop = monsterDalamShop
        listDatabase = monster_db
        checker = 'id'
    elif tipeList == 'item':
        listShop = itemDalamShop
        listDatabase = itemShop_db
        checker = 'type'
    
    for line in listShop:
        if line[0] != checker: # pakai ini karena list database memakai header
            indexDalamShop.append(line[0]) # index - index yang ada dalam list shop
    for line in listDatabase:
        if line[0] not in indexDalamShop:
            if tipeList == 'monster':
                listBaru.append(line)
            elif tipeList == 'item':
                listBaru.append([line[0]]) # List potion hanya menampilkan tipe/nama
    indexDatabase = fn.indexDalamList(listBaru)
    if listBaru:
        fn.printData(fn.appendHeader(listBaru,tipeList))
    else:
        print('Semua unit sudah ada di shop!')
    return indexDalamShop,indexDatabase

def menuPertama(lihat_valid: list, aksi_shopmng: str) -> str:
    while True:
        print('=> AKSI <=\n'
                '> Monster\n'
                '> Item\n'
                '> Batal')
        print('─'*55)
        monster_potion = str.lower(input(fn.clr('>>> Mau ' + aksi_shopmng +' apa?: ','cyan','')))
        # Validasi Input
        if monster_potion in lihat_valid:
            break
        else:
            print('Pilih opsi yang valid!\n')
    return monster_potion

def fnTambah(monster_db, monsterDalamShop: list, monsterShop_db: list,itemDalamShop: list, itemShop_db, shopMenu: bool, tipeList: str) -> bool:
    # Mengambil data dari database KESELURUHAN
    indexDalamShop, indexDatabase = database(monster_db,monsterDalamShop,itemDalamShop,itemShop_db,tipeList)
    # @Belum validasi
    if len(indexDatabase) > 0:
        print('\n> Ketik "BATAL" untuk keluar\n') 
        while True:
            id = input(fn.clr(f'>>> Masukkan id {tipeList}: ','cyan',''))
            if id == 'batal':
                shopMenu = True
                break
            if not fn.isInteger(id):
                print('Masukan berupa integer!')
                continue
            
            if tipeList == 'monster': tipe = 'Monster'
            elif tipeList == 'item': 
                tipe = 'Item'
                id = fn.convertItemNames(id,'id')

            if id not in indexDatabase:
                if id in indexDalamShop:
                    print(f'{tipe} sudah ada di shop!','\n')
                else: # Id Monster tidak ada di database
                    print(f'{tipe} tidak ada di database!','\n')
                continue
            else:
                break

        while True:
            if shopMenu: break
            stok = input(fn.clr('>>> Masukkan stok awal: ','cyan',''))
            if fn.isInteger(stok):
                if int(stok) <= 0:
                    print('Stok harus lebih dari 0','\n')
                    continue
                else: break
            else:
                print('Masukan berupa integer!','\n')
                continue

        while True:
            if shopMenu: break
            harga = input(fn.clr('>>> Masukkan harga: ','cyan',''))
            if fn.isInteger(harga):
                if int(harga) < 0:
                    print('Harga tidak boleh negatif! ','\n')
                    continue
                else: break
            else:
                print('Masukan berupa integer!','\n')
                continue
        
        if tipeList == 'monster':
            listDatabase = monster_db
            listUnitShop = monsterShop_db
            indexKolom = 1 # indexKolom Nama
        elif tipeList == 'item':
            listDatabase = itemShop_db
            listUnitShop = itemShop_db
            indexKolom = 0
        if not shopMenu:
            for line in listDatabase:
                if line[0] == id:
                    namaUnit = line[indexKolom]
            for line in listUnitShop:
                if line[0] == id:
                    line[1] = stok
                    line[2] = harga
            namaUnit = fn.convertItemNames(namaUnit,'name')
            print()
            print(f'{tipe} telah berhasil ditambahkan!')
            print(f'Nama : {namaUnit}')
            print(f'Stok : {stok}')
            print(f'Harga : {harga}')
            # @manipulasi list of monster shop
    shopMenu = True # Kembali ke shop menu
    return shopMenu,monsterShop_db,itemShop_db

def fnUbah(monsterShop_db: list,itemShop_db: list,monster_db: list, monsterDalamShop: list, itemDalamShop: list, shopMenu: bool,tipeList: str) -> bool:
    # Mengambil data dari database SHOP
    if tipeList == 'monster':
        fn.printData(fn.appendHeader(monsterDalamShop,tipeList))
        listUnitShop = monsterDalamShop
        indexList = fn.indexDalamList(monsterDalamShop)

    elif tipeList == 'item':
        fn.printData(fn.appendHeader(itemDalamShop,tipeList))
        listDatabase = itemDalamShop
        listUnitShop = itemDalamShop
        indexList = ['1','2','3']

    print() 
    while True:
        id = input(fn.clr(f'>>> Masukkan id {tipeList}: ','cyan',''))
        if id in indexList:
            break
        else:
            if fn.isInteger(id):
                if tipeList == 'monster':
                    if int(id) > fn.hitungJumlahBaris(monster_db):
                        print('Monster tidak ada dalam database!\n')
                    else:
                        print('Monster tidak ada dalam shop\n')
                elif tipeList == 'item':
                    if int(id) > 3:
                        print('Item tidak ada dalam database!\n')
                    else:
                        print('Item tidak ada dalam shop\n')
            else:
                print('Masukan berupa integer!\n')
            
          
    while True:
        stok = input(fn.clr('>>> Masukkan stok baru: ','cyan',''))
        if not fn.isInteger(stok):
            print('Masukan berupa integer!\n')
        else: break
    while True:
        harga = input(fn.clr('>>> Masukkan harga baru: ','cyan',''))
        if not fn.isInteger(harga):
            print('Masukan berupa integer!\n')
        else: break
    if tipeList == 'monster':
        tipe = 'Monster'
        listDatabase = monster_db
        listUnitShop = monsterShop_db
        indexKolom = 1 # indexKolom Nama
    elif tipeList == 'item':
        tipe = 'Item'
        listDatabase = itemShop_db
        listUnitShop = itemShop_db
        indexKolom = 0
        id = fn.convertItemNames(id,'id')
    if not shopMenu:
        for line in listDatabase:
            if line[0] == id:
                namaUnit = line[indexKolom]
        for line in listUnitShop:
            if line[0] == id:
                line[1] = stok
                line[2] = harga
        namaUnit = fn.convertItemNames(namaUnit,'name')

        print()
        if stok == '' and harga == '':
            print(f'{tipe} tidak jadi diubah')
        else:
            print(f'{tipe} telah berhasil diubah!')
            print(f'Nama : {namaUnit}')
            if stok != '':
                print(f'Stok baru : {stok}')
            if harga != '':
                print(f'Harga baru: {harga}')
        # @manipulasi list of monster shop
    shopMenu = True # Kembali ke shop menu
    return shopMenu,monsterShop_db,itemShop_db

def fnHapus(monster_db, monsterDalamShop, itemDalamShop,monsterShop_db: list, itemShop_db: list, tipeList: str) -> bool:
    if tipeList == 'monster':
        tipe = 'Monster'
        fn.printData(fn.appendHeader(monsterDalamShop,tipeList))
        listDatabase = monster_db
        listUnitShop = monsterShop_db
        indexKolom = 1 # indexKolom Nama untuk pemanggilan
    elif tipeList == 'item':
        tipe = 'Item'
        fn.printData(fn.appendHeader(itemDalamShop,tipeList))
        listDatabase = itemShop_db
        listUnitShop = itemShop_db
        indexKolom = 0

    id = input(fn.clr(f'>>> Masukkan id {tipeList}: ','cyan',''))
    if tipeList == 'item':
        id = fn.convertItemNames(id,'id')
    # Manipulasi list
    for line in listDatabase:
        if line[0] == id:
            namaUnit = line[indexKolom]
    for line in listUnitShop:
        if line[0] == id:
            line[1] = 0
    namaUnit = fn.convertItemNames(namaUnit,'name')
    print(f"{tipe} {namaUnit} telah berhasil dihapus dari shop!")
    shopMenu = True # Kembali ke shop menu
    return shopMenu, monsterShop_db, itemShop_db

def shopManagement(monster_db,monsterShop_db,itemShop_db):
    # INIT
    admin_main_aksi = ['lihat','tambah','ubah','hapus','keluar']
    lihat_valid = ['monster','item','batal']
    shopMenu = True

    # HEADER
    print('='*22 + fn.clr(' SHOP MANAGEMENT ','yellow','bold') + '='*22, '\n')
    print('	＼(＾▽＾)／  Admin, Welcome to the SHOP!!!','\n')

    while shopMenu: # kembali ke menu shop setelah aksi
        shopMenu = False
        itemDalamShop= fn.updateListShop(itemShop_db,'item') # list item yang ada di shop (stok > 0)
        monsterShopList = fn.combineList(monster_db,monsterShop_db)
        monsterDalamShop = fn.updateListShop(monsterShopList,'monster')
        # SHOP MENU
        while True:
            
            print()
            print('─'*55)
            print('=> AKSI <=\n'
                '> Lihat\n'
                '> Tambah\n'
                '> Ubah\n'
                '> Hapus\n'
                '> Keluar\n')
            print('─'*55)
            aksi_shopmng = str.lower(input(fn.clr('>>> Pilih aksi: ','cyan','')))
            if aksi_shopmng in admin_main_aksi:
                break
            else:
                print('Pilih aksi yang valid!\n')

        if aksi_shopmng != 'keluar':
            monster_potion = menuPertama(lihat_valid, aksi_shopmng)
            if monster_potion == 'batal':
                shopMenu = True
                continue
            if aksi_shopmng == 'lihat':
                print('─'*55)
                shopMenu = shop.f_lihat(monster_potion,monsterDalamShop,itemDalamShop)

            elif aksi_shopmng == 'tambah':
                print('─'*55)
                shopMenu,monsterShop_db,itemShop_db = fnTambah(monster_db, monsterDalamShop, monsterShop_db,itemDalamShop, itemShop_db, shopMenu, monster_potion)

            elif aksi_shopmng == 'ubah':
                print('─'*55)
                shopMenu,monsterShop_db,itemShop_db = fnUbah(monsterShop_db,itemShop_db,monster_db, monsterDalamShop, itemDalamShop,shopMenu,monster_potion)

            elif aksi_shopmng == 'hapus':
                print('─'*55)
                shopMenu, monsterShop_db,itemShop_db = fnHapus(monster_db, monsterDalamShop, itemDalamShop,monsterShop_db,itemShop_db,monster_potion)
       
        else: #keluar
            print()
            print('	ヾ(•ω•`)o Selamat Tinggal!!! ')
            print()
    return monster_db,monsterShop_db,itemShop_db