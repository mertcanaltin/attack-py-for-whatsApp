import pyautogui,time
time.sleep(5)
a= open("attackMessage", "r")
for word in a:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
