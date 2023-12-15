import os
try:
    import numpy as np
except:
    os.system(f"pip install numpy")
import numpy as np
from colorama import Fore, Back, Style
arr = np.array([['CDN', 'HR-WEB', 'HR-API', "BI-WEB", "BI-API", "ERP-WEB", "ERP-API", "CRM-WEB", "CRM-API", "EOFFICE-WEB", "EOFFICE-API"], ['','','','','','','','','','','']], dtype=object)

def Sl_Product():
    sl = ""
    sl = input("Vui long nhap so luong muon cai(Mac dinh la 1 neu khong nhap): ")
    if sl == "" or sl <= '0':
        sl = 1
    return sl
def choices():
    number = 0
    for a in arr[0]:
        number += 1
        print (str(number) + ". " + a, end="   ")
    while True:
        choices = input('\nVui long nhap san pham can cai (Nhap 0 đe ket thuc): ')
        match choices:
            case "0": break
            case "1": print("Ban da chon CDN"); num = int(Sl_Product()); arr[1][0] = num
            case "2": print("Ban da chon HR-WEB"); num = int(Sl_Product()); arr[1][1] = num
            case "3": print("Ban da chon HR-API"); num = int(Sl_Product()); arr[1][2] = num
            case "4": print("Ban da chon BI-WEB"); num = int(Sl_Product()); arr[1][3] = num
            case "5": print("Ban da chon BI-API"); num = int(Sl_Product()); arr[1][4] = num
            case "6": print("Ban da chon ERP-WEB"); num = int(Sl_Product()); arr[1][5] = num
            case "7": print("Ban da chon ERP-API"); num = int(Sl_Product()); arr[1][6] = num
            case "8": print("Ban da chon CRM-WEB"); num = int(Sl_Product()); arr[1][7] = num
            case "9": print("Ban da chon CRM-API"); num = int(Sl_Product()); arr[1][8] = num
            case "10": print("Ban da chon EOFFICE-WEB"); num = int(Sl_Product()); arr[1][9] = num
            case "11": print("Ban da chon EOFFICE-API"); num = int(Sl_Product()); arr[1][10] = num
            case _: print("Ban chua chon san pham. Vui long nhap lai")

choices()
for i in arr[0]:
    rows, cols = np.where(arr == i)
    if arr[1][cols] != "":
        print("Ban da chon san pham "+i+" voi so lan cai:",arr[1][cols[0]])

