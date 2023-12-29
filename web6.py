import os, string, random, time, shutil, tempfile
try:
    import numpy as np
except:
    os.system(f"pip install numpy")
import numpy as np
arr = np.array([['CDN', 'HR-WEB', 'HR-API', "BI-WEB", "BI-API", "ERP-WEB", "ERP-API", "CRM-WEB", "CRM-API", "EOFFICE-WEB", "EOFFICE-API"], 
                ['','','','','','','','','','',''],
                ['','','','','','','','','','',''],
                ['','','','','','','','','','','']], dtype=object)
passgit = 'Ltt3mJvFr5uuYqUjWCQY'
cdn_private = cdn_public = secret_cdn = ''
slash = '\\'
temp_f = tempfile.gettempdir()
os.makedirs(f'{temp_f}{slash}value{slash}', exist_ok=True)
temp_f = f'{temp_f}{slash}value{slash}'
#"0.Duong dan chua source cho {sp}", "1.Duong dan folder chua file index.html", "2.Duong dan folder uploads", "3.Nhap ten cho API cho {sp} (vd:{sp})", "4.Nhap port API cho {sp} (vd:7020)", "5.Nhap branch name cua san pham {sp}", "6.Nhap link web(vd:https://dgn.com.vn)", "7.Nhap link api(vd:https://dgn.com.vn/api)", "8.Nhap ten db mongo cho API", "9.Nhap companycode cua san pham {sp}", "10.Nhap link CDN-PRIVATE cho {sp}(vd:https://192.168.1.5/cdn)","11.Nhap link CDN-PUBLIC cho {sp}(vd:https://cdgn.com.vn/cdn)", "12.Nhap secret CDN cho {sp}", "13.San pham nay dung cho link KC hay PRO", "14.Secret cho sp {sp}"]

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
        input_info = np.array([[f"Duong dan chua source cho {sp}", "Duong dan folder chua file index.html", "Duong dan folder uploads", f"Ten API cho {sp} (vd:{sp})", f"Port API cho {sp} (vd:7020)", f"Branch name cua san pham {sp}", f"Link web cua {sp} (vd:https://dgn.com.vn)", f"Link api cua {sp} (vd:https://dgn.com.vn/api)", f"Ten db mongo cho {sp}", f"Companycode cua san pham {sp}", f"Link CDN-PRIVATE cho {sp}(vd:https://192.168.1.5/cdn)",f"Link CDN-PUBLIC cho {sp}(vd:https://cdgn.com.vn/cdn)", f"Secret CDN cho {sp}", "San pham nay dung cho link KC hay PRO", f"Secret cho {sp}"],
                     ['','','','','','','','','','','','','','','']], dtype=object)
        self.sp = sp
        self.filename = filename
    def randomSecret(self):
        letters_and_digits = string.ascii_letters + string.digits
        random_string_and_digits=''.join(random.choice(letters_and_digits) for i in range(32))
        return random_string_and_digits
    def findInfoCDN(self, prefix):
        nameapi = []
        info_cdn_file = []
        for root, dirs, files in os.walk(temp_f):
            for file in files:
                if file.startswith(prefix):  
                    info_cdn_file.append(file)
        for number, i in enumerate(info_cdn_file, 1):
            with open(temp_f + i, 'r') as f:
                for line in f:
                    if 'Ten API cho CDN' in line:
                        nameapi.append(line.split('=')[1])
                        print(f'{number}.{info_cdn_file[number - 1]} voi ten API la \'{(nameapi[number - 1]).strip()}\'')
        nhap = input(f'Vui long chon file thong tin chua CDN se cai cho {sp}: ')
        while True:
            if nhap.isdecimal() and nhap <= str(len(nameapi)) and nhap >= str('1'):
                with open(temp_f + info_cdn_file[int(nhap) - 1], 'r') as f:
                    for line in f:
                        if 'Link CDN-PRIVATE' in line: cdn_private = (line.split('=')[1]).strip()
                        if 'Link CDN-PUBLIC' in line: cdn_public = (line.split('=')[1]).strip()
                        if 'Secret cho CDN' in line: secret_cdn = (line.split('=')[1]).strip()
                return cdn_private, cdn_public, secret_cdn
            else:
                nhap = input('Ban chon chua dung. Vui long chon lai: ')
    def writeInfo(self):
        print("------------------------------------------------------------------------------")
        print(f"Vui long nhap thong tin cho san pham {self.sp}")
        for i in input_info[0]:
            x, y = np.where(input_info == i)
            if 'API' in self.sp and y[0] == 1:
                pass
            elif not (self.sp == 'CDN' and (y[0] == 1 or y[0] == 5 or y[0] == 6 or y[0] == 7 or y[0] == 9 or y[0] == 12 or y[0] == 13) or y[0] == 14):
                if y[0] == 13:
                    linkstatus = ['PRO', 'KC']
                    while True:
                        nhap = input(f"{i}: ").upper()
                        if nhap in linkstatus:
                            input_info[1][y[0]] = nhap
                            break
                        else:
                            print('Chi nhap kc hoac pro')
                elif y[0] == 3:
                    nhap = input(f"{i}: ").upper()
                    input_info[1][y[0]] = nhap
                elif self.sp != 'CDN' and (y[0] == 10 or y[0] == 11 or y[0] == 12):
                    if y[0] == 10:
                        cdn_private, cdn_public, secret_cdn = self.findInfoCDN('CDN')
                        input_info[1][10] = cdn_private; input_info[1][11] = cdn_public; input_info[1][12] = secret_cdn
                    else:
                        pass
                else:
                    nhap = input(f"{i}: ")
                    input_info[1][y[0]] = nhap
            else:
                if self.sp == 'CDN':
                    input_info[1][5] = 'production'; input_info[1][14] = self.randomSecret()
                else:
                    input_info[1][14] = self.randomSecret()
        with open (self.filename,"w") as f:
            for i in input_info[0]:
                x, y = np.where(input_info == i)
                f.write(f"{i}={input_info[1][y[0]]}\n")
                f.close
    def readInfo(self):
        listInfo = []
        with open (self.filename,'r') as f:
            for line in f.read().splitlines():
                listInfo.append(line.split('='))
        if self.sp != 'CDN' and listInfo[10][1] == '':
                cdn_private, cdn_public, secret_cdn = self.findInfoCDN('CDN')
                listInfo[10][1] = cdn_private; listInfo[11][1] = cdn_public; listInfo[12][1] = secret_cdn
        return listInfo   
    def showInfo(self):
        listInfo = self.readInfo()
        numarr = []
        print("------------------------------------------------------------------------------")
        print(f"Thong tin moi nhat cua san pham {sp}")
        for number, i in enumerate(listInfo, 1):
            if i[1] != '':
                print (f'{number}.{i[0]}: {i[1]}')
                numarr.append(str(number))
        return listInfo, numarr   
    def editInfo(self, listInfo, numarr):
        numEdit = list(map(str, input("\nNhap cac so can chinh sua phan cach bang dau , (Nhap 0 de thoat): ").split(',')))
        for nums in numEdit:
            index = numEdit.index(nums)
            while True:    
                if nums == '0': break
                elif nums.isdecimal() and nums in numarr:
                    num = int(nums) - 1
                    value = input(f"{listInfo[num][0]}: ")
                    if nums == '14' or nums == '4':
                        value = value.upper()
                    listInfo[num][1] = value
                    break
                else:
                    nums = input(f"Vi tri thu {index + 1} nhap khong dung. Vui long nhap lai hoac nhap 0 de bo qua: ")
        with open(self.filename, 'w') as f:
            for i in listInfo:
                f.write("=".join(str(x) for x in i)+ "\n")   
