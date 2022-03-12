import pyautogui;
import random;
import time;
list = ["https://www.fiverr.com/seller_dashboard","https://www.fiverr.com/users/freecodebd/manage_orders?source=header_navigation","https://www.fiverr.com/users/freecodebd/manage_gigs","https://www.fiverr.com/users/freecodebd/seller_analytics_dashboard#analytics-seller-level","https://www.fiverr.com/users/freecodebd/seller_analytics_dashboard?tab=repeat_business","https://www.fiverr.com/freecodebd?up_rollout=true","https://www.fiverr.com/users/freecodebd/requests?source=header_nav","https://www.fiverr.com/users/freecodebd/balance/sales"]

while True:
    time.sleep(random.randint(20,180))
    pyautogui.press("f6")
    time.sleep(random.randint(1,5))
    pyautogui.write(random.choice(list))
    time.sleep(random.randint(1,5))
    pyautogui.press("enter")


