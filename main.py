import os
import keyboard
import shutil
import configparser
import sys
from typing import List
import pystray
from pystray import MenuItem as item
from PIL import Image
import threading
from pathlib import Path


exclusion_added = False
shortcut_paths: List[str] = []
default_lnks_path = os.path.join(r'C:\Users\Public\Documents', 'Links')
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
# Load user settings from config file
config = configparser.ConfigParser()
config.read("config.ini")
if not config.has_section("Settings"):
    config.add_section("Settings")
    config.set("Settings", "lnks_path", default_lnks_path)
    config.set("Settings", "hotkey", "ctrl+win")
    with open("config.ini", "w") as configfile:
        config.write(configfile)
lnks_path = config.get("Settings", "lnks_path")
hotkey = config.get("Settings", "hotkey")
if not os.path.exists(lnks_path):
    os.makedirs(lnks_path)


def move_shortcuts():
    global shortcut_paths
    if os.listdir(lnks_path):
        for file in os.listdir(lnks_path):
            if file.endswith('.lnk'):
                file_path = os.path.join(lnks_path, file)
                if file in os.listdir(desktop_path):
                    os.remove(os.path.join(desktop_path, file))
                shortcut_paths.append(file_path)
                shutil.move(file_path, desktop_path)
    else:
        for file in os.listdir(desktop_path):
            if file.endswith('.lnk'):
                file_path = os.path.join(desktop_path, file)
                shortcut_paths.append(file_path)
                shutil.move(file_path, lnks_path)


def exit():
    icon.stop()
    keyboard.remove_hotkey(hotkey)
    os._exit(0)


def setup_tray():
    executable_folder = getattr(sys, '_MEIPASS', Path(__file__).parent)
    icon_path = str(executable_folder) + r"\ico\pic.ico"
    image = Image.open(icon_path)
    # image = Image.open(r"x:\pic.ico")
    menu = (item('EXIT', exit),)
    return pystray.Icon("LnkHider", image, "LnkHider", menu)


def tray_icon():
    global icon
    icon = setup_tray()
    icon.run()


keyboard.add_hotkey(hotkey, move_shortcuts)

tray_thread = threading.Thread(target=tray_icon)
tray_thread.start()

print("Listening for shortcuts...")
keyboard.wait()
