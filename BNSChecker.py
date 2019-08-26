import psutil #https://pypi.org/project/psutil/
import os, sys
from playsound import playsound #https://pypi.org/project/playsound/

found = False
counter = 0
amount_of_minutes_utill_kill = 120
BNS = []
warning_sound = "countdown.wav"
one_minute_remaining = "underaminute.mp3"

while(True):
    print("Looking for processes...")
    while(not found):
        counter = 0
        for p in psutil.process_iter(): #Search through all active processes
            if p.name() in ["Client.exe", "NCLauncher2.exe"] and not p in BNS: #We find the process we are looking for
                print(p, "found")
                killed = False
                BNS += [psutil.Process(p.pid)]
                print("Addded ",p.name(), " with the PID: ", p.pid, "to the list")
            if len(BNS) > 1:
                found = True;
                print("Found all occurrences...")
                break

    print("[Started Counter]")
    while(found):
        counter = BNS[1].cpu_times().user
        if (counter > amount_of_minutes_utill_kill * 60):
            print("[Finished Counter]")
            for process in BNS:
                print("Killed: ", process.name())
                process.kill()
            print(counter)
            if input("Press any key to exit..."): 
                sys.exit()
        elif (counter >= (amount_of_minutes_utill_kill * 60) - 11):
            print("Final Call!")
            playsound(warning_sound)
        elif (counter >= (amount_of_minutes_utill_kill * 60) - 60):
            print("Warning!")
            playsound(one_minute_remaining)
