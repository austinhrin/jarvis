# preinstalled python dependancies
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# pip installed dependancies
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def down():
    current_volume = volume.GetMasterVolumeLevel()
    if (current_volume - 5) <= -65:
        dB = -65
    else:
        dB = current_volume - 5
    volume.SetMasterVolumeLevel(dB, None)

def up():
    current_volume = volume.GetMasterVolumeLevel()
    if (current_volume + 5) >= 0.0:
        dB = 0.0
    else:
        dB = current_volume + 5
    volume.SetMasterVolumeLevel(dB, None)

def mute():
    volume.SetMute(1, None)

def unmute():
    volume.SetMute(0, None)

def get_dB(percent):
    if int(percent) == 0:
        db = -65.0
    elif int(percent) == 100:
        db = -0.0
    else:
        '''
        estimate db from percentage using Logarithmic Regression
        http://www.xuru.org/rt/LnR.asp
        for y:
        100 0.0
        93 -1.1
        86 -2.2
        80 -3.3
        75 -4.4
        69 -5.5
        61 -7.5
        55 -8.8
        50 -10.4
        36 -15.0
        25 -20.4
        13 -30.0
        6 -40.0
        0 -65.0
        '''
        # y = 14.2848947 ln(x) - 66.12641667
        # y = 14.35238939 ln(x) - 66.31769768
        db = 14.2848947 * math.log(percent) - 66.12641667
        if db < -65.0:
            db = -65.0
    return db

def set_volume(dB):
    volume.SetMasterVolumeLevel(float(dB), None)
