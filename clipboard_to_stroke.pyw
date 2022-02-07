#libs
import pyclip
from pyautogui import write
import logging
from sys import argv

debug1 = 0

logging.basicConfig(filename=f'{argv[0]}.log', encoding='utf-8',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logger = logging.getLogger(__name__)

if debug1: logging.info("//////////////Script start//////////////")
#get clipboard
clp_d = pyclip.paste()
if debug1: logging.info(f"Coppied: {clp_d}")
#convert bit list to string
clp_utf_8 = clp_d.decode('utf-8')
if debug1: logging.info(f"Coppied conv to string: {clp_utf_8}")
write(clp_utf_8)
