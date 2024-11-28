
from src import functions
def inventory(monster_user:list, inventory_user:list, monster_df:list, owca_coin:str, user_id:int):
    print()
    print (functions.clr("<============ ",'green','bold')+functions.clr('INVENTORY LIST (User ID: '+str(user_id)+'))','cyan','bold')+functions.clr(" ============>",'green','bold'))
    print (f"Jumlah O.W.C.A. Coin-mu sekarang {owca_coin}.")
    print 
    for i in range (len(monster_user)):
        print (f"{i+1}. Monster        (Name: {monster_df[int(monster_user[i][1])-1][1]}, Lvl: {monster_user[i][2]}, HP: {monster_df[int(monster_user[i][1])-1][4]})")
    for j in range (len(inventory_user)):
        print (f"{len(monster_user)+ j+1}. Potion         (Type: {functions.convertItemNames((inventory_user[j][1]),'name')}, Amount: {inventory_user[j][2]})")
    while True:
        print('\nKetik KELUAR untuk keluar dari inventory')
        print (functions.clr("Ketikkan id untuk menampilkan detail item: ",'cyan',''), end="")
        b = input()
        if functions.isInteger(b):
            if 0 < int(b) <= (len(inventory_user) + len(monster_user)):
                a = int(b)
                a -= 1
                if a > len(monster_user)-1:
                    print('\n'+ functions.clr('POTION','greenDark','bold'),end='')
                    print (f"""
Type: """ + functions.convertItemNames(f'{inventory_user[a-len(monster_user)][1]}','name') + f"""
Quantity: {inventory_user[a-len(monster_user)][2]}""")
                elif 0 <= a <= len(monster_user)-1:
                    print('\n'+ functions.clr('MONSTER','greenDark','bold'),end='')
                    print (f"""
Name: {monster_df[int(monster_user[a][1])-1][1]}                
ATK Power: {monster_df[int(monster_user[a][1])-1][2]}
DEF Power: {monster_df[int(monster_user[a][1])-1][3]}
HP: {monster_df[int(monster_user[a][1])-1][4]}
Level: {monster_user[a][2]}""")
            else:
                print ("Input tidak valid, coba lagi!")
        elif b == 'keluar':
            print ("Keluar dari inventory...\n")
            break
        else: print('Input tidak valid!')