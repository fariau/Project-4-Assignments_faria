import time

def countdown_timer(seconds):
    while seconds > 0 :
        mins, secs = divmod(seconds,60)
        time_format = '{:02d}:{:02d}'.format(mins,secs)
        print(time_format, end='\r')
        time.sleep(1) 
        seconds -= 1
        
    print("00:00 \ntime's up")
    
total_seconds = int(input("enter time in second for countdown: "))
countdown_timer(total_seconds)