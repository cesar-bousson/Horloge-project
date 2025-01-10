from horloge_poo import PyClock

class Console(PyClock):
    def __init__(self,date,am_pm):
        super().__init__(date,am_pm)
        self.console = PyClock((0,0,0),24)

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
        print(
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
            "                    --------------------------------------------------------------------")

    def interaction(self):
        self.home()
        answer = int(input("                     ----------------------  Your answer :  -----------------------------\n"))
        if not 0 < answer < 7:
            print("This option doesn't exist. Please retry...")
        if answer == 1:
            print(self.display_time())
        if answer == 2:
            print(self.live_timing())
        if answer == 3:
            hour = int(input("Hour : "))
            minute = int(input("Minute : "))
            second = int(input("Second : "))
            print(self.alarm((hour,minute,second)))
        if answer == 4:
            print(self.stopwatch())
        if answer == 5:
            hour = int(input("Hour : "))
            minute = int(input("Minute : "))
            second = int(input("Second : "))
            print(self.timer([hour,minute,second]))
        if answer == 6:
            self.options()
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