listInfo = []
with open ('CDN.1','r') as f:
    for line in f.readlines():
        listInfo.append(line.split(':'))
    print(listInfo)
    print ('------------------------------------------------------')
listInfo1 = []
with open ('CDN.1','r') as fi:
    for line in fi.read().splitlines():
        listInfo1.append(line.split(':'))
    print(listInfo1)