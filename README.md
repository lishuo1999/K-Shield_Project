# K-Shield Jr 8_Team6
케이쉴드 주니어 8기 침해사고대응 D반 최종 프로젝트

## 개요
- 주제 : ```리눅스 침해사고조사 스크립트 개발```
- 진행 기간 : ```2022.07 ~ 2022.08```
- 참여 인원 : ```5명```
- 역할 : ```User_info.py / main.py 개발``` 

</br>

## 기술 스택
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white" /> <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat&logo=Ubuntu&logoColor=white" /> <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white" />

</br>

## 프로젝트 소개
- 리눅스 환경 가상머신 대상으로 침해사고조사 스크립트 Python언어를 사용해 개발
- 조사대상 아티팩트를 사용자 정보, 파일, 네트워크 통신, 프로세스, 시스템 정보 크게 다섯 파트로 나누어 수집
    + 사용자 정보: 로그인, 로그아웃 등의 로그 데이터 및 현재 로그인 상태인 사용자 계정 정보, 계정 수 등 포함, 시스템에 등록된 사용자, 그룹 등 관련 정보들 포함
    + 파일 정보: \var\log, \etc\passwd, \etc\sysconfig, \proc\meminfo 등 정보
    + 네트워크 통신 정보: 인터페이스 설정 정보, 네트워크 정보, 네트워크 연결 상태, 라우팅 테이블, 인터페이스 상태 등 포함
    + 프로세스 정보: 시스템에 동작 중인 모든 프로세스, CPU와 메모리에 관한 정보, 시스템 부팅 메시지 등 포함
    + 시스템 정보: 시스템관련 전반적 정보, 마운트된 정보, 모듈, 파일 시스템 크기와 용량, usb 등 정보 포함

## 서비스 특징
- 침해사고 분석 단계에서 데이터 수집 작업 자동화시켜 시간 절약 및 일관성 유지함으로써 업무 효율성 향상화
- 수집된 정보는 현재 디렉토리에서 별도의 폴더 생성과 함께 저장
    + 사용자 정보: /usr
    + 파일 정보: /file
    + 네트워크 통신 정보: /net
    + 프로세스 정보: /proc
    + 시스템 정보: /sys
- 아트팩트 수집 담당자 정보 입력받아 별로의 파일에 저장하여 책임 추적하는데 용이

</br>

## 담당 역할 및 학습 내용
- 사용자 정보 및 로그인 정보 수집하는 User_info.py와 메인 실행 파일 main.py 개발
- 사용자 정보 및 로그인 정보 수집 명령어 학습
- 파이썬 rgparse 라이브러리 학습해 스크립트 개발
- 리눅스 기본 아트팩트 종류 및 디렉토리 서칭 및 정리
- Ubuntu 22.04 및 CentOS 7 대상으로 데이터 수집 실습을 통해 명령어 숙지

</br>


## 서비스 실행
### Main.py

Automatically collect Linux artifacts script
 <br/>

### How to use
```
root@ubuntu:~/K-Shield_D6# python3 main.py -h
usage: main.py [-h] [-p] [-n] [-s] [-f] [-u] [-a] [--group GROUP]
               [--name NAME] [--comment COMMENT] [-d DIRECTORY]

Automatically collect Linux artifacts script

options:
  -h, --help            show this help message and exit
  -p, --process         Collecting data about process
  -n, --network         Collecting data about network
  -s, --system          Collecting data about system
  -f, --file            Collecting data about file
  -u, --user            Collecting data about user
  -a, --all             Collecting all data
  --group GROUP
  --name NAME
  --comment COMMENT
  -d DIRECTORY, --directory DIRECTORY
```

Execute with personal information
------------
```
root@ubuntu:~/K-Shield_D6# python3 main.py --group K-Shield --name user --comment 'Team Project'


    __    __             __                  __        __
   |  |  /  /           |  |    __          |  |      |  | 
   |  | /  /        __ _|  |__ |__| _______ |  |      |  |
   |  |/  /  ___   /  __|  |_ \ __ /  ___  \|  | _____|  |
   |     |  |___| |  /_ |   _  |  |  /___\  |  |/  __    |       
   |  |\  \        \__  \  | | |  |  \_____/|  |  |__|   |  
   |__| \__\      |____ /__| |_|__|\_______ |__|\________|          
   
    Group: K-Shield
    Name: user
    date: 2022-08-20 22:34:16.530594
    Comment: Team Project
```
### User_info

