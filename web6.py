import os, string, random, time, shutil, json
from collections import OrderedDict
try:
    import numpy as np
except:
    os.system(f"pip install numpy")
import numpy as np
arr = np.array([['CDN', 'HR-WEB', 'HR-API', "BI-WEB", "BI-API", "ERP-WEB", "ERP-API", "CRM-WEB", "CRM-API", "EOFFICE-WEB", "EOFFICE-API"], 
                ['','','','','','','','','','',''],
                ['','','','','','','','','','',''],
                ['','','','','','','','','','','']], dtype=object)
#"0.Duong dan chua source cho {sp}", "1.Duong dan folder chua file index.html", "2.Duong dan folder uploads", "3.Nhap ten cho API cho {sp} (vd:{sp})", "4.Nhap port API cho {sp} (vd:7020)", "5.Nhap branch name cua san pham {sp}", "6.Nhap link web(vd:https://dgn.com.vn)", "7.Nhap link api(vd:https://dgn.com.vn/api)", "8.Nhap ten db mongo cho API", "9.Nhap companycode cua san pham {sp}", "10.Nhap duong dan folder cdn cho {sp}(vd:/home/cdn-api)", "11.Nhap link CDN-PRIVATE cho {sp}(vd:https://192.168.1.5/cdn)","12.Nhap link CDN-PUBLIC cho {sp}(vd:https://cdgn.com.vn/cdn)", "13.Nhap secret CDN cho {sp}", "14.San pham nay dung cho link KC hay PRO", "15.Secret cho sp {sp}"]

class ChoiceSP:
    def __init__(self):
        pass
    def showChoice(self):
        for sp in arr[0]:
            rows, cols = np.where(arr == sp)
            if arr[1][cols[0]] != "":
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
                    case "1": print("Ban da chon CDN"); num = self.slProduct(arr[0][0]); arr[1][0] = num; arr[2][0] = 'cdn-api'; arr[3][0] = 'CDN'; break
                    case "2": print("Ban da chon HR-WEB"); num = self.slProduct(arr[0][1]); arr[1][1] = num; arr[2][1] = 'dhr-api&dhr-web6'; arr[3][1] = 'DHR'; break
                    case "3": print("Ban da chon HR-API"); num = self.slProduct(arr[0][2]); arr[1][2] = num; arr[2][2] = 'dhr-api'; arr[3][2] = 'DHR'; break
                    case "4": print("Ban da chon BI-WEB"); num = self.slProduct(arr[0][3]); arr[1][3] = num; arr[2][3] = 'bi-api&bi-web'; arr[3][3] = 'BI'; break
                    case "5": print("Ban da chon BI-API"); num = self.slProduct(arr[0][4]); arr[1][4] = num; arr[2][4] = 'bi-api'; arr[3][4] = 'BI'; break
                    case "6": print("Ban da chon ERP-WEB"); num = self.slProduct(arr[0][5]); arr[1][5] = num; arr[2][5] = 'lpt-api&erp-web'; arr[3][5] = 'ERP'; break
                    case "7": print("Ban da chon ERP-API"); num = self.slProduct(arr[0][6]); arr[1][6] = num; arr[2][6] = 'lpt-api'; arr[3][6] = 'ERP'; break
                    case "8": print("Ban da chon CRM-WEB"); num = self.slProduct(arr[0][7]); arr[1][7] = num; arr[2][7] = 'crm-api&crm-web'; arr[3][7] = 'CRM'; break
                    case "9": print("Ban da chon CRM-API"); num = self.slProduct(arr[0][8]); arr[1][8] = num; arr[2][8] = 'crm-api'; arr[3][8] = 'CRM'; break
                    case "10": print("Ban da chon EOFFICE-WEB"); num = int(self.slProduct(arr[0][9])); arr[1][9] = num; arr[2][9] = 'dgn-eoffice-api&dgn-eoffice-web'; arr[3][9] = 'EOFFICE'; break
                    case "11": print("Ban da chon EOFFICE-API"); num = int(self.slProduct(arr[0][10])); arr[1][10] = num; arr[2][10] = 'dgn-eoffice-api'; arr[3][10] = 'EOFFICE'; break
                    case _: choice = input(f"Vi tri thu {index + 1} nhap khong dung. Vui long nhap lai hoac nhap 0 de bo qua: ")
        self.showChoice()

