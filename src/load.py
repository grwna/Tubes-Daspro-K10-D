import os
import sys
import argparse
from src import functions as fn

'''F15:
PROGRAM LOAD
{ Spesifikasi : Melakukan loading data ke dalam sistem dan 
otomatis dijalankan ketika sistem mulai pertama kali bila diberikan 
input nama folder yang berisi file penyimpanan. 
 file penyimpanan dalam folder dijamin ada dan memiliki nama yang fixed. 
 Untuk folder, harus melakukan validasi. }'''

def cekArrayKosong(arr:list)->list :
    data = []
    for i in arr :
        if not(i == '' or i == "\n") :
            data +=[i]

    return data

def afkhFolderAda(path:str) -> bool:
    isPathAda = os.path.exists(path)

    return isPathAda

def separasiArray(db:list)->list :
    data = []
    adlhHeader = True # Variabel untuk menandai header
    for line in db:
        if adlhHeader :
            adlhHeader = False
            continue    # Melewati header
        row = []
        temp=""
        skipLine = False
        for char in line:
            if char == ';':
                row.append(temp)
                temp = ''
            elif char == "\n" :
                skipLine = True
            elif char == " " and not temp :
                continue
            else:
                if skipLine and temp :
                    row.append(temp)
                    temp =""
                    skipLine = False
                temp += char
        if temp:  # Menambahkan elemen terakhir setelah loop
            row.append(temp)
            temp = ''  # Reset temp untuk line berikutnya
        if row:  # Hanya menambahkan row jika tidak kosong
            data.append(row)
    return data

def bacaFile(file:list)->list :
    lines = []
    for line in file :
        lines.append(line)
    return lines
    
def load() -> list[list] :
    print("\nLoading...\n")     #loadin
    parser = argparse.ArgumentParser(usage="python main.py <nama_folder>")
    parser.add_argument("x")
    stat = True

    if len(sys.argv) == 1 :     # Mengecek apakah folder ada atau tidak
        print("Tidak ada nama folder yang diberikan!")
        sys.exit(1)
    args = parser.parse_args()

    if afkhFolderAda(args.x) :
        with open(f"{args.x}/user.csv", 'r') as file:
            user_db = separasiArray(cekArrayKosong(bacaFile(file)))
        with open(f"{args.x}/monster.csv", 'r') as file:
            monster_db = separasiArray(cekArrayKosong(bacaFile(file)))
        with open(f"{args.x}/item_inventory.csv", 'r') as file:
            itemInventory_db = separasiArray(cekArrayKosong(bacaFile(file)))
        with open(f"{args.x}/item_shop.csv", 'r') as file:
            itemShop_db = separasiArray(cekArrayKosong(bacaFile(file)))
        with open(f"{args.x}/monster_inventory.csv", 'r') as file:
            monsterInventory_db = separasiArray(cekArrayKosong(bacaFile(file)))
        with open(f"{args.x}/monster_shop.csv", 'r') as file:
            monsterShop_db = separasiArray(cekArrayKosong(bacaFile(file)))
        
        print(fn.clr('X=='*21+'X','yellow','bold'))
        print('+ > '*4+ fn.clr(" Selamat datang di program OWCA ! ",'cyan','bold')+'< + '*4)
        print(fn.clr('X=='*21+'X','yellow','nold'))
        return  user_db, monster_db, itemInventory_db, itemShop_db, monsterInventory_db, monsterShop_db, stat
    else :
        stat = False
        print(f"Folder {args.x} tidak ditemukan")


    return [], [], [], [], [], [], stat