```
root@ubuntu:~/K-Shield_D6# python3 main.py -u
Making directory to store investigator's personal information: /root/K-Shield_D6/result
Making directory to store evidence: /root/K-Shield_D6/usr
2022-08-20 22:27:05.626556  Collecting System Login Failure History via 'lastb' command ...
2022-08-20 22:27:05.665170  Collecting System Login History via 'lastlog' command ...
2022-08-20 22:27:05.703223  Collecting Login User Information via 'who' command ...
2022-08-20 22:27:05.712757  Collecting All Login User Information  via 'who -aH' command ...
2022-08-20 22:27:05.719587  Collecting Login User Accounts and Number of users Logged in via 'who -q' command ...
2022-08-20 22:27:05.724953  Collecting Login User Accounts via 'whoami' command ...
2022-08-20 22:27:05.731152  Collecting Login User Accounts via 'logname' command ...
2022-08-20 22:27:05.740399  Collecting Login User Information via 'w' command ...
2022-08-20 22:27:05.778597  Collecting Login User Accounts via 'users' command ...
2022-08-20 22:27:05.784256  Collecting The Number of users Logged in via 'users | wc -w' command ...
2022-08-20 22:27:05.790343  Collecting Login and Logout Information via 'last' command ...
2022-08-20 22:27:05.801230  Collecting File /etc/auth.log contents ...
2022-08-20 22:27:05.811077  Collecting Account Information via 'id' command ...
2022-08-20 22:27:05.818198  Collecting File /etc/passwd contents ...
2022-08-20 22:27:05.823893  Collecting File /etc/shadow contents ...
2022-08-20 22:27:05.859446  Collecting File /etc/group contents ...
2022-08-20 22:27:05.864563  Collecting File /etc/default/useradd contents ...
2022-08-20 22:27:05.870542  Collecting File /etc/skel contents ...
2022-08-20 22:27:05.879162  Collecting File /etc/login.defs contents ...
2022-08-20 22:27:05.883910  Collecting File /etc/gshadow contents ...
```

### File_info
------------
```
root@ubuntu:~/K-Shield_D6# python3 main.py -f
Making directory to store evidence: /root/K-Shield_D6/file
2022-08-20 22:29:07.684616  Log File Information
2022-08-20 22:29:07.808724  Excutables File Information
2022-08-20 22:32:28.976428  Hidden File Information
2022-08-20 22:32:29.033846----------Open File Information----------
```

### Network_info
```
root@ubuntu:~/K-Shield_D6# python3 main.py -n
Making directory to store evidence: /root/K-Shield_D6/net
2022-08-20 22:28:31.332465 Collecting Network Info via 'ifconfig' command ... 
2022-08-20 22:28:31.366966 Collecting File /etc/hosts contents ...
2022-08-20 22:28:31.374486 Collecting File /etc/hosts.allow contents ...
2022-08-20 22:28:31.387150 Collecting File /etc/hosts.deny contents ...
2022-08-20 22:28:31.397602 Collecting File /etc/resolv contents ... 
2022-08-20 22:28:31.397602 Collecting Network Info via 'ip link show' command ... 
------ End time :   2022-08-20 22:28:31.420596 ------
2022-08-20 22:28:31.420933 Collecting Network Info via 'arp' command ... 
------ End time :   2022-08-20 22:28:31.585942 ------
2022-08-20 22:28:31.586384 Collecting Network Info via 'netstat' command ... 
------ End time :   2022-08-20 22:28:40.158359 ------
2022-08-20 22:28:40.158646 Collecting Network Info via 'ss' command ... 
------ End time :   2022-08-20 22:28:40.586532 ------
2022-08-20 22:28:40.587227 Collecting Network Info via 'nmcli' command ... 
------ End time :   2022-08-20 22:28:40.895114 ------
2022-08-20 22:28:40.895341 Collecting File /proc/net contents ... 
------ End time :   2022-08-20 22:28:41.296879 ------
2022-08-20 22:28:41.297373 Collecting Extra Network Info ... 
------ End time :   2022-08-20 22:28:52.314459 ------
```

### Process_info
```
root@ubuntu:~/K-Shield_D6# python3 main.py -p
Making directory to store evidence: /root/K-Shield_D6/proc
2022-08-20 22:27:56.018745 Collecting Process Info via ps aux command ...
2022-08-20 22:27:56.084835 Collecting Process Info via ps -ef command ...
2022-08-20 22:27:56.355013 Collecting Process Info via top -n 1 command ...
2022-08-20 22:27:56.355762 Collecting Process Info via CPUinfo command ...
2022-08-20 22:27:56.356038 Collecting Process Info via CPUinfo command ...
2022-08-20 22:27:56.356280 Collecting Process Info via CPUinfo command ...
2022-08-20 22:27:56.356465 Collecting Process Info via CPUinfo command ...
2022-08-20 22:27:56.356834 Collecting Process Info via memoryinfo command ...
2022-08-20 22:27:56.357074 Collecting Process Info via dmesg command ...
```

### System_info 
```
root@ubuntu:~/K-Shield_D6# python3 main.py -s
2022-08-20 22:28:14.029736 Collecting System Info via system_info ...
2022-08-20 22:28:14.077326 Collecting System Info via uname ...
2022-08-20 22:28:14.120843 Collecting System Info via locale ...
2022-08-20 22:28:14.122862 Collecting System Info via fstab ...
2022-08-20 22:28:14.123998 Collecting System Info via mtab ...
2022-08-20 22:28:14.125231 Collecting System Info via issue ...
2022-08-20 22:28:14.127913 Collecting System Info via issue.net ...
2022-08-20 22:28:14.130295 Collecting System Info via kernel_info ...
2022-08-20 22:28:14.172613 Collecting System Info via modules ...
2022-08-20 22:28:14.219519 Collecting System Info via sudo ...
2022-08-20 22:28:14.252624 Collecting System Info via lsusb ...
2022-08-20 22:28:14.303638 Collecting System Info via mount ...
2022-08-20 22:28:14.329735 Collecting System Info via df ...
2022-08-20 22:28:14.353982 Collecting System Info via packages istall information ...
```
