import time
import os
import keyboard
import pygame
import threading
import datetime

class PyClock():
    def __init__(self,date:tuple,am_pm):
        self.date = date
        self.am_pm = am_pm

    def check(self):
        if self.am_pm == 12 or self.am_pm == 24:
            pass
        else:
            raise TypeError("Are you idiot or what ?")
            # CHECKING
        if self.date[0] > 24 or self.date[1] > 60 or self.date[2] > 60:
            pass
            #raise TypeError("Please set a normal date.")
        if self.am_pm == 12:
            if self.date[0] >= 12:
                raise TypeError("Please set date to 12h format.")

    def get_date(self): #Force à la complexité ...
        """Function displaying time with hh:mm:ss format"""
        if self.date[0] < 10 and self.date[1] < 10 and self.date[2] < 10:#0 0 0
            return f"0{self.date[0]} : 0{self.date[1]} : 0{self.date[2]}"

        if self.date[0] >= 10 and self.date[1] >= 10 and self.date[2] >= 10:#. . .
            return f"{self.date[0]} : {self.date[1]} : {self.date[2]}"

        if self.date[0] < 10 and self.date[1] >= 10 and self.date[2] < 10:#0 . 0
            return f"0{self.date[0]} : {self.date[1]} : 0{self.date[2]}"

        if self.date[0] >= 10 and self.date[1] < 10 and self.date[2] >= 10:#. 0 .
            return f"{self.date[0]} : 0{self.date[1]} : {self.date[2]}"

        if self.date[0] < 10 and self.date[1] >= 10 and self.date[2] >= 10:#0 . .
            return f"0{self.date[0]} : {self.date[1]} : {self.date[2]}"

        if self.date[0] >= 10 and self.date[1] >= 10 and self.date[2] < 10:#. . 0
            return f"{self.date[0]} : {self.date[1]} : 0{self.date[2]}"

        if self.date[0] < 10 and self.date[1] < 10 and self.date[2] >= 10:#0 0 .
            return f"0{self.date[0]} : 0{self.date[1]} : {self.date[2]}"

        if self.date[0] >= 10 and self.date[1] < 10 and self.date[2] < 10:#. 0 0
            return f"{self.date[0]} : 0{self.date[1]} : 0{self.date[2]}"

    def set_date(self,times:tuple,form):
        """Methdod changing date/format."""
        self.date = times
        self.am_pm = form
        self.check()

    def set_live(self):
        """Set actual time."""
        current_time = datetime.datetime.now()
        self.date = list(self.date)
        self.date[0],self.date[1],self.date[2] = current_time.hour,current_time.minute,current_time.second
        self.date = tuple(self.date)

    def interact(self):
        """Allow user to pause, resume or stop the time."""
        print(self.get_date(), "\nPress space to pause time\nPress CTRL + C to stop time.")
        if keyboard.is_pressed("space"):
            print(f"Time paused. Type $ to resume. Type CTRL + C to stop.")
            while not keyboard.is_pressed("$"):
                copy = list(self.date)
                self.date = copy
                self.date[0] += 0
                if keyboard.is_pressed("$"):
                    self.date = tuple(self.date)
                    print("Time resumed")

    def live_timing(self):
        """Display live timing"""
        stop = False
        while not stop:
            os.system("cls" if os.name == "nt" else "clear")
            self.set_live()
            print(self.get_date())
            time.sleep(1)

    def changing_time(self):
        """Method that allow time advancement."""
        live = list(self.date)
        live[2] += 1
        if live[2] >= 60:
            live[2] = 0
            live[1] += 1
        if live[1] >= 60:
            live[1] = 0
            live[0] += 1
        if live[0] >= 24:
            live = [0,0,0]
        if self.am_pm == 12:
            if live == [12,0,0]:
                live = [0,0,0]
        self.date = tuple(live)

    def display_time(self):
        """Method refreshing time every second"""
        stop = False
        while not stop:
            os.system("cls" if os.name == "nt" else "clear") #clear le terminal
            self.changing_time()
            time.sleep(1)

    def alarm(self,delta:tuple):

        def play_music(music):
            pygame.mixer.init()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()
        def wait_for_input():
            input()
            pygame.mixer.stop()

        while self.date != delta:
            os.system("cls" if os.name == "nt" else "clear")

            print(self.get_date())
            self.changing_time()
            time.sleep(1)

            if self.date == delta:
                music_thread = threading.Thread(target=play_music, args=("Ring.mp3",))
                input_thread = threading.Thread(target=wait_for_input)

                music_thread.start()
                input_thread.start()
                return "RRRRIIIIIINNNNNNNGGGGGGGGG"

    def stopwatch(self):
        """Set a stopwatch."""
        self.set_date((0,0,0),self.am_pm)
        while not keyboard.is_pressed("enter"):
            os.system("cls" if os.name == "nt" else "clear")
            self.changing_time()
            self.interact()
            time.sleep(1)

    def timer(self,chrono:list):
        """Set a timer with a ringtone at the end."""
        def play_music(music):
            pygame.mixer.init()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()
        def wait_for_input():
            input()
            pygame.mixer.stop()
        if len(chrono) != 3:
            raise TypeError("Veuillez entrer exactement 3 éléments minimum dans la liste (h,m,s)")
        if chrono[0] >= 24 or chrono[1] >= 60 or chrono[2] >= 60:
            raise TypeError("Please set a normal date.")
        while chrono != [0,0,0]:
            os.system("cls" if os.name == "nt" else "clear")
            self.date = chrono
            chrono[2] -= 1
            if chrono[2] < 0:
                chrono[2] = 60
                chrono[1] -= 1
            if chrono[1] < 0:
                chrono[0] -= 1
                chrono[1] = 60
            self.interact()
            time.sleep(1)
            if chrono == [0,0,0]:
                music_thread = threading.Thread(target=play_music, args=("Mask-off.mp3",))
                input_thread = threading.Thread(target=wait_for_input)
                music_thread.start()
                input_thread.start()
                return "RRRRIIIIIINNNNNNNGGGGGGGGG"

if __name__ == "__main__":
    timing = PyClock((11,59,55),12)
    #timing.live_timing()
    #print(timing.display_time())
    #print(timing.alarm( (0,0,0) ))
    #print(timing.stopwatch())
    #print(timing.timer([0,0,10]))