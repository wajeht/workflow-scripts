import time
import pyautogui

# if you wanna use this version of the auto login script
# pip install pyautogui in ternimal

# edit the following codes
acid = "enter your amarill college id"
acpass = "enter your amarillo college passsword"

pyautogui.hotkey('command', 'space')
pyautogui.typewrite('firefox')
pyautogui.hotkey('enter')

time.sleep(4)

pyautogui.hotkey('command', 'l')
pyautogui.typewrite('https://actx.blackboard.com/webapps/login/')
pyautogui.hotkey('enter')

time.sleep(4)

pyautogui.typewrite(acid)
pyautogui.hotkey('tab')

pyautogui.typewrite(acpass)
pyautogui.hotkey('enter')




