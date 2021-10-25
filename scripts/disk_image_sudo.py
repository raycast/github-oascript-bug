import subprocess
import os
import logging

__APP_NAME = "image1.jpg"

def create_disk_image(dir_path, disk_image_path):
    logging.info("Creating disk image...")

    dirname = os.path.dirname(__file__)
    script_path = os.path.join(dirname, "./create-dmg-sudo")

    subprocess.run(
        f'{script_path} --volname "Debug" --window-pos 200 120 --window-size 800 400 --icon-size 100 --icon "{__APP_NAME}" 200 190 --hide-extension "{__APP_NAME}" --app-drop-link 600 185 "{disk_image_path}" {dir_path}', shell=True, check=True)

create_disk_image("disc_content", "disc.dmg")
