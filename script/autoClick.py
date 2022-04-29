import time

import pyautogui

while True:
    location = pyautogui.locateCenterOnScreen('keepStuding.jpg', confidence=0.9)
    if location is not None:
        pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button='left')
        break
    print("未找到匹配图片,5秒后重试")
    time.sleep(5)