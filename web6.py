import numpy as np
from colorama import Fore, Back, Style
arr = np.array([['CDN', 'HR-WEB', 'HR-API', "BI-WEB", "BI-API", "ERP-WEB", "ERP-API", "CRM-WEB", "CRM-API", "EOFFICE-WEB", "EOFFICE-API"], ['','','','','','','','','','','']], dtype=object)

def Sl_Product():
    sl = ""
    sl = input(Fore.GREEN + "Vui lòng nhập số lượng muốn cài(Mặc định là 1 nếu không nhập): " + Style.RESET_ALL)
    if sl == "":
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
            case "0":
                break
            case "1":
                print("Bạn đã chọn CDN")
                num = int(Sl_Product())
                arr[1][0] = num
            case "2":
                print("Bạn đã chọn HR-WEB")
                num = int(Sl_Product())
                arr[1][1] = num
            case "3":
                print("Bạn đã chọn HR-API")
                num = int(Sl_Product())
                arr[1][2] = num
            case _:
                print("Bạn chưa chọn sản phẩm. Vui lòng nhập lại")

choices()
for i in arr[0]:
    rows, cols = np.where(arr == i)
    if arr[1][cols] != "":
        print("Bạn đã chọn sản phẩm "+i+" với số lượng "+str(arr[1][cols]))

