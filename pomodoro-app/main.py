from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    global TIMER
    if TIMER is not None:
        window.after_cancel(TIMER)
        TIMER = None
        timer_label.config(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
        canvas.itemconfig(timer_text, text=f"00:00")
        REPS = 0
        checkmark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        start_button.config(state=ACTIVE)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    start_button.config(state=DISABLED)
    REPS += 1
    if REPS == 10:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=PINK, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
        REPS = 0
    elif REPS % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK, bg=YELLOW, font=(FONT_NAME, 45, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"{0}{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        if REPS == 0:
            checkmark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        elif REPS % 2 != 0:
            check = checkmark.cget("text") + "✓"
            checkmark.config(text=check, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()