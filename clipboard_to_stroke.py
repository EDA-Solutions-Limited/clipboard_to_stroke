"""A script used to send keyboard inputs to the computer from clipboard"""
import logging
from sys import argv
from time import sleep
import pyclip
from pyautogui import write

debug_switch = 0

logging.basicConfig(filename=f'{argv[0]}.log',
                    encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

if debug_switch:
    logging.info("//////////////Script start//////////////")

#get clipboard
clp_d = pyclip.paste()
if debug_switch:
    logging.info(f"Copied: {clp_d}")

#convert bit list to string
clp_utf_8 = clp_d.decode('utf-8')
if debug_switch:
    logging.info(f"Copied conv to string: {clp_utf_8}")
sleep(1)
write(clp_utf_8)
