from horloge_poo import PyClock
import time

class Console(PyClock):
    def __init__(self,date,am_pm):
        super().__init__(date,am_pm)
        # self.console = PyClock((0,0,0),24)

    def home(self):
        (print
        (
        "                    --------------------------------------------------------------------\n",
        "                    ------------------------  Welcome to PyClock.  ---------------------\n",
        "                    ----------------  Made specially for grandma Jeannine  -------------\n",
        "                    --------------------------------------------------------------------\n",
        "                    -----------------------  What do you need ?  -----------------------\n",
        "                    --------------------------------------------------------------------\n",
        "                    ----------------------  1 : Personnal Clock  -----------------------\n",
        "                    ----------------------  2 : Live Clock  ----------------------------\n",
        "                    ----------------------  3 : Alarm  ---------------------------------\n",
        "                    ----------------------  4 : Stopwatch  -----------------------------\n",
        "                    ----------------------  5 : Timer  ---------------------------------\n",
        "                    ----------------------  6 : Settings  ------------------------------\n",
        "                    --------------------------------------------------------------------\n",
        "                    -------------------------  Clock set to : --------------------------\n",
        f"                   --------------------------  {self.get_date()}  ---------------------------\n",
        "                    --------------------------------------------------------------------\n",
        "                    ----------------  IN DEVELOPMENT, ERROR MAY OCCUR  -----------------"))
        #answer = int(input("                     ----------------------  Your answer :  -----------------------------\n"))

    def options(self):
        print("""
            "                    --------------------------------------------------------------------\n",
            "                    ----------------------------  Settings.  ---------------------------\n",
            "                    --------------------------------------------------------------------\n",
            "                    -------------------------  Select option  --------------------------\n",
            "                    --------------------------------------------------------------------\n",
            "                    ------------------------- 1 : Change time  -------------------------\n",
            "                    -----------------------  2 : Back to menu  -------------------------\n",
            "                    --------------------------------------------------------------------\n",
            "                    -----------------------  Clock set to : ----------------------------\n",
            f"                   -----------------------  {print(self.get_date())}  ------------------------------\n",
            "                    --------------------------------------------------------------------
            """)

    def interaction(self):
        self.home()
        
        try:
            
            answer = int(input("                     ----------------------  Your answer :  -----------------------------\n"))
            if not 1 < answer < 6:
                print(" Warning ! This option doesn't exist. Please retry in 3 seconds")
                time.sleep(5)
                return
            elif answer == 1:
                print(self.display_time())
            elif answer == 2:
                print(self.live_timing())
            elif answer == 3:
                hour = int(input("Hour : "))
                minute = int(input("Minute : "))
                second = int(input("Second : "))
                print(self.alarm((hour,minute,second)))
            elif answer == 4:
                print(self.stopwatch())
            elif answer == 5:
                hour = int(input("Hour : "))
                minute = int(input("Minute : "))
                second = int(input("Second : "))
                print(self.timer([hour,minute,second]))
            elif answer == 6:
                self.options()
            else:
                print("Choice must be between number 1 and 6 in the menu.")
                return    
            
        except ValueError:
            print("Error :Try again between choice 1-2-3-5-6 in 3 seconds.")
            time.sleep(3)
            return 
        
#    interaction()  
            
