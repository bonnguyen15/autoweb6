import os, time
import numpy as np
import tempfile, shutil
# slash = '\\'
# temp_f = tempfile.gettempdir()
# bien_env=['REACT_APP_ROOT', 'REACT_APP_API', 'REACT_APP_WEB', 'REACT_APP_SECRET', 'REACT_APP_CDN_URL', 'REACT_APP_CDN_SECRET', 'REACT_APP_COMPANYCODE', 'REACT_APP_ENV', 'GENERATE_SOURCEMAP']
# bien_env2=["/", "http://168.168.2.19/hr-pro", "http://168.168.2.19", "fefefefefv3454fewf", "http://168.168.2.19/cdn-api", "ferwgfwefce342354gvfvd", "demo", "PRO", 'false']
# file_env = "D:\web\hr-pro\dhr-web6\.env"
# for index,i in enumerate(bien_env,0):
#     with open(file_env, 'r+') as envFile:
#         lines = envFile.readlines()
#     new_lines=[]
#     for line in lines:
#         if i in line:
#             a = line.split('=')[1]
#             new_line = line.replace(a, bien_env2[index])
#             new_lines.append(new_line + '\n')
#         else:
#             new_lines.append(line)
#     with open(file_env, 'w') as jsonFile:
#         jsonFile.writelines(new_lines)
a = 'D:\web'
b = 'D:\web\public'
c = 'demo'
d = 'http://168.168.2.19'
text = ['','','','','']
text[0] = '''#!/bin/bash
#Cac thong tin can thay the
dirsourcecode='''+ a
text[1] = 'dirweb='+ b
text[2] = 'branch='+ c
text[3] = 'HP_REPLACE=' + d
text[4] = '''runWithDelay () {
    sleep $1;
    shift;
    "${@}";
}

#UPDATE API
update_api () {
if [ -d "$dirsourcecode/$1" ]; then
	cd $dirsourcecode/$1
	echo "Go to root API folder: $dirsourcecode/$1"
	git branch
	git status
	git reset --hard origin/$branch
	git pull https://ptecdgn:$2@bitbucket.org/diginetvn/$1.git $branch
	if [ $? -ne 0 ]; then
		echo "DGN_UPGRADE_ERR Cai dat $1 bi loi" >&2
		exit 1
	fi
	rm -rf package-lock.json node_modules
	sleep 5
	npm install
	if [ $? -ne 0 ]; then
		echo "DGN_UPGRADE_ERR Cai dat $1 bi loi" >&2
		exit 1
	fi
	runWithDelay 15 pm2 restart process.json &
else
	echo $1 chua duoc cai dat
	exit
fi
}

#UPDATE UI
update_ui () {
if [ -d "$dirsourcecode/$1" ]; then
	cd $dirsourcecode/$1
	echo "Go to root WEB folder: $dirsourcecode/$1"
	git branch
	git reset --hard origin/$branch
	git pull https://ptecdgn:$2@bitbucket.org/diginetvn/$1.git $branch
	if [ $? -ne 0 ]; then
		echo "DGN_UPGRADE_ERR Cai dat $1 bi loi" >&2
		exit 1
	fi
	#Install code
	sleep 5
	npm run freshtall
	if [ $? -ne 0 ]; then
		echo "DGN_UPGRADE_ERR Cai dat $1 bi loi" >&2
		exit 1
	fi
	# Update homepage
	if [ $1 = hrm-ui ]; then
		if grep -q 'homepage' package.json
		then
			sed -i "s|http.*|${HP_REPLACE}/hrm\",|g" package.json
		else
			sed -i "5 i \ \ \ \ \"homepage\": \"${HP_REPLACE}/hrm\"," package.json
		fi
		dirweb=$dirweb/hrm
	else
		if grep -q 'homepage' package.json
		then
			sed -i "s|http.*|${HP_REPLACE}\",|g" package.json
		else
			sed -i "5 i \ \ \ \ \"homepage\": \"${HP_REPLACE}\"," package.json
		fi
	fi
	#Run build code
	export NODE_OPTIONS=--max_old_space_size=8192
	sleep 5
	npm run build
	if [ $? -ne 0 ]; then
		echo "DGN_UPGRADE_ERR Cai dat $1 bi loi" >&2
		exit 1
	fi
	cp -Rf build/* $dirweb
else
	echo $1 chua duoc cai dat
	exit
fi
}

update_hrjob () {
if [ -d "$dirsourcecode/$1" ]; then
	cd $dirsourcecode/$1
	echo "Go to root WEB folder: $dirsourcecode/dhr-job"
	git branch
	git reset --hard origin/$branch
	git pull https://ptecdgn:$2@bitbucket.org/diginetvn/$1.git $branch
	if [ $? -ne 0 ]; then
		echo "DGN_UPGRADE_ERR Cai dat $1 bi loi" >&2
		exit 1
	fi
	export COMPOSER_ALLOW_SUPERUSER=1;
	if [ -e composer.lock ]; then
		rm -f composer.lock
	fi
	yes | composer install
	yes | composer dumpautoload
else
	echo $1 chua duoc cai dat
	exit
fi
}

input=$1
last_3_chars="${input:${#input}-3}"
	if [ "$last_3_chars" = "api" ]; then
		update_api $1 $2
	elif [ $1 = dhr-job ]; then
		update_hrjob $1 $2
	else 
		update_ui $1 $2
	fi
	echo "Finished successfully"
exit'''
textall = "\n".join(text)
with open('van_ban.txt', 'w') as f:
    f.write(textall)

    