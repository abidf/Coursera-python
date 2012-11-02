# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = '0:00.0'
t = 0
game_count = 0
win_count = 0
is_going = 0
# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D

def format(t):
    global time
    milliseconds = t % 10
    sec = (t - milliseconds) / 10
    minutes = sec // 60
    seconds = sec % 60
    if seconds >=10:
        time = str(minutes) + ':' + str(seconds) + '.' +str(milliseconds)
    else:
        time = str(minutes) + ':0' + str(seconds) + '.' +str(milliseconds)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start_button():
    global is_going
    is_going = 1
    timer.start()
    
def stop_button():
    global game_count, win_count, is_going
    timer.stop()
    game_count = game_count + is_going
    if time[-1] == '0' and is_going:
        win_count = win_count + 1
    is_going = 0    
    
def reset_button():
    global t, time, game_count, win_count, is_going
    game_count = 0
    win_count = 0
    is_going = 0
    timer.stop()
    t = 0
    format(t)

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global t
    t = t + 1
    format(t)

def draw(canvas):
    canvas.draw_text(time, (100, 100), 32, "Red")
    canvas.draw_text(str(win_count) + '/' + str(game_count), 
                     (250, 20), 20, "Green")
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
frame.add_button("Start", start_button, 100)
frame.add_button("Stop", stop_button, 100)
frame.add_button("Reset", reset_button, 100)
# start timer and frame
frame.start()

# remember to review the grading rubric