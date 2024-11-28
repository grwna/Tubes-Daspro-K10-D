from src import functions as fn

'''F10: Shop & Currency
{ Spesifikasi : Sebuah menu shop dimana Agent dapat melihat dan membelistok
monster atau potion dari shop

Keluaran: 
monsterShop_db -> monster_shop.csv (mengubah stok)
itemShop_db -> item_shop.csv (mengubah stok)
monsterInventory_db -> monster_inventory.csv  (menambah monster di inventory)
itemInventory_db -> item_inventory.csv (menambah item di inventory)
'''


def shop_lihat_beli(cekLihat: list,aksi_shop: str,owca: int) -> str:
    print('─'*55)
    if aksi_shop == 'beli':
        print(f'Jumlah O.W.C.A. Coin-mu sekarang {owca}','\n')
    while True:
        print('=> AKSI <=\n'
                '> Monster\n'
                '> Item\n'
                '> Batal')
        print('─'*55)
        aksi_lihat = str.lower(input(fn.clr('>>> Mau ' + aksi_shop + ' apa?: ','cyan','')))
        # Validasi Input
        if aksi_lihat in cekLihat:
            break
        else:
            print('Pilih opsi yang valid!','\n')
    return aksi_lihat

def f_lihat(tipeList: str, combMonsterList:list,itemList:list) -> bool:
    # Menampilkan list Monster
    if tipeList == 'monster':
        print('─'*75)
        fn.printData(fn.appendHeader(combMonsterList,tipeList))
        print('─'*75)

    elif tipeList == 'item': # potion
        print('─'*55)
        fn.printData(fn.appendHeader(itemList,tipeList))
    shopMenu = True # Kembali ke shop menu
    return shopMenu


def beliShop (monsterDalamShop: list, itemDalamShop:list,monsterShopList: list,monsterShop_db: list,itemShop_db: list, monsterInventory_db:list,itemInventory_db:list, OC:int, tipeList: str, idUser = str) -> bool:
    
        # check user_id dan monster_id dari (monster_inventory.csv)
    if tipeList == 'monster':
        while True:
            idBeli = input(fn.clr(f'>>> Masukkan id monster: ','cyan',''))
            valid = False   # Mengecek Validasi ID unit yang di beli
            if not fn.isInteger(idBeli):
                print('Masukan berupa integer!','\n')
                continue
            for line in monsterDalamShop:
                if idBeli in line[0]: 
                    valid = True
            if valid:
                break
            else:
                print('Monster tersebut tidak ada di shop!')
                print()

        inventory = fn.inventoryUser(monsterInventory_db,str(idUser))
        stat = fn.cekUdahAda(idBeli,inventory,'1') # '1' menunjukkan index kolom (monster id ada di indeks kolom 1)

        print('─'*55)
        if stat:
            print(f'{monsterShopList[int(idBeli)-1][1]} sudah ada dalam inventory-mu! Pembelian dibatalkan')

        elif not stat:
            hargaMonster = int(monsterShop_db[int(idBeli)-1][2])
            stokMonster = int(monsterShop_db[int(idBeli)-1][1])
            if OC > hargaMonster:
                while True:
                    print('Harga monster adalah ' + fn.clr(f'{hargaMonster}','yellow',''))
                    yakin = str.lower(input(fn.clr(f'>>> Apakah kamu yakin ingin membeli {monsterShopList[int(idBeli)-1][1]}? (Y/N): ','cyan','')))
                    if yakin in ['y','n']:
                        break
                    else:
                        print('Pilih opsi yang valid!','\n')
                if yakin == 'y':
                    lanjut = True
                    monsterInventory_db.append([str(idUser),idBeli,'1']) # 1 adalah level
                    stokMonster = stokMonster - 1 # Mengurangi stok monster di shop
                    OC = OC -  hargaMonster

                    monsterShop_db = fn.updateStock(monsterShop_db,stokMonster,idBeli,1)  # Assign stok baru
                    monsterShopList = fn.updateStock(monsterShopList,stokMonster,idBeli,5)
     
                    print(f'Berhasil membeli monster {monsterShopList[int(idBeli)-1][1]} !')
                else:
                    lanjut = False
            else: # OC kurang dari harga monster atau stok monster habis
                if OC < hargaMonster:
                    print('OC-mu tidak cukup! Membatalkan pembelian')



    elif tipeList == 'item':
        print('─'*55)
        while True:
            idBeli = input(fn.clr(f'>>> Masukkan id item: ','cyan',''))
            valid = False   # Mengecek Validasi ID unit yang di beli

            if not fn.isInteger(idBeli):
                print('Masukan berupa integer!','\n')
                continue
            
            # List item tidak ada ID, maka id harus di convert ke type
            idBeliBaru = fn.convertItemNames(idBeli,'id')

            for line in itemDalamShop:
                if idBeliBaru in line[0]: 
                    valid = True
            if valid:
                break
            else:
                print('Item tersebut tidak ada di shop!','\n')

        hargaItem = int(itemShop_db[int(idBeli)-1][2])
        stokMonster = int(itemShop_db[int(idBeli)-1][1])
        while True:        
            jumlah = int(input(fn.clr('>>> Masukkan Jumlah: ','cyan','')))
            print()
            # Validasi
            if not fn.isInteger(idBeli):
                print('Masukan berupa integer!','\n')
                continue
            if jumlah > stokMonster:
                print('Stok item tidak cukup!')
            elif OC < hargaItem*jumlah:
                print('OC-mu tidak cukup!','\n')

            else: # Stok item cukup untuk di beli
                break
        
        
        # Mengecek apakah item sudah ada di inventory user
        inventory = fn.inventoryUser(itemInventory_db,str(idUser))
        stat = fn.cekUdahAda(idBeli,inventory,'1')
        
        # Validasi 'OC' dilakukan di validasi 'jumlah'
        if stat:  # Jika item sudah ada di inventory
            for line in itemInventory_db:
                if line[0] == str(idUser) and line[1] == idBeliBaru:
                    line[2] = str(int(line[2]) + jumlah)
        else:      # Jika item belum ada di inventory (append baris baru)
            itemInventory_db.append([str(idUser),idBeliBaru,str(jumlah)])
        namaItem = idBeliBaru
        namaItem = fn.convertItemNames(namaItem,'name')

        while True:
            print('Harga total adalah ' + fn.clr(f'{hargaItem*jumlah} OC\n','yellow',''))
            yN = str.lower(input(fn.clr(f'Apakah kamu yakin ingin membeli {jumlah} {namaItem}? (y/n)','cyan','')))
            if yN in ['y','n']:
                if yN == 'y':
                    lanjut = True
                    break
                elif yN == 'n':
                    lanjut = False
                    break
            else:
                print('Masukan tidak valid')
        # Post purchase processing
    if lanjut:
        OC = OC - hargaItem*jumlah
        itemShop_db[int(idBeli)-1][1] = str(stokMonster - jumlah)
        print(f'Berhasil membeli item: {jumlah} {namaItem}.')
        print()
    print()
    print(f'Jumlah O.W.C.A. Coin-mu sekarang {OC}','\n')
    shopMenu = True
    return monsterShopList,shopMenu,OC,monsterShop_db,itemShop_db,monsterInventory_db,itemInventory_db


