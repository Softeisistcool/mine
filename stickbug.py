import os
import webbrowser
import keyboard

i = 2
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

stickbug = 'https://www.youtube.com/watch?v=Tt7bzxurJ1I'
while True:
    if keyboard.is_pressed('9'):
        webbrowser.get(chrome_path).open(stickbug)













