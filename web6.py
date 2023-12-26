import os, string, random
try:
    import numpy as np
except:
    os.system(f"pip install numpy")
import numpy as np
arr = np.array([['CDN', 'HR-WEB', 'HR-API', "BI-WEB", "BI-API", "ERP-WEB", "ERP-API", "CRM-WEB", "CRM-API", "EOFFICE-WEB", "EOFFICE-API"], 
                ['','','','','','','','','','',''],
                ['','','','','','','','','','','']], dtype=object)
class ChoicePro:
    def __init__(self):
        pass
    def showChoice(self):
        for sp in arr[0]:
            rows, cols = np.where(arr == sp)
            if arr[1][cols] != "":
                print("Ban da chon san pham "+sp+" voi so lan cai:",arr[1][cols[0]])
    def slProduct(self, sp):
        while True:
            sl = ""
            sl = input(f"Vui long nhap so luong muon cai cho {sp} (Mac dinh la 1): ")
            if sl == '': sl = '1'; return sl
            elif sl.isdecimal(): 
                if sl <= '0': sl = '1'; return sl; break 
                else: return str(sl); break
            else: print('Ban nhap khong dung. Vui long nhap lai')
    def choices(self):
        number = 0
        for a in arr[0]:
            number += 1
            print (str(number) + ". " + a, end="   ")
        choices = list(map(str, input('\nNhap cac san pham can cai phan cach bang dau , (Nhap 0 đe ket thuc): ').split(',')))
        for choice in choices:
            index = choices.index(choice)
            while True:
                match choice:
                    case "0": break
                    case "1": print("Ban da chon CDN"); num = self.slProduct(arr[0][0]); arr[1][0] = num; arr[2][0] = 'cdn-api'; break
                    case "2": print("Ban da chon HR-WEB"); num = self.slProduct(arr[0][1]); arr[1][1] = num; arr[2][0] = 'dhr-api&dhr-web6'; break
                    case "3": print("Ban da chon HR-API"); num = self.slProduct(arr[0][2]); arr[1][2] = num; arr[2][0] = 'dhr-api'; break
                    case "4": print("Ban da chon BI-WEB"); num = self.slProduct(arr[0][3]); arr[1][3] = num; arr[2][0] = 'bi-api&bi-web'; break
                    case "5": print("Ban da chon BI-API"); num = self.slProduct(arr[0][4]); arr[1][4] = num; arr[2][0] = 'bi-api';break
                    case "6": print("Ban da chon ERP-WEB"); num = self.slProduct(arr[0][5]); arr[1][5] = num; arr[2][0] = 'lpt-api&erp-web'; break
                    case "7": print("Ban da chon ERP-API"); num = self.slProduct(arr[0][6]); arr[1][6] = num; arr[2][0] = 'lpt-api'; break
                    case "8": print("Ban da chon CRM-WEB"); num = self.slProduct(arr[0][7]); arr[1][7] = num; arr[2][0] = 'crm-api&crm-web'; break
                    case "9": print("Ban da chon CRM-API"); num = self.slProduct(arr[0][8]); arr[1][8] = num; arr[2][0] = 'crm-api'; break
                    case "10": print("Ban da chon EOFFICE-WEB"); num = int(self.slProduct(arr[0][9])); arr[1][9] = num; arr[2][0] = 'dgn-eoffice-api&dgn-eoffice-web'; break
                    case "11": print("Ban da chon EOFFICE-API"); num = int(self.slProduct(arr[0][10])); arr[1][10] = num; arr[2][0] = 'dgn-eoffice-api'; break
                    case _: choice = input(f"Vi tri thu {index + 1} nhap khong dung. Vui long nhap lai hoac nhap 0 de bo qua: ")
        self.showChoice()

c = ChoicePro()
c.choices()