def shop(user_db, monster_db, itemInventory_db, itemShop_db, monsterInventory_db, monsterShop_db,idUser,owca):
    # HEADER
    print('='*22 + ' SHOP ' + '='*22, '\n')
    print('	＼(＾▽＾)／  Welcome to the SHOP!!!','\n')

    # INIT
    # Pengecek validasi input
    aksiUtama = ['lihat','beli','keluar','data']
    cekLihat = ['monster','item','batal']
    owca = int(owca)
    shopMenu = True
    while shopMenu: # kembali ke menu shop setelah aksi
        shopMenu = False
        
        # Inisialisasi list yang akan ditampilkan dalam shop (harus di loop)
        itemDalamShop= fn.updateListShop(itemShop_db,'item') # list item yang ada di shop (stok > 0)
        monsterShopList = fn.combineList(monster_db,monsterShop_db)
        monsterDalamShop = fn.updateListShop(monsterShopList,'monster')

        while True:
            print('─'*55)
            print('=> AKSI <=\n'
                  '> Lihat\n'
                  '> Beli\n'
                  '> Keluar')
            print('─'*55)
            aksi_shop = str.lower(input(fn.clr('>>> Pilih aksi: ','cyan','')))

            if aksi_shop in aksiUtama:
                break
            else:
                print('Pilih aksi yang valid!')

        if aksi_shop != 'keluar':
            aksi_shop_2 = shop_lihat_beli(cekLihat,aksi_shop,owca)
            if aksi_shop == 'lihat':
                shopMenu = f_lihat(aksi_shop_2,monsterDalamShop,itemDalamShop)
        
            elif aksi_shop == 'beli':
                monsterShopList,shopMenu,owca,monsterShop_db,itemShop_db,monsterInventory_db,itemInventory_db = (
                beliShop(monsterDalamShop,itemDalamShop,monsterShopList,monsterShop_db,itemShop_db,monsterInventory_db,itemInventory_db,owca,aksi_shop_2,idUser))
                
        else: #keluar
            owca = str(owca)
            print()
            print('	ヾ(•ω•`)o Selamat Tinggal!!! ')
            print('\n\n')
    return monster_db, itemInventory_db, itemShop_db, monsterInventory_db, monsterShop_db,owca
