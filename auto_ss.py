import pyautogui
import os
import datetime
import time
import argparse

if __name__ == '__main__':


    parser = argparse.ArgumentParser()
 
    # Adding optional argument
    parser.add_argument("-d", "--dir", help = "Directory screenshots are saved to. Default is ..../Desktop/ss")
    
    # Read arguments from command line
    args = parser.parse_args()
    root_dir = os.path.expanduser(os.path.join("~", "Desktop", "ss"))
 
    if args.dir:
        root_dir = args.dir

    upper_time_bound = datetime.time(hour=19)
    lower_time_bound = datetime.time(hour=8)

    while True:
        lower_folder_name = str(datetime.date.today())
        save_path = os.path.join(root_dir, lower_folder_name)
        
        curr_day = datetime.datetime.now()
        curr_time = curr_day.time()
        # can't use colon in windows filename
        png_name = os.path.join(save_path, f"{curr_time.hour}.{str(curr_time.minute).zfill(2)}.png")
        if(lower_time_bound <= curr_time <= upper_time_bound and curr_day.weekday() <= 4):
            try:
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                pyautogui.screenshot(png_name)
                
            except:
                pass
            time.sleep(60)
            


