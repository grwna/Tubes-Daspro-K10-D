from src import save,functions

def exit_(df_user:list, df_monster:list, df_monsterShop:list, df_monsterInventory:list, df_itemShop:list, df_itemInventory:list)-> bool :
    gameMasihJalan = True
    while gameMasihJalan :
        inginExit = str.lower(input(functions.clr("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ",'cyan','')))

        while (inginExit != "y") and (inginExit != "n") :
            print("Input Tidak Valid!")
            inginExit = str.lower(input(functions.clr("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ",'cyan','')))
    
        if (inginExit == "y") :
            save.save(df_user, df_monster, df_monsterShop, df_monsterInventory, df_itemShop, df_itemInventory)
            gameMasihJalan = False

        else :
            gameMasihJalan = False
    
    return gameMasihJalan
