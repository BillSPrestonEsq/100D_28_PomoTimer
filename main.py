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
current_time = WORK_MIN
reps = 1
CHECK_MARK = "✔"
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_pomo():
    global reps
    window.after_cancel(timer)
    reps = 1
    canvas.itemconfig(timer_text, text="00:00")
    pomo_checks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomo():
    count_down(WORK_MIN)
    step_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global reset_clicked
    global timer
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1
    work_sec = WORK_MIN * 1
    print(f"reps:{reps}, count:{count}, reset?: {reset_clicked}")

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds in range(0, 10):
        seconds = "0" + str(seconds)

    canvas_text = f"{minutes}:{seconds}"

    canvas.itemconfig(timer_text, text=canvas_text)

    if count == 0:
        reps += 1
        if reps % 8 == 0:
            count = long_break_sec
            step_label.config(text="Break", fg=RED)
            pomo_checks.config(text=f"{pomo_checks.cget('text')}{CHECK_MARK}")
        elif reps % 2 == 0:
            count = short_break_sec
            step_label.config(text="Break", fg=PINK)
            pomo_checks.config(text=f"{pomo_checks.cget('text')}{CHECK_MARK}")
        else:
            count = work_sec
            step_label.config(text="Work", fg=GREEN)
        timer = window.after(100, count_down, count)
    else:
        timer = window.after(100, count_down, count - 1)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=20, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

step_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 50), fg=GREEN)
step_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_pomo)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_pomo)
reset_button.grid(row=2, column=2)

pomo_checks = Label(text="", bg=YELLOW, font=(FONT_NAME, 20), fg=GREEN)
pomo_checks.grid(row=3, column=1)

window.mainloop()