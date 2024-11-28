# SEMENTARA
# Menyimpan fungsi-fungsi yang akan diambil dari function-function lainnya
def appendHeader(namaList: list, tipeList: str) -> list:
    if tipeList == 'monster':
        # Mengubah judul kolom pada list
        
        temp = ['ID','Type','ATK Power','DEF Power','HP']
        if len(namaList[0]) == 7:
            temp.append('Stok')
            temp.append('Harga')
        temp2 = []
        temp2.append(temp)
        for line in namaList:
            temp2.append(line)
        

    if tipeList == 'item':
        tempList =[]
        index = 1

        for line in namaList:    # Memunculkan kolom ID untuk potion/item
            line =[f'{str(index)}'] + line
            tempList.append(line)
            index += 1

        temp=['ID','Tipe'] 
        if len(namaList[0]) == 3:
            temp.append('Stok')
            temp.append('Harga')
        temp2 = []
        temp2.append(temp)
        for line in tempList:
            temp2.append(line)
        for line in temp2:
            if line[1] == 'strength': line[0] = '1'; line[1] = 'Strength Potion' 
            if line[1] == 'resilience': line[0] = '2'; line[1] = 'Resilience Potion'
            if line[1] == 'healing': line[0] = '3'; line[1] = 'Health Potion'
    return temp2

def cekUdahAda(inputYangDiCek: str, namaList:list, indexKolom: str) -> bool:
    stat=False
    indexAda = 0
    for i in namaList:
        if i[int(indexKolom)] == inputYangDiCek :
            stat=True
        indexAda += 1
    return stat

def clr(content: str,color: str, mod: str) -> str:
    if color == 'black': color = '30'
    elif color == 'red': color = '91'
    elif color == 'green': color = '92'
    elif color == 'yellow': color = '93'
    elif color == 'blue': color = '94'
    elif color == 'magenta': color = '95'
    elif color == 'cyan': color = '96'
    elif color == 'white': color = '97'
    elif color == 'gray': color = '90'
    elif color == 'redDark': color = '31'
    elif color == 'greenDark': color = '32'
    elif color == 'yellowDark': color = '33'
    elif color == 'blueBDark': color = '34'
    elif color == 'magentaDark': color = '35'
    elif color == 'cyanDark': color = '36'
    elif color == 'whiteDark': color = '37'
    else: color = ''

    if mod == 'normal': mod = '0;'
    elif mod == 'bold': mod = '1;'
    elif mod == 'dim': mod = '2;'
    elif mod == 'italic': mod = '3;'
    elif mod == 'underline': mod = '4;'
    elif mod == 'crossed': mod = '9;'
    else: mod = ''

    teks = "\033["+ mod +color +"m\
"+content +"\033[0;37m"
    return teks

def combineList(list1:list, list2:list)->list:
    combinedList = []
    for baris in range(len(list1)):
        combinedRow = list1[baris][:]
        for kolom in range(1,len(list2[0])):
            combinedRow.append(list2[baris][kolom])  # Append shared column from list2
        combinedList.append(combinedRow)
    return combinedList

def convertItemNames(convert:str,tipe: str) -> str:
    if tipe == 'id':
        if convert =='1': convert ='strength'
        if convert =='2': convert ='resilience'
        if convert =='3': convert ='healing'
    elif tipe == 'name':
        if convert == 'strength': convert = 'Strength Potion' 
        if convert == 'resilience': convert = 'Resilience Potion'
        if convert == 'healing': convert = 'Health Potion'
    
    return convert

def hitungJumlahBaris(namaList:list) -> int:
    jmlhBaris = 0
    for line in namaList:
        jmlhBaris += 1
    return jmlhBaris

def indexDalamList(listRef: list) -> list:
    listIndex = []
    for line in listRef:
        listIndex.append(line[0])
    return listIndex

def inventoryUser(namaList:list ,idUser:str) -> list:
    namaListBaru = []
    for line in namaList:
        if line[0] == idUser:
            namaListBaru.append(line)  # Array yang berisi hanya satu user id untuk mengecek inventory user
    return namaListBaru

def isInteger(cek: str)->bool:
    integer = True
    cek = str(cek)
    for char in cek:
        if ord(char) < 48 or ord(char) > 57:
            integer = False
    return integer

def printData(namaList: list):
    # Merapikan Output
    maxWidth = [max(len(str(line[i])) for line in namaList) for i in range(len(namaList[0]))]
    for line in namaList:
        for i, elem in enumerate (line):
            print(f"{elem:{maxWidth[i]}}" + " || ",end=' ')
        print()

def updateListShop(namaList:list,tipeList:str) -> list:  # Hanya dipakai untuk mengupdate display
    namaListBaru = [] # list monster yang ada di shop (stok > 0)
    for line in namaList:
        if tipeList == 'monster':
            if (line[5]) == 'Stok' or line[5] == 'stock':
                namaListBaru.append(line)
            else:
                if int(line[5]) > 0:
                    namaListBaru.append(line)
        else: # potion
            if (line[1]) == 'stock':
                namaListBaru.append(line)
            else:
                if int(line[1]) > 0:
                    namaListBaru.append(line)
    return namaListBaru

def updateStock(namaList: list,stokBaru: int,idBeli: str,indexKolomId: int) -> list:
    for line in namaList:
        if line[0] == idBeli:
            line[indexKolomId] = str(stokBaru)
    return namaList