from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
VIO = "#D77FA1"
NUDE = "#FDD7AA"
GREEN = "#45b0aa"
AQUA = "#2abbb5"
COMPLETION_COLOR = "#019267"
FONT_NAME = "Comic sans ms"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None
mark = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    window.after_cancel(timer)
    start_button.config(bg=GREEN)
    reset_button.config(bg=GREEN)
    center_label.config(text="Pomodoro Timer", bg=NUDE, fg=AQUA,)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        center_label.config(text="Long Break", fg=VIO)
        start_button.config(bg=VIO)
        reset_button.config(bg=VIO)
    elif reps % 2 == 0:
        center_label.config(text="Break", fg=VIO)
        count_down(SHORT_BREAK_MIN * 60)
        start_button.config(bg=VIO)
        reset_button.config(bg=VIO)
        check_mark.config()
    else:
        center_label.config(text="Work", fg=AQUA)
        start_button.config(bg=GREEN)
        reset_button.config(bg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, mark
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        if reps % 2 == 0:
            for n in range(math.floor(reps/2)):
                mark += "✓"
                check_mark.config(text=mark, fg=COMPLETION_COLOR)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=NUDE)

canvas = Canvas(width=680, height=680,bg=NUDE, highlightthickness=0)
img = PhotoImage(file="tomatoo.png")
canvas.create_image(340, 340, image=img)
timer_text = canvas.create_text(340, 390, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=0, row=1, columnspan=3, rowspan=1)

center_label = Label(text="Pomodoro Timer", bg=NUDE, fg=AQUA, font=(FONT_NAME, 35, "bold"))
check_mark = Label(bg=NUDE, font=(FONT_NAME, 20, "bold"))
start_button = Button(text="Start", command=start_timer, bg=GREEN, font=(FONT_NAME, 15, "normal"))
reset_button = Button(text="Reset", bg=GREEN, command= timer_reset, font=(FONT_NAME, 15, "normal"))


center_label.grid(column=0, row=0, columnspan=3)
check_mark.grid(column=0, row=3, columnspan=3)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

window.mainloop()