class Info(): 
    def __init__(self, sp, filename):
        global input_info
        input_info = np.array([[f"Duong dan chua source cho {sp}", "Duong dan folder chua file index.html", "Duong dan folder uploads", f"Nhap ten cho API cho {sp} (vd:{sp})", f"Nhap port API cho {sp} (vd:7020)", f"Nhap branch name cua san pham {sp}", "Nhap link web(vd:https://dgn.com.vn)", "Nhap link api(vd:https://dgn.com.vn/api)", "Nhap ten db mongo cho API", f"Nhap companycode cua san pham {sp}", f"Nhap duong dan folder cdn cho {sp}(vd:/home/cdn-api)", f"Nhap link CDN-PRIVATE cho {sp}(vd:https://192.168.1.5/cdn)",f"Nhap link CDN-PUBLIC cho {sp}(vd:https://cdgn.com.vn/cdn)", f"Nhap secret CDN cho {sp}", "San pham nay dung cho link KC hay PRO", f"Secret cho sp {sp}"],
                     ['','','','','','','','','','','','','','','','']], dtype=object)
        self.sp = sp
        self.filename = filename

    def randomSecret(self):
        letters_and_digits = string.ascii_letters + string.digits
        random_string_and_digits=''.join(random.choice(letters_and_digits) for i in range(32))
        return random_string_and_digits
    
    def findSecretCDN(self, cdn_file):
        with open(cdn_file,'r') as f:
            for line in f:
                if 'CDN_URL_INTERNAL' in line:
                    a = line.split('"')[3]
                if 'CDN_URL_PUBLIC' in line:
                    b = line.split('"')[3]
                if 'CDN_SECRET' in line:
                    c = line.split('"')[3]
        return a,b,c
                    
    def writeInfo(self):
        print("------------------------------------------------------------------------------")
        print(f"Vui long nhap thong tin cho san pham {self.sp}")
        for i in input_info[0]:
            x, y = np.where(input_info == i)
            if not (self.sp == 'CDN' and (y[0] == 5 or y[0] == 9 or y[0] == 10 or y[0] == 11 or y[0] == 12 or y[0] == 13 or y[0] == 14) or y[0] == 15):
                if y[0] == 14:
                    linkstatus = ['PRO', 'KC']
                    while True:
                        nhap = input(f"{i}: ").upper()
                        if nhap in linkstatus:
                            input_info[1][y[0]] = nhap
                            break
                        else:
                            print('Chi nhap kc hoac pro')
                elif y[0] == 11 or 12 or 13:
                    if input_info[1][10] != '':
                        while True:
                            if os.path.isfile(f'{input_info[1][10]}\process.json'):
                                file_cdn = f'{input_info[1][10]}\process.json'
                                cdn_private, cdn_public, secret_cdn = self.findSecretCDN(file_cdn)
                                input_info[1][11] = cdn_private; input_info[1][12] = cdn_public; input_info[1][13] = secret_cdn
                                break
                            elif nhap == '0':
                                break
                            else:
                                nhap = input(f"Khong tim thay folder CDN, Vui long nhap lai hoac nhap 0 de thoat: ")
                                input_info[1][10] = nhap
                    else:
                        nhap = input(f"{i}: ")
                        input_info[1][y[0]] = nhap
                else:
                    nhap = input(f"{i}: ")
                    input_info[1][y[0]] = nhap
            else:
                if self.sp == 'CDN':
                    input_info[1][5] = 'production'; input_info[1][15] = self.randomSecret()
                else:
                    input_info[1][5] = 'development'; input_info[1][15] = self.randomSecret()
        with open (self.filename,"w") as f:
            for i in input_info[0]:
                x, y = np.where(input_info == i)
                f.write(f"{i}={input_info[1][y[0]]}\n")
                f.close

    def editInfo(self):
        listInfo = []
        with open (self.filename,'r') as f:
            print("------------------------------------------------------------------------------")
            print(f"Thong tin ban da nhap cho san pham {self.sp}: ")
            numarr = []
            for number, line in enumerate(f.read().splitlines(), 1):
                listInfo.append(line.split('='))
                if line.split('=')[1] != '':
                    numarr.append(number)
                    print(f"{number}.{line.split('=')[0]}: {line.split('=')[1]}")
            numEdit = list(map(str, input("\nNhap cac so can chinh sua phan cach bang dau , (Nhap 0 de thoat): ").split(',')))
            for nums in numEdit:
                index = numEdit.index(nums)
                while True:    
                    if nums == '0': break
                    elif nums.isdecimal() and nums <= str(len(listInfo)) and nums in numarr:
                        num = int(nums) - 1
                        value = input(f"{listInfo[num][0]}: ")
                        listInfo[num][1] = value
                        break
                    else:
                        nums = input(f"Vi tri thu {index + 1} nhap khong dung. Vui long nhap lai hoac nhap 0 de bo qua: ")
        with open(self.filename, 'w') as f:
            for i in listInfo:
                f.write("=".join(str(x) for x in i)+ "\n")

    def showInfo(self):
        print("------------------------------------------------------------------------------")
        print(f"Thong tin moi nhat cua san pham {sp}")
        number = 0
        listInfo = []
        with open (self.filename,'r') as f:
            for line in f.read().splitlines():
                number += 1
                listInfo.append(line.split('='))
                if line.split('=')[1] != '':
                    print(f"{number}.{line.split('=')[0]}: {line.split('=')[1]}")
        return listInfo
c = ChoiceSP()
c.choices()
for sp in arr[0]:
    rows, cols = np.where(arr == sp)
    if arr[1][cols[0]] != "":
        for i in range(int(arr[1][cols[0]])):
            filename = sp + "." + str(i)
            cinfo = Info(sp, filename)
            cinfo.writeInfo()
            cinfo.editInfo()
            # if not os.path.exists(filename):
            #     cinfo.writeInfo()
            #     cinfo.editInfo()
            # else:
            #     cinfo.editInfo()

