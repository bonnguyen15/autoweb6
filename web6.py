import numpy as np
from colorama import Fore, Back, Style
arr = np.array([['CDN', 'HR-WEB', 'HR-API', "BI-WEB", "BI-API", "ERP-WEB", "ERP-API", "CRM-WEB", "CRM-API", "EOFFICE-WEB", "EOFFICE-API"], ['','','','','','','','','','','']], dtype=object)

def Sl_Product():
    sl = ""
    sl = input(Fore.GREEN + "Vui lòng nhập số lượng muốn cài(Mặc định là 1 nếu không nhập): " + Style.RESET_ALL)
    if sl == "" or sl <= '0':
        sl = 1
    return sl
def choices():
    while True:
        number = 0
        for a in arr[0]:
            number += 1
            print (str(number) + ". " + a, end="   ")
        choices = input(Fore.GREEN + '\nVui lòng nhập sản phẩm cần cài (Nhập 0 để kết thúc): ' + Style.RESET_ALL)
        match choices:
            case "0": break
            case "1": print("Bạn đã chọn CDN"); num = int(Sl_Product()); arr[1][0] = num
            case "2": print("Bạn đã chọn HR-WEB"); num = int(Sl_Product()); arr[1][1] = num
            case "3": print("Bạn đã chọn HR-API"); num = int(Sl_Product()); arr[1][2] = num
            case "4": print("Bạn đã chọn BI-WEB"); num = int(Sl_Product()); arr[1][3] = num
            case "5": print("Bạn đã chọn BI-API"); num = int(Sl_Product()); arr[1][4] = num
            case "6": print("Bạn đã chọn ERP-WEB"); num = int(Sl_Product()); arr[1][5] = num
            case "7": print("Bạn đã chọn ERP-API"); num = int(Sl_Product()); arr[1][6] = num
            case "8": print("Bạn đã chọn CRM-WEB"); num = int(Sl_Product()); arr[1][7] = num
            case "9": print("Bạn đã chọn CRM-API"); num = int(Sl_Product()); arr[1][8] = num
            case "10": print("Bạn đã chọn EOFFICE-WEB"); num = int(Sl_Product()); arr[1][9] = num
            case "10": print("Bạn đã chọn EOFFICE-API"); num = int(Sl_Product()); arr[1][10] = num
            case _: print("Bạn chưa chọn sản phẩm. Vui lòng nhập lại")

choices()
for i in arr[0]:
    rows, cols = np.where(arr == i)
    if arr[1][cols] != "":
        print("Bạn đã chọn sản phẩm "+i+" với số lần cài:",arr[1][cols[0]])

