from ctypes import Structure, windll, c_uint, sizeof, byref
import time
import winsound

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]
 
def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

while 1:
    GetLastInputInfo = int(get_idle_duration())
    # print GetLastInputInfo
    if GetLastInputInfo == 840:
        # if GetLastInputInfo is 14 minutes, play a sound
        sound = r"c:\windows\media\Windows Logoff Sound.wav"
        winsound.PlaySound(sound, winsound.SND_FILENAME)
    time.sleep(0.2)
