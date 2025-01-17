import pywinctl as pwc
import pyautogui

def capture_area(filename, x, y, width, height):
    image = pyautogui.screenshot(region=(x, y, width, height))
    image.save(filename)

# print(pwc.getAllWindows())
# print(pwc.getAllTitles())
# print(pwc.getWindowsWithTitle('iPhoneミラーリング'))
win = pwc.getWindowsWithTitle('iPhoneミラーリング')[0]
win.activate()
capture_area("region_screenshot.png", win.left+6, win.top+37, win.left+win.width-6, win.top+win.height-10)