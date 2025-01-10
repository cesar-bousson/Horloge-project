from horloge_poo import PyClock
import os
import time

class Console(PyClock):
    def __init__(self,date,am_pm):
        super().__init__(date,am_pm)
        self.console = PyClock((0,0,0),24)

    def home(self):
        (print
        (
        "                     ______________________________________________________________________\n",
        "                    |--------------------------------------------------------------------|\n",
        "                    |------------------------  Welcome to PyClock.  ---------------------|\n",
        "                    |----------------  Made specially for grandma Jeannine  -------------|\n",
        "                    |--------------------------------------------------------------------|\n",
        "                    |-----------------------  What do you need ?  -----------------------|\n",
        "                    |--------------------------------------------------------------------|\n",
        "                    |------------------------  1 : Start Clock  -------------------------|\n",
        "                    |------------------------  2 : Live Clock  --------------------------|\n",
        "                    |------------------------  3 : Alarm  -------------------------------|\n",
        "                    |------------------------  4 : Stopwatch  ---------------------------|\n",
        "                    |------------------------  5 : Timer  -------------------------------|\n",
        "                    |------------------------  6 : Settings  ----------------------------|\n",
        "                    |--------------------------------------------------------------------|\n",
        "                    |------------------------  Clock set to : ---------------------------|\n",
        f"                    |--------------------------  {self.get_date()}  --------------------------|\n",
        "                    |--------------------------------------------------------------------|\n",
        "                    |-----------------  IN DEVELOPMENT, ERROR MAY OCCUR  ----------------|"))
        "                    |--------------------------------------------------------------------|\n"

        #answer = int(input("                     ----------------------  Your answer :  -----------------------------\n"))

    def options(self):
        print(
            "                     ______________________________________________________________________\n",
            "                    |--------------------------------------------------------------------|\n",
            "                    |--------------------------  Settings.  -----------------------------|\n",
            "                    |--------------------------------------------------------------------|\n",
            "                    |------------------------  Select option  ---------------------------|\n",
            "                    |--------------------------------------------------------------------|\n",
            "                    |------------------------ 1 : Change time  --------------------------|\n",
            "                    |-----------------------  2 : Back to menu  -------------------------|\n",
            "                    |--------------------------------------------------------------------|\n",
            "                    |------------------------  Clock set to : ---------------------------|\n",
            f"                    |-------------------------  {self.get_date()}  ---------------------------|\n",
            "                    |--------------------------------------------------------------------|")

    def interaction(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.home()
        answer = int(input("                     |--------------------------  Your answer :  -------------------------|\n                                                       "))
        if not 0 < answer < 7:
            print("This option doesn't exist. Please wait...")
            time.sleep(5)
            self.interaction()
        else:
            pass

        #DISPLAYING TIME
        if answer == 1:
            print(self.display_time())

        #LIVE TIMING
        if answer == 2:
            print(self.live_timing())

        #ALARM
        if answer == 3:
            hour = int(input("Hour : "))
            minute = int(input("Minute : "))
            second = int(input("Second : "))
            print(self.alarm((hour,minute,second)))

        #STOPWATCH
        if answer == 4:
            print(self.stopwatch())

        #TIMER
        if answer == 5:
            hour = int(input("Hour : "))
            minute = int(input("Minute : "))
            second = int(input("Second : "))
            print(self.timer([hour,minute,second]))

        #SETTINGS
        if answer == 6:
            os.system("cls" if os.name == "nt" else "clear")
            self.options()
            question = int(input("                     |--------------------------  Your answer :  -------------------------|\n                                                       "))
            if not 0 < question < 3:
                print("It's either 1 or 2, no more options. Please wait...")
                time.sleep(5)
                self.interaction()
            if question == 1:
                hour = int(input("Hour : "))
                minute = int(input("Minute : "))
                second = int(input("Second : "))
                format = int(input("Format : "))
                self.set_date((hour, minute, second),format)
                os.system("cls" if os.name == "nt" else "clear")
                self.interaction()
            if question == 2:
                os.system("cls" if os.name == "nt" else "clear")
                self.interaction()

        """
        if answer == 1:
            print("Not possible yet")
            heure = int(input("Hour : "))
            minute = int(input("Minute : "))
            second = int(input("Second : "))
            format = int(input("Format (12/24) : "))
            self.set_date((heure,minute,second),format)
        if answer == 2:
            self.home()
        """

ok = Console((0,0,0),am_pm=24)
print(ok.interaction())