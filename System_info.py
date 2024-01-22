from ast import Name
from genericpath import isfile
import platform
import os
import subprocess
from datetime import date, datetime

red = '\033[1;31m'
yellow = '\033[0;33m'
noclr = '\033[0m'

dir_main = f"{os.environ['HOME']}/K-Shield_D6"
if os.path.isdir(dir_main) == False: 
    subprocess.run([f"mkdir",  dir_main])
savedir = f"{os.environ['HOME']}/K-Shield_D6/sys"


def osmkdir():
    try:
        if os.path.isdir(savedir) == False:
            subprocess.run(['mkdir', savedir])
    except Exception as err:
        print("Error creating directory: ",f"{red}{err}{noclr}")
        return False

        
def status(name):

    nowtime = datetime.now()

    if os.path.isfile(savedir + "/status.txt") == True:
        f = open(savedir + '/status.txt', "a")
        f.write("{} : {}\n".format(name, nowtime.time()))

    elif os.path.isfile(savedir + "/status.txt") == False:
        f = open(savedir + '/status.txt', "w")
        f.write("today : {}\n".format(nowtime.date()))
        f.write("---------------------------------------\n")
        f.write("{} : {}\n.".format(name, nowtime.time()))
    
    print(f"{yellow}{(nowtime.now())}{noclr}" + " Collecting System Info via {} ...".format(name) )
    #print("-----------------------{}------------------\n".format(name))
    
    f.close()
   

def file_save(path, filename, savename):
    

    if os.path.isfile(savedir + savename) == True:

        f = open(path + filename, "r")
        s = open(savedir + savename, "a")
        data = f.read()
        s.write("----------------------{}--------------------------------\n".format(filename))
        s.write(data)
        s.write("-----------------------------------------------------\n\n")
        s.close()    
        f.close
    elif os.path.isfile(savedir + savename) == False:
        f = open(path + filename, "r")
        s = open(savedir + savename, "w")
        data = f.read()
        s.write("----------------------{}--------------------------------\n".format(filename))
        s.write(data)
        s.write("-----------------------------------------------------\n\n")
        s.close()    
        f.close


def os_sys(command, save_name):
    subprocess.run("echo '---------------------------{}-------------------------------' >> ".format(command) + savedir + save_name, shell=True)
    subprocess.run('{} >> '.format(command) + savedir + save_name, shell=True)
    subprocess.run("echo '---------------------------------------------------------------\n' >> " + savedir + save_name, shell=True)




def sys_info():
    status("system_info")
    s = open(savedir + '/system_info.txt', "w")
    s.write("----------------sysytem_info------------------\n")
    s.write("Architecture : " + platform.architecture()[0] + "\n") #architecture
    s.write("Machine : " + platform.machine() + "\n") #machine
    s.write("Node : " + platform.node() + "\n")    #node
    s.write("System : " + platform.system() + "\n") #os
    now = str(datetime.now()) # 현재시간
    s.write("local time : " + now + "\n")
    s.write("-------------------------------------------------\n\n")
    s.close()

    status("uname") #system_info
    os_sys("uname -a", "/system_info.txt")
    os_sys("uname -r", "/system_info.txt")
    
    status("locale")
    file_save("/etc/default/", "locale", "/system_info.txt")


    status("fstab")
    #etc/fstab 부팅시 마운트 정보
    file_save("/etc/","fstab","/system_info.txt")
    
    
    
    
    status("mtab")
    # /etc/mtab 현재 마운트 상태에 대한 정보
    file_save("/etc/","mtab","/system_info.txt")
    


    status("issue")
    file_save("/etc/", "issue", "/issue.txt")     #로그인전 로컬접속시도 message


    status("issue.net")
    file_save("/etc/","issue.net", "/issue.txt")

    status("kernel_info")
    os_sys("find /etc ! -path /etc -prune -name '*release*' -print0 | xargs -0 cat 2>/dev/null", "/kernel_info.txt") #kernel_info

    status("modules") #모듈정보
    os_sys("lsmod", "/modules.txt")

    status("sudo") #sudo
    os_sys("sudo -V", "/sudo.txt")

    status("lsusb") #usb information
    os_sys("lsusb", "/usb_info.txt")
    
    status("mount") #mount된 정보
    os_sys("mount", "/mount.txt")
    

    status("df") # 파일시스템 크기와 용량
    os_sys("df", "/df.txt")
  
    status("packages istall information")
    os_sys("cat $MOTHERPATH/var/lib/dpkg/status | grep -B 1 'Status: install ok installed'", "/pkg_inf.txt")

osmkdir()
sys_info()

#ubuntu 20 /etc/inittab이 없음..?