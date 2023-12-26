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

class ChoicePro:
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
        input_info = np.array([[f"Duong dan chua source cho {sp}", "Duong dan folder chua file index.html", "Duong dan folder uploads", f"Nhap ten cho API cho {sp} (vd:{sp})", f"Nhap port API cho {sp} (vd:7020)", f"Nhap branch name cua san pham {sp}", "Nhap link web(vd:https://dgn.com.vn)", "Nhap link api(vd:https://dgn.com.vn/api)", "Nhap ten db mongo cho API", f"Nhap companycode cua san pham {sp}", f"Nhap duong dan folder cdn cho {sp}(vd:/home/cdn-api)", "Nhap link API-CDN(vd:https://cdgn.com.vn/cdn)", "Nhap secret API-CDN(vd:co 37 ky tu)"],
                     ['','','','','','','','','','','','','',]], dtype=object)
        self.info = input_info
        self.sp = sp
        self.filename = filename

    def randomSecret(self):
        letters_and_digits = string.ascii_letters + string.digits
        random_string_and_digits=''.join(random.choice(letters_and_digits) for i in range(32))
        return random_string_and_digits
    
    def writeInfo(self):
        print("------------------------------------------------------------------------------")
        print(f"Vui long nhap thong tin cho san pham {self.sp}")
        for i in self.info[0]:
            x, y = np.where(self.info == i)
            if not (self.sp == 'CDN' and (y[0] == 1 or y[0] == 5 or y[0] == 9 or y[0] == 10 or y[0] == 11 or y[0] == 12)):
                nhap = input(f"{i}: ")
                self.info[1][y[0]] = nhap
        with open (self.filename,"w") as f:
            for i in self.info[0]:
                x, y = np.where(self.info == i)
                if self.info[1][y[0]] != '':
                    f.write(f"{i}={self.info[1][y[0]]}\n")
                    f.close

    def editInfo(self):
        number = 0
        listInfo = []
        with open (self.filename,'r') as f:
            print("------------------------------------------------------------------------------")
            print(f"Thong tin ban da nhap cho san pham {self.sp}: ")
            for line in f.read().splitlines():
                number += 1
                listInfo.append(line.split('='))
                print(f"{number}.{line.split('=')[0]}: {line.split('=')[1]}")
            numEdit = list(map(str, input("\nNhap cac so can chinh sua phan cach bang dau , (Nhap 0 de thoat): ").split(',')))
            for nums in numEdit:
                index = numEdit.index(nums)
                while True:    
                    if nums == '0': break
                    elif nums.isdecimal() and nums <= str(len(listInfo)):
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
                print(f"{number}.{line.split('=')[0]}: {line.split('=')[1]}")
        return listInfo

class GetVarAndCrtFolder():
    def __init__(self, filename, sp, spApi):
        self.filename = filename ; self.sp = sp; self.spApi = spApi

    def SearchStr(self,word):
         with open(self.filename, 'r') as file:
             lines = file.readlines()
             for line in lines:
                 if line.find(word) != -1:
                    var = line.split('=')
                    return var[1].strip()
    def getVarInFile(self):
        global name_api, port_api, branch, link_web
        # for i in input_info[0]:
        #     print(i)

    def createFolder(self):
        with open(self.filename, 'r') as f:
            global dirsource, diruploads, diruploads
            if self.sp == ('CDN' or self.spApi):
                dirsource = self.SearchStr('Duong dan chua source cho')
                diruploads = self.SearchStr('Duong dan folder uploads')
                try: os.makedirs(dirsource, exist_ok=True);os.makedirs(diruploads, exist_ok=True)
                except: print('Khong tao duoc folder')
            else: 
                dirsource = self.SearchStr('Duong dan chua source cho')
                diruploads = self.SearchStr('Duong dan folder uploads')
                dirindex = self.SearchStr('Duong dan folder chua file index.html')
                try: os.makedirs(dirsource, exist_ok=True);os.makedirs(diruploads, exist_ok=True);os.makedirs(dirindex, exist_ok=True)
                except: print('Khong tao duoc folder')
        self.getVarInFile()
class ReplaceFile():
    passgit = 'Ltt3mJvFr5uuYqUjWCQY'
    def __init__(self, filename, cols):
        self.api = arr[2][cols[0]].split('&')
        self.sp_env = arr[3][cols[0]]

    def replaceFile(self, replace_file, search_str, old_str, new_str):
        with open(replace_file, 'r') as f:
            lines = f.readlines()
        new_lines = []
        for line in lines:
            if search_str in line:
                new_line = line.replace(old_str, new_str)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        with open(replace_file, 'w') as f:
            f.writelines(new_lines)
    def file(self):
        bien_process=["name", "NODE_PORT", f"{self.sp_env}_SECRET", f"{self.sp_env}_UPLOAD_DIR", f"{self.sp_env}_UPLOAD_URL", f"{self.sp_env}_API_URL", f"{self.sp_env}_WEB_URL", "${arrinput[15]}_DATABASE_NAME", f"{self.sp_env}_TRACKING_BRANCH", "max_memory_restart", "CDN_API_URL", "CDN_API_SECRET", "NODE_ENV", "CDN_URL_INTERNAL", "CDN_URL_PUBLIC"]


    def configApi(self):
        os.system(f"git clone https://ptecdgn:{self.passgit}@bitbucket.org/diginetvn/{self.api[0]} {dirsource}\{self.api[0]}")
        os.chdir(f"{dirsource}\{self.api[0]}")
        if self.sp == 'CDN':
            os.system(f"git fetch && git checkout production")
        else:
            os.system(f"git fetch && git checkout development")
        shutil.copyfile('process.json.copy','process.json')

c = ChoicePro()
c.choices()
# for sp in arr[0]:
#         rows, cols = np.where(arr == sp)
#         if arr[1][cols] != "":
#             for i in range(int(arr[1][cols[0]])):
#                 filename = sp + "." + str(i)
#                 cinfo = Info(sp, filename)
#                 if not os.path.exists(filename):
#                     cinfo.writeInfo()
#                     cinfo.editInfo()
#                 else:
#                     cinfo.editInfo()
                    
# for sp in arr[0]:
#         rows, cols = np.where(arr == sp)
#         if arr[1][cols] != "":
#             for i in range(int(arr[1][cols[0]])):
#                 filename = sp + "." + str(i)
#                 cinfo = Info(sp, filename)
#                 listInfo = cinfo.showInfo()

for sp in arr[0]:
        spApi = sp[-3:]
        rows, cols = np.where(arr == sp)
        var = arr[1][cols[0]]
        if var != "":
            for i in range(int(var)):
                filename = sp + "." + str(i)
                gvar_ctrf = GetVarAndCrtFolder(filename, sp, spApi)
                gvar_ctrf.getVarInFile()
                # spConfig.configApi()
                