class replaceEnv():
    def __init__(self, listInfo, sp):
        self.listInfo = listInfo; self.sp = sp
    def createFolder(self):
        if self.sp == 'CDN' or 'API' in self.sp:
            try: os.makedirs(self.listInfo[0][1], exist_ok=True);os.makedirs(self.listInfo[2][1], exist_ok=True)
            except: print('Khong tao duoc folder')
        else: 
            try: os.makedirs(self.listInfo[0][1], exist_ok=True);os.makedirs(self.listInfo[1][1], exist_ok=True);os.makedirs(self.listInfo[2][1], exist_ok=True)
            except: print('Khong tao duoc folder')
    def gitCode(self):
        giturl = arr[2][cols[0]].split('&')[0]
        if not os.path.exists(f'{self.listInfo[0][1]}{slash}{giturl}'):
            os.system(f"git clone https://ptecdgn:{passgit}@bitbucket.org/diginetvn/{giturl} {self.listInfo[0][1]}{slash}{giturl}")
            if len(arr[2][cols[0]].split('&')) > 1:
                giturl = arr[2][cols[0]].split('&')[1]
                os.system(f"git clone https://ptecdgn:{passgit}@bitbucket.org/diginetvn/{giturl} {self.listInfo[0][1]}{slash}{giturl}")
        if self.sp == 'HR-WEB' and not os.path.exists(f'{self.listInfo[0][1]}{slash}hrm-ui'):
            os.system(f"git clone https://ptecdgn:{passgit}@bitbucket.org/diginetvn/hrm-ui {self.listInfo[0][1]}{slash}hrm-ui")
    def createVar(self, giturl):
        link_web_cut = '/'.join(self.listInfo[6][1].split('/')[3:])
        if giturl != 'hrm-ui':
            if link_web_cut == '':
                react_app_root = '/'
            else:
                react_app_root = f'/{link_web_cut}/'
        else:
            listInfo[6][1] = f'{listInfo[6][1]}/hrm'
            if link_web_cut == '':
                react_app_root = '/hrm/'
            else:
                react_app_root = f'/{link_web_cut}/hrm/'
        return react_app_root, listInfo[6][1]
    def replaceApi(self):
        if self.sp == 'CDN': node_evn = 'production'
        else: node_evn = 'development'
        bien_process = ['name', 'NODE_PORT', f"{arr[3][cols[0]]}_SECRET", f"{arr[3][cols[0]]}_UPLOAD_DIR", f"{arr[3][cols[0]]}_UPLOAD_URL", f"{arr[3][cols[0]]}_API_URL", f"{arr[3][cols[0]]}_WEB_URL", f"{arr[3][cols[0]]}_DATABASE_NAME", f"{arr[3][cols[0]]}_TRACKING_BRANCH", 'max_memory_restart', 'CDN_API_URL', 'CDN_API_SECRET', 'NODE_ENV', 'CDN_URL_INTERNAL', 'CDN_URL_PUBLIC']
        bien_process2 = [self.listInfo[3][1],self.listInfo[4][1],self.listInfo[14][1],self.listInfo[2][1],f'{self.listInfo[6][1]}/uploads',self.listInfo[7][1],self.listInfo[6][1],self.listInfo[8][1],self.listInfo[5][1],'2000M',self.listInfo[11][1],self.listInfo[12][1],node_evn,self.listInfo[10][1],self.listInfo[11][1]] 
        giturl = arr[2][cols[0]].split('&')[0]
        file_process = f"{self.listInfo[0][1]}{slash}{giturl}{slash}process.json"
        os.chdir(f"{self.listInfo[0][1]}{slash}{giturl}")
        os.system(f"git fetch && git checkout {self.listInfo[5][1]}")
        shutil.copyfile('process.json.copy','process.json')
        for index,i in enumerate(bien_process,0):
            with open(file_process, 'r+') as jsonFile:
                lines = jsonFile.readlines()
            new_lines=[]
            for line in lines:
                if i in line:
                    a = line.split('"')[3]
                    new_line = line.replace(a, bien_process2[index])
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)
            with open(file_process, 'w') as jsonFile:
                jsonFile.writelines(new_lines)
    def replaceUI(self, giturl):
        react_app_root, listInfo[6][1] = self.createVar(giturl)
        bien_env=['REACT_APP_ROOT', 'REACT_APP_API', 'REACT_APP_WEB', 'REACT_APP_SECRET', 'REACT_APP_CDN_URL', 'REACT_APP_CDN_SECRET', 'REACT_APP_COMPANYCODE', 'REACT_APP_ENV', 'GENERATE_SOURCEMAP']
        bien_env2=[f"{react_app_root}", f"{listInfo[7][1]}", f"{listInfo[6][1]}", f"{listInfo[14][1]}", f"{listInfo[11][1]}", f"{listInfo[12][1]}", f"{listInfo[9][1]}", f"{listInfo[13][1]}", 'false']
        file_env = f"{self.listInfo[0][1]}{slash}{giturl}{slash}.env"
        os.chdir(f"{self.listInfo[0][1]}{slash}{giturl}")
        os.system(f"git fetch && git checkout {self.listInfo[5][1]}")
        shutil.copyfile('.env.copy','.env')
        for index,i in enumerate(bien_env,0):
            with open(file_env, 'r+') as envFile:
                lines = envFile.readlines()
            new_lines=[]
            for line in lines:
                if i in line:
                    a = line.split('=')[1]
                    new_line = line.replace(a, bien_env2[index])
                    new_lines.append(new_line + '\n')
                else:
                    new_lines.append(line)
            with open(file_env, 'w') as jsonFile:
                jsonFile.writelines(new_lines)
