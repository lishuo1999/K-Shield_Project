#!/bin/python3

from __future__ import print_function
from collections import OrderedDict
import subprocess
import os,sys
import pprint
from datetime import datetime

red = '\033[1;31m'
yellow = '\033[0;33m'
noclr = '\033[0m'

dir_main = f"{os.environ['HOME']}/K-Shield_D6"
if os.path.isdir(dir_main) == False: 
    subprocess.run([f"mkdir",  dir_main])
dir=f"{os.environ['HOME']}/K-Shield_D6/proc"

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
        printsave("Error creating directory: ",f"{red}{err}{noclr}")
        return False
make_dir(dir)

#시스템에 동작중인 모든 프로세스 소유자 정보 출력
def ps_aux():
    #subprocess.call('ps aux', shell=True)
    time = datetime.now()
    printsave( f"{yellow}{time}{noclr}" + " Collecting Process Info via ps aux command ...")

    subprocess.call('ps aux >' + dir + '/ps_aux_result.txt', shell=True) #명령어 실행 결과 ps_aux_result.txt 파일로 저장
ps_aux()

#부모 프로세스와 자식 프로세스 확인
def ps_ef():
    #subprocess.call('ps -ef', shell=True)
    time = datetime.now()
    printsave( f"{yellow}{time}{noclr}" + " Collecting Process Info via ps -ef command ...")
    
    subprocess.call('ps -ef >'  + dir + '/ps_ef_result.txt', shell=True) #명령어 실행 결과 ps_ef_result.txt 파일로 저장
ps_ef()

#실행되는 task 유동적 관찰, 실시간 os 상태 줄력
def top():
    process = os.popen('top -n 1')
    preprocessed = process.read()
    process.close()
     #명령어 실행 결과 top_result.txt 파일로 저장
    output =  dir +'/top_result.txt'
    fout = open(output,'w')
    fout.write(preprocessed)
    fout.close()
    time = datetime.now()
    printsave( f"{yellow}{time}{noclr}" + " Collecting Process Info via top -n 1 command ...")
    
top()

#Filename:CPU1.py
#Filename:meminfo.py

#프로세서 정보 출력, cpu에 관련된 다양한 정보 출력
def CPUinfo():
    CPUinfo=OrderedDict() #dictionary 순서보장
    procinfo=OrderedDict()
    nprocs = 0
    with open('/proc/cpuinfo') as f:
        for line in f:
            if not line.strip():
                #end of one processor
                CPUinfo['proc%s' % nprocs]=procinfo
                nprocs = nprocs+1
                #Reset
                procinfo=OrderedDict()
            else:   
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return CPUinfo

if __name__ == '__main__':
    CPUinfo = CPUinfo()
    for processor in CPUinfo.keys():
        time = datetime.now()
        printsave( f"{yellow}{time}{noclr}" + " Collecting Process Info via CPUinfo command ...")
        
         #명령어 실행 결과 CPUinfo_result.txt 파일로 저장
        f = open(dir + '/CPUinfo_result.txt', 'a')
        f.write('CPUinfo[{0}]={1}\n'.format(processor,CPUinfo[processor]['model name']))
        f.close()

#메모리에 관한 상세 정보 출력
def meminfo():
    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

if __name__ == '__main__':
    meminfo = meminfo()
    time = datetime.now()
    printsave( f"{yellow}{time}{noclr}" + " Collecting Process Info via memoryinfo command ...")
    
     #명령어 실행 결과 meminfo_result.txt 파일로 저장
    f = open(dir + '/meminfo_result.txt', 'w')
    f.write("Total memory:{0}\n".format(meminfo['MemTotal']))
    f.write("Free memory:{0}\n".format(meminfo['MemFree']))
    f.close()

#시스템 부팅 메세지 
def dmesg():
    #subprocess.call('sudo dmesg', shell=True)
    time = datetime.now()
    printsave( f"{yellow}{time}{noclr}" + " Collecting Process Info via dmesg command ...")
    
    subprocess.call('sudo dmesg >'  + dir + '/dmesg_result.txt', shell=True)  #명령어 실행 결과 dmesg_result.txt 파일로 저장
dmesg()