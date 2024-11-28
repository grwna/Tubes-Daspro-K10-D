from src import functions as fn

'''F11: Laboratory
{ Spesifikasi : Sebuah menu untuk Agent dapat meng-upgrade level monster}

Keluaran:
monsterInventory_db -> monster_inventory.csv (mengubah level monster)
user_db -> user.csv (mengubah O.W.C.A Coin user)
'''

def panggilBerdasarkanID(namaList,indexID):
    idx = 0
    for line in namaList:
        if line[0] == indexID:
            break
        idx +=1
    return idx

def laboratory(monster_db,monsterInventory_db,user_db,idUser,owca):
    # INIT
    menuLab = True
    lanjut = True
    inventory = fn.inventoryUser(monsterInventory_db,str(idUser)) # Hanya untuk Display
    jumlahMonster = fn.hitungJumlahBaris(inventory)

    print(fn.clr('=+'*15,'blue','')+fn.clr(' LABORATORY ','red','bold')+fn.clr('=+'*15,'blue',''))

    print('\n',fn.clr('		( •̀ᴗ•́ )و ̑̑ Welcome to the LAB!','cyan','bold'))

    while menuLab:
        menuLab = False
        print()
        print(fn.clr('=>'*15 ,'blue','')+fn.clr(' MONSTER LIST ','red','bold')+fn.clr('<='*15 ,'blue','')) # @kalo pake \n ada spasi di terminal
        print()
        if jumlahMonster > 0:
            for i in range(jumlahMonster):
                idx = panggilBerdasarkanID(monster_db,inventory[i][1])
                namaMonster = monster_db[idx][1]
                levelMonster = inventory[i][2]
                print(f'{i+1}. {namaMonster} (Level: {levelMonster})')
            print()
            lanjut = True
            
        else:
            print()
            print('Tidak ada monster di inventory mu!','\n')
            input(fn.clr('>>> Keluar? ','cyan',''))
            lanjut = False
        

        # !placeholder
        if lanjut:
            while True:
                aksi = str.lower(input(f">>> Pilih aksi ({fn.clr('upgrade','cyan','')}/{fn.clr('keluar','red','')}): ")) 
                if aksi == 'upgrade':
                    print()
                    print('<'+'->'*15 + ' UPGRADE PRICE ' + '<-'*15+'>')
                    print('Level 1 -> Level 2: 300 OC')
                    print('Level 2 -> Level 3: 600 OC')
                    print('Level 3 -> Level 4: 1000 OC')
                    print('Level 4 -> Level 5: 1500 OC','\n')
                    print(f'O.W.C.A Coin-mu: {owca}')

                    while True:
                        print('─'*55)
                        nomorMonster = str.lower(input(fn.clr('>>> Pilih Monster: ','cyan','')))
                        if nomorMonster == 'keluar':
                            menuLab = True
                            break
                        if not fn.isInteger(nomorMonster):
                            print('Masukkan berupa integer!','\n')
                            continue
                        elif int(nomorMonster) > jumlahMonster or int(nomorMonster) <= 0:
                            print('Monster tidak ada di inventory')

                        levelMonster =  inventory[int(nomorMonster)-1][2]        # ditaro disini untuk validasi
                        if levelMonster == '1': harga = 300
                        elif levelMonster == '2': harga = 600
                        elif levelMonster == '3': harga = 1000
                        elif levelMonster == '4': harga = 1500

                        if int(nomorMonster) > jumlahMonster or (int(nomorMonster) <= 0):
                            print('Pilih opsi yang valid! (opsi sesuai angka monster)\n')
                            continue
                        elif int(levelMonster) > 4:
                            print('Level monster sudah maksimum!\n')
                        elif harga > int(owca):
                            print('OC-mu tidak cukup untuk meng-upgrade monster!\n')
                        else: break

                    if not menuLab:
                        idMonsterAsli = inventory[int(nomorMonster)-1][1]
                        panggilBerdasarkanID(monster_db,idMonsterAsli)
                        namaMonster = monster_db[idx-1][1]

                        while True:
                            yesNo = str.lower(input(fn.clr('>>> Lanjutkan upgrade (Y/N): ','cyan','')))
                            if yesNo == 'y':
                                print(f'Selamat, {namaMonster} berhasil di-upgrade ke level {int(levelMonster) + 1} !\n')
                                owca = str(int(owca)- harga)
                                inventory[int(nomorMonster)-1][2]  = str(int(levelMonster) + 1)
                                print(f'O.W.C.A Coin-mu: {owca}')
                                menuLab = True
                                break
                            elif yesNo == 'n':
                                menuLab = True
                                break
                            else:
                                print('Masukkan input yang valid!','\n')
                    break
                elif aksi == 'keluar': # Keluar
                    print()
                    print('	ヾ(•ω•`)o Selamat Tinggal!!! ')
                    print()
                    break
                else:
                    print('Input tidak valid!\n')
                    continue
    return monsterInventory_db, owca