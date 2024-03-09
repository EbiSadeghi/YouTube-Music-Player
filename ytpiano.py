import pyautogui
import time
import subprocess

def open_firefox(numTabs, link):
    # Open Firefox  
    for ii in range(numTabs):
        subprocess.Popen(['firefox'])

    # Wait for Firefox to open
    time.sleep(4)

    # Open a webpage (replace 'https://www.example.com' with your desired URL)
    for ii in range(numTabs):
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.5)
        pyautogui.write(link)
        pyautogui.press('enter')
        time.sleep(0.5)
    time.sleep(7)  # Wait for the page to load


# Press number keys (1 to 9)
def play_verse(myList):
    for ii in myList:
        if (ii is not None):
            pyautogui.press(str(ii))
            time.sleep(0.25)  
            pyautogui.hotkey('alt', 'tab')
        time.sleep(0.25)  # Wait for a bit between key presses

# You can add more code here if needed
leanOnMe = [1, None , 1, 2, 3, 4, None, 4, 3, 2, 1, None, 1, 2, 3, 3, None, 2] 
pirate = [3, 5, 6, 6, None, 6, 7, 8, 8, None,  8, 9, 7, 7, None,  6, 5, 5, 6]

chordsLink = "https://www.youtube.com/watch?v=qWX31yz68Ns"
pianoLink = "https://www.youtube.com/watch?v=3gZC5763wYk"

open_firefox(2, chordsLink)

play_verse(leanOnMe)
play_verse(leanOnMe)
play_verse(leanOnMe)

