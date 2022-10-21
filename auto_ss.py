import pyautogui
import os
import datetime
import time

upper_time_bound = datetime.time(hour=19)
lower_time_bound = datetime.time(hour=8)

while True:
    lower_folder_name = str(datetime.date.today())
    root_dir = os.path.expanduser("~/Desktop/ss")
    save_path = os.path.join(root_dir, lower_folder_name)
    
    curr_day = datetime.datetime.now()
    curr_time = curr_day.time()
    if(lower_time_bound <= curr_time <= upper_time_bound and curr_day.weekday() <= 4):
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        ss = pyautogui.screenshot()
        ss.save(os.path.join(save_path, f"{curr_time.hour}:{str(curr_time.minute).zfill(2)}.png"))
        time.sleep(60)
        


