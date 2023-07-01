import pyautogui
pyautogui.FAILSAFE = False
from time import sleep

width = pyautogui.size()[0]
height = pyautogui.size()[1]

try:
    print("Pressione CTRL + C para interromper o script")
    while True:
        pyautogui.moveTo(width, height, duration=1)
        sleep(10)
        pyautogui.moveTo(width, (height - 1), duration=1)
        sleep(10)
except KeyboardInterrupt:
    print("\nScript interrompido")