class setup():
    def __init__(self, listInfo):
        self.listInfo = listInfo
    def setupAPI(self):
        os.chdir(f"{self.listInfo[0][1]}{slash}{giturl}")
        os.system('npm install & npm install upath & pm2 start process.json & ')


c = ChoiceSP()
c.choices()
for sp in arr[0]:
    rows, cols = np.where(arr == sp)
    if arr[1][cols[0]] != "":
        for i in range(int(arr[1][cols[0]])):
            filename = f'{temp_f}{sp}.{str(i)}'
            cinfo = Info(sp, filename)
            if not os.path.exists(filename):
                cinfo.writeInfo()
for sp in arr[0]:
    rows, cols = np.where(arr == sp)
    if arr[1][cols[0]] != "":
        for i in range(int(arr[1][cols[0]])):
            filename = f'{temp_f}{sp}.{str(i)}'
            cinfo = Info(sp, filename)
            listInfo, numarr = cinfo.showInfo()
            cinfo.editInfo(listInfo, numarr)
            creplace = replaceEnv(listInfo, sp)
            creplace.createFolder()
for sp in arr[0]:
    rows, cols = np.where(arr == sp)
    if arr[1][cols[0]] != "":
        for i in range(int(arr[1][cols[0]])):
            filename = f'{temp_f}{sp}.{str(i)}'
            cinfo = Info(sp, filename)
            listInfo = cinfo.readInfo()
            creplace = replaceEnv(listInfo, sp)
            creplace.gitCode()
            creplace.replaceApi()
            if not 'API' in sp and sp != 'CDN':
                giturl = arr[2][cols[0]].split('&')[1]
                creplace.replaceUI(giturl)
                if sp == 'HR-WEB':
                    giturl = 'hrm-ui'
                    creplace.replaceUI(giturl)


            
