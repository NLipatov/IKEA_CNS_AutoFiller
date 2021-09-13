import time
from PIL.ImageOps import grayscale
import pyautogui
from pywinauto.keyboard import send_keys



def click_when_founded(image_filename_png, confidence=0.7, grayscale=True):
    while True:
        what_to_click_on = pyautogui.locateOnScreen(image_filename_png, grayscale=True, confidence=0.9)
        if what_to_click_on != None:
            pyautogui.click(what_to_click_on)
            break
        else: 
            continue

def check_if_located(image_filename_png, confidence=0.7, grayscale=True):
    what_to_click_on = pyautogui.locateOnScreen(image_filename_png, grayscale=True, confidence=0.9)
    if what_to_click_on == None:
        return False
    else:
        return True

def launch_citrix_from_win_start_menu():
    send_keys("{VK_LWIN down}{VK_LWIN up}")
    time.sleep(0.5)
    send_keys('citrix')
    time.sleep(1)
    click_when_founded("Citrix_in_Start_Menu.png")

def Start_CNS():
    #if check_if_located("upper_part_of_citrix_window.png") == False:
    #    launch_citrix_from_win_start_menu()
    #else:
    #    click_when_founded("CNS_Icon_In_Citrix.png")
    click_when_founded("CNS_Icon_In_Citrix.png")

def login_into_CNS_system(login, password):
    while check_if_located("upper_part_of_citrix_window.png") == False:
        check_if_located("part_of_CNS_login_menu.png")
    send_keys(f'{login}')
    send_keys('{TAB}')
    send_keys(f'{password}')
    click_when_founded("Connect_button_on_CNS_login_form.png")

def Date_gen():
    year_yy = time.strftime("%y")
    day_dd = time.strftime("%d")
    month_mm = time.strftime("%m")
    return f"{year_yy}{month_mm}{day_dd}"
    

def OG_Autofill(StringOGType, StringVolume, stringWeight, StringTrip):
    DC1_button_coords = pyautogui.locateOnScreen('DC1.png', grayscale=True, confidence=0.5)


    StringDate = Date_gen()
    StringTime = "0000"


    click_when_founded('Registrate_CSM_Button_PNG.png')
    

    send_keys('339')
    send_keys('{TAB}')
    send_keys('DT')
    send_keys('{TAB}')

    send_keys(StringDate+StringTrip+"OGA")
    send_keys('339')
    send_keys('{TAB}')
    send_keys('DT')
    send_keys('{TAB}')
    send_keys('1')
    send_keys('{TAB}')
    send_keys(f'{StringTrip}')
    send_keys('{TAB}')
    send_keys('STO')
    send_keys('{TAB}')
    send_keys('1')
    send_keys('{TAB}')
    send_keys('{TAB}')
    send_keys('DDU')
    send_keys('{TAB}')
    send_keys(f'{StringDate+StringTime}')
    send_keys('{TAB}')
    send_keys('{TAB}')
    send_keys('{TAB}')
    send_keys('90')
    send_keys('{TAB}')
    send_keys('20000')
    click_when_founded('Other_Articles.png')
    send_keys(f'{StringOGType}')
    send_keys('{TAB}')
    send_keys('1')
    send_keys('{TAB}')
    send_keys('1')
    send_keys('{TAB}')
    send_keys(f'{StringVolume}')
    send_keys('{TAB}')
    send_keys(f'{stringWeight}')
    send_keys('{TAB}')
    send_keys(f'{StringVolume}')
    send_keys('{TAB}')
    send_keys(f'{stringWeight}')
    send_keys('{TAB}')
    send_keys(f'{StringVolume}')
    send_keys('{TAB}')
    send_keys(f'{stringWeight}')









