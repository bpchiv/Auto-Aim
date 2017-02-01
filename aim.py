import pyautogui
im1=pyautogui.screenshot()
im1.save('my_screenshot.png')
location = pyautogui.locate('images/Heroes/Widow/widow_head.png','my_screenshot.png', grayscale=False)

print(location)

#widow_location = pyautogui.locateOnScreen('images/Heroes/Widow/widow_head.png')
#print(widow_location)
#widowX,widowY = pyautogui.center(widow_location)
#pyautogui.moveTo(widowX,widowY)
