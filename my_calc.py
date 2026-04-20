import tkinter

button_values = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "*"],
    [".", "0", "=", "/"]
]

row_count = len(button_values)
column_count = len(button_values[0])

right_symbols = ["+", "-", "*", "/"]


colour_purpleish = "#67637C"
colour_beigeish = "#F1D1AB"
colour_beiger = "#C7B999"
colour_maroonish = "#8B5C67"
colour_white = "#FFFFFF"
colour_grey = "#808080"

window = tkinter.Tk()  # creates a window
window.title("Calculator")
window.resizable(False, False)
frame = tkinter.Frame(window)
label = tkinter.Label(frame, text='0', font=("Arial", 24), bg=colour_grey, fg=colour_white,anchor="e")
label.grid(column=0, row=0, columnspan=column_count,sticky="we")

current = ""

def button_clicked(value):
    global current
    if value == "=":
        try:
            result = str(eval(current))
            label.config(text=result)
            current = result
        except:
            label.config(text="Error")
            current = ""
    else:
        current += value
        label.config(text=current)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count - 1, height=1,
                                command=lambda v=value: button_clicked(v))
        
        if value in right_symbols:
            button.config(fg=colour_white, bg=colour_maroonish)
        else:
            button.config(fg=colour_beiger, bg=colour_maroonish)    
        button.grid(row=row+1, column=column)

frame.pack()
window.update()
window_width = window.winfo_width()
window_height= window.winfo_height()
screen_width = window.winfo_width()
screen_height = window.winfo_height()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()



