from src import load, register, login, menu, inventory, battle, arena, shop_management, shop, laboratory, monster_management, logout, functions, save, exit_

""" PROGRAM UTAMA POKEMON KW
"""


# Mengload semua file csv yang dibutuhkan
user_db, monster_db, itemInventory_db, itemShop_db, monsterInventory_db, monsterShop_db, statusLoad = load.load()

# Inisialisasi status apakah sudah login atau register
statusRegsLog = False
status_login = ""
# Akan langsung mengeprint menu untuk login atau register akun
while True:
    while True:
        print("""
    Ketik REGISTER, LOGIN, atau HELP untuk memulai program
    Ketik KELUAR untuk keluar program
            """)
        actionAwal = str.lower(input(functions.clr('>>> ','cyan','')))

    # Jika ingin register makan akan menjalankan fungsi register
        if actionAwal == "register":
            print()
            user_id, user_db, monsterInventory_db, status_login = register.register(user_db,monster_db, monsterInventory_db)
            break
        # Jika ingin login ke akun yang sudah ada akan menjalankan fungsi login
        elif actionAwal == "login":
            print()
            user_id, status_login = login.login(user_db)
            if not user_id:
                continue
            elif int(user_id) > -1 :
                break
        elif actionAwal == "help":
            print()
            helpMenu = menu.help(status_login)
            print(helpMenu)
            continue
        elif actionAwal == 'keluar':
            exit()
        else:
            print("Command tidak valid\n")

    owca_coin = int(user_db[user_id-1][4])
    while True:
        monster_user = functions.inventoryUser(monsterInventory_db, str(user_id))
        inventory_user = functions.inventoryUser(itemInventory_db, str(user_id))
        action2 = str.lower(input(functions.clr('>>> ','cyan',''))) # Input untuk aksi utama kedua yang dilakukan oleh user

        if action2 == "logout" :
            status_login = logout.logout(status_login)
            if status_login == "" :
                break

        elif action2 == "inventory":
            if status_login == "agent":
                inventory.inventory(monster_user, inventory_user, monster_db, owca_coin, user_id)
            else:
                print ("Anda tidak memiliki akses ke inventory!")
        elif action2 == "battle":
            if status_login == "agent":
                owca_coin, inventory_user = battle.battle(owca_coin, monster_user, monster_db,inventory_user)
            else:
                print ("Anda tidak memiliki akses ke battle!")
        elif action2 == "help":
            helpMenu = menu.help(status_login)
            print(helpMenu)
        elif action2 == "arena":
            if status_login == "agent":
                owca_coin, inventory_user = arena.arena(owca_coin, monster_user, monster_db, inventory_user)
            else:
                print ("Anda tidak memiliki akses ke arena!")
        elif action2 == "laboratory":
            if status_login == "agent":
               monsterInventory_db, owca_coin = laboratory.laboratory(monster_db,monsterInventory_db,user_db,user_id,owca_coin)
            else:
                print ("Anda tidak memiliki akses ke laboratory!")
        elif action2 == "shop":
            if status_login == "agent":
                monster_db, itemInventory_db, itemShop_db, monsterInventory_db, monsterShop_db, owca_coin = shop.shop(user_db, monster_db, itemInventory_db, itemShop_db, monsterInventory_db, monsterShop_db,user_id,owca_coin)
            else:
                monster_db, monsterShop_db, itemShop_db = shop_management.shopManagement(monster_db,monsterShop_db,itemShop_db)
        elif action2 == "monster":
            if status_login == "admin":
                monster_db, monsterShop_db = monster_management.monsterManagement(monster_db,monsterShop_db)
            else:
                print ("Anda tidak memiliki akses ke monster management!")
        elif action2 == "save":
            user_db[user_id-1][4] = owca_coin
            save.save(user_db, monster_db, monsterShop_db, monsterInventory_db, itemShop_db, itemInventory_db)
        elif action2 == "exit":
            game_status = exit_.exit_(user_db, monster_db, monsterShop_db, monsterInventory_db, itemShop_db, itemInventory_db)
            if not game_status :
                print(functions.clr('\nKeluar dari program...\n','red',''))
                exit()
        else:
            print ("Input tidak valid, silakan ulangi!\n")
