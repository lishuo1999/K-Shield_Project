#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

red = '\033[1;31m'
yellow = '\033[0;33m'
noclr = '\033[0m'


dir_main = f"{os.environ['HOME']}/K-Shield_D6"
if os.path.isdir(dir_main) == False: 
    subprocess.run([f"mkdir",  dir_main])
dir = f"{os.environ['HOME']}/K-Shield_D6/file"

def printsave(*tmp): #터미널에 문자열 출력시키고 stdout.txt에 출력내용들 저장하는 함수
        file = open(dir + '/stdout.txt', 'a', encoding = 'utf-8')
        print(*tmp) #터미널에 문자열 출력
        print(*tmp, file=file) #문자열 파일에 저장
        file.close()

def make_dir(dir): 
    try:	
        if os.path.isdir(dir) == False: # /usr 존재하지 않을때 mkdir 실행시켜 디렉토리 생성
            subprocess.run([f"mkdir",  dir])  # 수집된 정보들 저장할 디렉토리 생성
            printsave("Making directory to store evidence: " + dir)

    except Exception as err:
        printsave("Error creating directory: ", f"{red}{err}{noclr}")
        return False

#각각 중요 파일의 수정된 정보 수집

logdir="\var\log" #기본 로그 파일
pwddir="\etc\passwd" # 암호화된 파일
netdir="\etc\sysconfig" #네트워크 설정 파일
memdir="\proc\meminfo" # 메모리 관련 정보 파일

	
def important_file_info():

	try: 
		time = datetime.now()
		printsave(f"{yellow}{time}{noclr}" + "  Log File Information")

		subprocess.run('find $logdir -name "*.log" -mtime -3 >>' + dir + '/logfile_info.txt', shell=True)  # 3일 전까지 갱신된 파일 출력
		subprocess.run('find $logdir -mmin -30 -type f -ls >>' + dir + '/logfile_info.txt', shell=True)  # 30분 이내의 수정한 파일 출력

		subprocess.run('find $pwddir -type f -mtime -3 >>' + dir + '/logfile_info.txt', shell=True) 
		subprocess.run('find $pwddir -mmin -30 -type f -ls >>' + dir + '/logfile_info.txt', shell=True) 

		subprocess.run('find $netdir -type f -mtime -3 >>' + dir + '/logfile_info.txt', shell=True) 
		subprocess.run('find $netdir -mmin -30 -type f -ls >>' + dir + '/logfile_info.txt', shell=True) 

		subprocess.run('find $memdir -type f -mtime -3 >>' + dir + '/logfile_info.txt', shell=True) 
		subprocess.run('find $memdir -mmin -30 -type f -ls >>' + dir + '/logfile_info.txt', shell=True) 

	except Exception as e:
		printsave("error: ", f"{red}{e}{noclr}")
		

# 실행권한 또는 특수권한을 가진 파일 정보 수집

def executables_file_info():

	try: 
		time = datetime.now()
		printsave(f"{yellow}{time}{noclr}" + "  Excutables File Information")
	
		# 해시값( 무결성 검사) 를 통해 특수 권한을 가진 파일 찾기
		subprocess.run('find / -type f -perm -o+rx -print0 2>/dev/null | xargs -0 sha1sum >>' + dir + '/Excutables_info.txt', shell=True) 
	except Exception as e:
		printsave(f"{red}{e}{noclr}")


# 숨긴 파일 찾기

def hidden_file_info():

	try: 
		time = datetime.now()
		printsave(f"{yellow}{time}{noclr}" + "  Hidden File Information")

		subprocess.run('find /var -type f -name 2>/dev/null".*" >>' + dir + '/hidden_info.txt', shell=True)  # /var 디렉터린 내 숨긴 파일 찾기
		subprocess.run('find /bin -type f -name 2>/dev/null".*" >>' + dir + '/hidden_info.txt', shell=True)  # /bin 디렉터린 내 숨긴 파일 찾기
		subprocess.run('find /etc -type f -name 2>/dev/null".*" >>' + dir +' /hidden_info.txt', shell=True)  # /etc 디렉터린 내 숨긴 파일 찾기
		subprocess.run('find /proc -type f -name 2>/dev/null".*" >>' + dir + '/hidden_info.txt', shell=True)  # /proc 디렉터린 내 숨긴 파일 찾기

	except Exception as e:
		printsave(f"{red}{e}{noclr}")		
			       
# 열린 파일의 목록 확인


def count_file_info():
	time = datetime.now()
	printsave(f"{yellow}{time}{noclr}" + "----------Open File Information----------")
	
	try:
		
		# /etc/passwd 디렉토리에 속한 파일이 하나 이상 열려 있을 경우, 그 디렉토리에 속한 하위 파일들 모두 출력

		if 'lsof /etc >= 1': 
			subprocess.run('lsof +D /etc 2>/dev/null >' + dir + '/count_file_info.txt', shell=True)
			#f=open(dir + "/count_file_info.txt", 'a', encoding = 'utf-8') # dir=홈 디렉토리, 홈 디렉터리에 .txt 파일 생성해서 계속 추가
			#f.close()

		elif 'lsof \proc >= 1':	
			subprocess.run('lsof +D /proc 2>/dev/null >>' + dir + '/count_file_info.txt', shell=True)
			#f=open(dir + "/count_file_info.txt", 'a', encoding = 'utf-8')
			#f.close()
		else:
			printsave("- Not Found Files") # 디렉토리 안의 해당 파일이 없는 경우 출력

	except Exception as e:
		printsave(f"{red}{e}{noclr}")
		
def main():
	return make_dir(dir), important_file_info(), executables_file_info(), hidden_file_info(), count_file_info()
	       
if __name__ == '__main__':
	main()
