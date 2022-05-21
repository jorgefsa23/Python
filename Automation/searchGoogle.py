import pyautogui
import time

searchTerm = input('Input seaching word(s)\n')
Outputformat = int(input('Select  Output option:\n1-information on screen\n2-save as pdf file\n3-save as html file\n'))

pyautogui.alert("Code running. DO NOT use computer untill the END message!\n")
pyautogui.PAUSE = 1

# Search term
pyautogui.press('winleft')
pyautogui.write(searchTerm)
pyautogui.press('enter')
time.sleep(3)

if Outputformat == 1:
    pyautogui.alert("Process finished. Please, read the result on your browser!")
elif Outputformat == 2:
    pyautogui.hotkey('ctrl', 'p')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write(searchTerm)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'f4')
    pyautogui.alert("Process finished. Please open the PDF file!")
else:
    pyautogui.hotkey('ctrl', 's')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write(searchTerm)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'f4')
    pyautogui.alert("Process finished. Please open the HTML file!")