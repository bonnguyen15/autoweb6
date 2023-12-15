import numpy as np
arr = np.array([['CDN', 'HR-WEB', 'HR-API'], ['','','']], dtype=object)

def Sl_Product():
    sl = ""
    sl = input("Vui lòng nhập số lượng muốn cài(Mặc định là 1 nếu không nhập): ")
    if sl == "":
        sl = 1
    return sl
def choices():
    while True:
        number = 0
        for a in arr[0]:
            number += 1
            print (str(number) + ". " + a, end="   ")
        choices = input('Vui lòng nhập số (Nhập 0 để kết thúc): ')
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
    if arr[1][cols] == "":
        continue
    else:
        print("Bạn đã chọn sản phẩm "+i+" với số lượng "+str(arr[1][cols]))

