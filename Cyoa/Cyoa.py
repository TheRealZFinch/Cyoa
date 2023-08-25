from lib.keyboard import keyboard
from lib.imgprinter import imgprinter
from sys import argv
import platform

if platform.system() == "Windows":
    from colorama import init
    init()
    clear = "cls"
if platform.system() == "Linux" or platform.system() == "Darwin":
    clear = "clear"

kb = keyboard()