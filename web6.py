import os, string, random
try:
    import numpy as np
except:
    os.system(f"pip install numpy")
import numpy as np
arr = np.array([['CDN', 'HR-WEB', 'HR-API', "BI-WEB", "BI-API", "ERP-WEB", "ERP-API", "CRM-WEB", "CRM-API", "EOFFICE-WEB", "EOFFICE-API"], 
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
        while True:
            choices = input('\nVui long nhap san pham can cai (Nhap 0 đe ket thuc): ')
            match choices:
                case "0": break
                case "1": print("Ban da chon CDN"); num = self.slProduct(arr[0][0]); arr[1][0] = num
                case "2": print("Ban da chon HR-WEB"); num = self.slProduct(arr[0][1]); arr[1][1] = num
                case "3": print("Ban da chon HR-API"); num = self.slProduct(arr[0][2]); arr[1][2] = num
                case "4": print("Ban da chon BI-WEB"); num = self.slProduct(arr[0][3]); arr[1][3] = num
                case "5": print("Ban da chon BI-API"); num = self.slProduct(arr[0][4]); arr[1][4] = num
                case "6": print("Ban da chon ERP-WEB"); num = self.slProduct(arr[0][5]); arr[1][5] = num
                case "7": print("Ban da chon ERP-API"); num = self.slProduct(arr[0][6]); arr[1][6] = num
                case "8": print("Ban da chon CRM-WEB"); num = self.slProduct(arr[0][7]); arr[1][7] = num
                case "9": print("Ban da chon CRM-API"); num = self.slProduct(arr[0][8]); arr[1][8] = num
                case "10": print("Ban da chon EOFFICE-WEB"); num = int(self.slProduct(arr[0][9])); arr[1][9] = num
                case "11": print("Ban da chon EOFFICE-API"); num = int(self.slProduct(arr[0][10])); arr[1][10] = num
                case _: print("Ban chua chon san pham. Vui long nhap lai")
        self.showChoice()
        
class Info():
    def __init__(self, sp):
        info = np.array([[f"Nhap duong dan chua source cho {sp} (Khong tu tao folder con trong duong dan)", "Nhap duong dan folder chua file index.html(Khong tu tao folder con trong duong dan)", "Nhap duong dan folder uploads", "Nhap ten cho API(vd:"")", "Nhap port cho API(vd:6020)", "Nhap branch name cua san pham", "Nhap link web(vd:https://dgn.com.vn)", "Nhap link api(vd:https://dgn.com.vn/api)", "Nhap ten db mongo cho API", "Nhap companycode", "Nhap duong dan folder cdn cua sp nay(vd:/home/cdn-api)", "Nhap link API-CDN(vd:https://cdgn.com.vn/cdn)", "Nhap secret API-CDN(vd:co 37 ky tu)"],
                     ['','','','','','','','','','','','','',]], dtype=object)
        self.info = info
    def randomSecret(self):
        letters_and_digits = string.ascii_letters + string.digits
        random_string_and_digits=''.join(random.choice(letters_and_digits) for i in range(32))
        return random_string_and_digits
    
    def writeInfo(self, sp, filename):
        print(f"Vui long nhap thong tin cho san pham {sp}")
        for i in self.info[0]:
            x, y = np.where(self.info == i)
            if not (sp == 'CDN' and (y[0] == 1 or y[0] == 5 or y[0] == 9 or y[0] == 10 or y[0] == 11 or y[0] == 12)):
                nhap = input(f"{i}: ")
                self.info[1][y[0]] = nhap
        for i in self.info[0]:
            x, y = np.where(self.info == i)
            if self.info[1][y[0]] != "":
                with open (filename,"a") as f:
                    f.write(f"{i}:{self.info[1][y[0]]}\n")
                    f.close

    def editInfo(self, sp, filename):
        number = 0
        array2D = []
        with open (filename,'r') as f:
            print("------------------------------------------------------------------------------")
            print(f"Thong tin ban da nhap cho san pham {sp}: ")
            for line in f.readlines():
                number += 1
                array2D.append(line.split(':'))
                print(str(number) + "." + line)
            while True:
                numEdit = input("Vui long chon so can chinh sua (Nhap 0 de thoat): ")
                if numEdit == '0': break
                elif numEdit.isdecimal() and numEdit <= str(len(array2D)):
                    num = int(numEdit) - 1
                    value = input(f"{array2D[num][0]}: ")
                    array2D[num][1] = value
                    print(array2D[num][1])
                else: print("Nhap khong dung. Vui long nhap lai.")
c = ChoicePro()
c.choices()
for sp in arr[0]:
    cinfo = Info(sp)
    rows, cols = np.where(arr == sp)
    if arr[1][cols] != "":
        filename = sp + "." + arr[1][cols[0]]
        # cinfo.writeInfo(sp, filename)
        cinfo.editInfo(sp, filename)



        

    
