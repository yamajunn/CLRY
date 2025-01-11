import pywinctl as pwc
from PIL import ImageGrab

def capture_region(x, y, width, height, save_path):
    region = (x, y, x + width, y + height)
    screen = ImageGrab.grab(bbox=region)
    screen.save(save_path)

# print(pwc.getAllWindows())
# print(pwc.getAllTitles())
# print(pwc.getWindowsWithTitle('iPhoneミラーリング'))
win = pwc.getWindowsWithTitle('iPhoneミラーリング')[0]
win.activate()
print(win.left+5, win.top+35, win.left+win.width-5, win.top+win.height-7)
    
capture_region(win.left+6, win.top+37, win.width-12, win.height-43, "region_screenshot.png")