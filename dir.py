import requests
import os,time
B = "\033[34m"    # BlueB 
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
head={"User-Agent":user}
def dir():
 os.system("figlet Dir brute")
 space=8*" "
 print(f"{C}{space}https://github.com/Ag3ntQ{W}")
 print(" ")
 inp=input("[#] Enter Domain : ")
 file_name=input("[#] Enter file name : ")
 print(25*"=")
 files=open(file_name)
 for line in files:
   line=line.strip()
   url=inp+"/"+line
   try:
    res=requests.get(url,headers=head)
    if res:
     print(f"[ • ] {line} [{res.status_code}]{W}")
    else:
       pass
   except KeyboardInterrupt:
   	break
   	print("[ !! ] KeyboardInterrupt : Terminated")
   except :
   	pass
  
try: 
 dir() 
except Exception as e:
	print(25*"-")
	print(f"{R}[•] {e}{W}")
	print(25*"-")