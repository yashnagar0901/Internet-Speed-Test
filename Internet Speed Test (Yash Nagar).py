from tkinter import *
import speedtest


def speed_check():
    tk = speedtest.Speedtest()
    tk.get_servers()
    down_speed = str(round(tk.download()/(10**6), 3)) + "Mbps"
    up = str(round(tk.upload()/(10**6), 3)) + "Mbps"
    lab_down.config(text=down_speed)
    lab_up.config(text=up)


tk = Tk()
tk.title("Internet Speed Checker")
tk.geometry("500x550")


font_family_header = "Baufra", 25, "bold"
font_family_subheader = "Helvetica", 20, "bold"
font_family_btn = "Helvetica", 20, "bold"
font_family_number = "Helvetica", 20, "bold"
font_color_heading = "#000000"
font_color_number = "#FFFFFF"
font_color_btn = "#000000"
background_color = "#306EFF"
button_color = "#2B547E"

tk.config(bg=background_color)

lab = Label(tk, text="Internet speed Test", font=font_family_header,
            fg=font_color_heading, bg=background_color)
lab.place(x=75, y=40, height=50, width=350)


lab = Label(tk, text="Downloading", font=font_family_subheader,
            fg=font_color_heading, bg=background_color)
lab.place(x=85, y=130, height=50, width=330)


lab_down = Label(tk, text="00", font=font_family_number,
                 fg=font_color_number, bg=background_color)
lab_down.place(x=85, y=200, height=50, width=330)


lab = Label(tk, text="Uploading", font=font_family_subheader,
            fg=font_color_heading, bg=background_color)
lab.place(x=85, y=290, height=50, width=330)


lab_up = Label(tk, text="00", font=font_family_number,
               fg=font_color_number, bg=background_color)
lab_up.place(x=85, y=360, height=50, width=330)


button = Button(tk, text="TEST HERE", fg=font_color_btn,
                bg=button_color, font=font_family_btn, relief=RAISED, command=speed_check)
button.place(x=85, y=450, height=50, width=330)


tk.mainloop()