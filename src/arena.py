from src import battle,functions

def arena(owca_coin:str, monster_user:list, monster_db:list, inventory_user:list):
    
    # Inisialisasi variabel
    totalDamageDiterima = 0
    totalDamageDiberikan = 0
    hadiah = [50, 75, 120, 150, 250]
    totalhadiah = [0, 50, 125, 245, 395, 645]
    # Memulai arena
    print("Selamat datang di arena!")
    monsterAgent, levelAgent = battle.seleksimonster(monster_user, monster_db)
    stage = 1
    while stage < 6:
        levelMusuh = stage
        print(f"===== Stage {stage} =====")
        damageDiberikan, damageDiterima, inventory_user, stat = battle.startBattle(monster_db, inventory_user, monsterAgent, levelMusuh, levelAgent)
        totalDamageDiterima += damageDiterima
        totalDamageDiberikan += damageDiberikan
        # Mengecek apakah agent kalah
        if stat == "kalah":
            print("Womp womp agent kalah dalam arena")
            break
        elif stat == "kabur":
            print("Tidak seru! Rupanya agent kabur dari arena!!! :-b")
            break
        else:
            if stage < 5:
                print(f"STAGE CLEARED! Anda mendapatkan "+functions.clr(f'{hadiah[stage - 1]} OC','yellow','')+" pada stage ini!\n")
                owca_coin = str(int(owca_coin) + hadiah[stage - 1])
                stage += 1
                input(functions.clr("Tekan enter untuk melanjutkan ke stage selanjutnya!",'cyan',''))
            else:
                print(f"Selamat, Agent berhasil menyelesaikan seluruh stage Arena !!!")
                owca_coin = str(int(owca_coin) + hadiah[stage - 1])
                stage += 1
                break
    
    # Menampilkan stats
    stats = """
====== STATS ======
Total hadiah      : """ + functions.clr(f'{totalhadiah[stage-1]} OC','yellow','') + f"""
Jumlah Stage      : {stage-1}
Damage diberikan  : """+ functions.clr(f'{totalDamageDiberikan}','green','') +"""
Damage diterima   : """+ functions.clr(f'{totalDamageDiterima}\n','red','') + """
Keluar dari arena...\n"""
    print(stats)
    return owca_coin, inventory_user