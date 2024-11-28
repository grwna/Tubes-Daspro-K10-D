import os
import time
from src import functions as fn

'''F14:
PROGRAM SAVE
{ Spesifikasi : Melakukan penyimpanan data ke dalam file setelah dilakukan perubahan. }'''

def save(df_user:list, df_monster:list, df_monsterShop:list, df_monsterInventory:list, df_itemShop:list, df_itemInventory:list) -> None :
    folder = input(fn.clr("Masukkan nama folder : ",'cyan',''))
    parentFolder = "data_save"
    fullPath = os.path.join(parentFolder, folder)
    # Asumsi input valid
    
    print("Saving...")
    time.sleep(0.75)

    if not(os.path.isdir(parentFolder)) :
        os.mkdir(parentFolder)
        print(f"Membuat folder parent {parentFolder}...")
    
    if not (os.path.isdir(fullPath)) :
        os.mkdir(fullPath)
        print(f"Membuat folder {fullPath}")

    # Save data user
    with open(f"{fullPath}/user.csv",'w') as f :
        # Header
        f.write("id;username;password;role;oc\n")
        # Body
        for line in df_user :
            text = f"{line[0]};{line[1]};{line[2]};{line[3]};{line[4]}\n"
            f.write(text)
        f.close()

    # Save data monster
    with open(f"{fullPath}/monster.csv",'w') as f :
        # Header
        f.write("id;type;atk_power;def_power;hp\n")
        # Body
        for line in df_monster :
            text = f"{line[0]};{line[1]};{line[2]};{line[3]};{line[4]}\n"
            f.write(text)
        f.close()          

    # Save data monster shop
    with open(f"{fullPath}/monster_shop.csv",'w') as f :
        # Header
        f.write("monster_id;stock;price\n")
        # Body
        for line in df_monsterShop :
            text = f"{line[0]};{line[1]};{line[2]}\n"
            f.write(text)
        f.close()  

    # Save data monster inventory
    with open(f"{fullPath}/monster_inventory.csv",'w') as f :
        # Header
        f.write("user_id;monster_id;level\n")
        # Body
        for line in df_monsterInventory :
            text = f"{line[0]};{line[1]};{line[2]}\n"
            f.write(text) 
        f.close() 

    # Save data item shop
    with open(f"{fullPath}/item_shop.csv",'w') as f :
        # Header
        f.write("type;stock;price\n")
        # Body
        for line in df_itemShop :
            text = f"{line[0]};{line[1]};{line[2]}\n"
            f.write(text)
        f.close()

    # Save data monster
    with open(f"{fullPath}/item_inventory.csv",'w') as f :
        # Header
        f.write("user_id;type;quantity\n")
        # Body
        for line in df_itemInventory :
            text = f"{line[0]};{line[1]};{line[2]}\n"
            f.write(text)  
        f.close()
    
    print(f"Berhasil menyimpan data di folder {fullPath}\n")