import simplegui

interval= 100
tick= 0
time= '0:00.0'
total_stops = 0
good_stops = 0
stop = True

def format(t):
    global time
    tenth_sec= t % 10
    sec= int(t/10) % 10
    ten_sec= int(t/100) % 6
    minute= int(t/600) % 600
    time= str(minute) + ':' + str(ten_sec) + str(sec) + ':' + str(tenth_sec)
    return str(time)
    if millisec >= 1000:
        sec += 1
    if sec >= 10:
        ten_sec += 1
    if ten_sec >= 6:
        minute += 1

def create_timer():
    global tick
    tick= tick + 1

def reset():
    global tick, good_stops, total_stops
    tick = 0
    stop = True
    total_stops = 0
    good_stops = 0
    timer.stop()
    
def stop():
    global total_stops
    if stop == False :
        if tick % 10 == 0 and tick != 0 :
            good_stops += 1
            total_stops += 1
        elif tick != 0 :
            total_stops += 1
    stopped = True
    timer.stop()

def start():
    global tick, stop
    stop = False
    timer.start()
    
def draw_handler(canvas):
    text= format(tick)
    canvas.draw_text(str(text), (30, 50), 20, "White")
    canvas.draw_text(str(good_stops) + '/' + str(total_stops), (200,400), 24, "white")
    
    
timer= simplegui.create_timer(interval,create_timer)
frame= simplegui.create_frame('test', 500,500)
frame.set_draw_handler(draw_handler)
frame.add_button("Start",start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.start()
timer.start()