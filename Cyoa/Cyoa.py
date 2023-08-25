from lib.keyboard import keyboard
from lib.imgprinter import imgprinter
import platform

if platform.system() == "Windows":
    from colorama import init
    init()

kb = keyboard()

