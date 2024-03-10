import time
def time_converter(sec):
    sec=sec%60
    min=sec//60
    hour=min//60
    min=sec%60
    print("Time covered is :: {%d:%d:%d}"%(int(hour),int(min),int(sec)))
initial_time=input("Press Enter button to start: ")
initial_time=time.time()    
while True:
    choice=input("break or not??")
    if choice=="break":
        break_time=input("Press break button to break: ")
        break_time=time.time()
        time_break=initial_time-break_time
        time_converter(time_break)
        continue
    else:    
        final_time=input("Press stop button to end: ")
        final_time=time.time()
        time_covered=initial_time-final_time 
        time_converter(time_covered)
        break    