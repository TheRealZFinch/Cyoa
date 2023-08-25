import ctypes
import platform

class keyboard:
    def __init__(self):
        os = platform.system()
        if os == "Windows":
            self.keyboard = ctypes.CDLL(".\\lib\\keyboard.dll")
        elif os == "Linux":
            self.keyboard = ctypes.CDLL("./lib/keyboard.so")

    def Wait(self):
        return self.keyboard.Wait()

    def WaitFor(self, keyname):
        while True:
            key = self.keyboard.Wait()
            if key == ord(keyname):
                break
        return True