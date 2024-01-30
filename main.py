import customtkinter
import pyautogui
import keyboard
import json

SCREEN_SIZE = pyautogui.size()

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('main-theme.json')

def display_splash_screen():
    WIDTH = 600
    HEIGHT = 350
    CENTER_WIDTH = SCREEN_SIZE.width // 2 - WIDTH // 2
    CENTER_HEIGHT = SCREEN_SIZE.height // 2 - HEIGHT // 2

    splash_window = customtkinter.CTk()
    splash_window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, CENTER_WIDTH, CENTER_HEIGHT))
    splash_window.overrideredirect(True)
    
    title = customtkinter.CTkLabel(master=splash_window, text='Booga Beast', font=('Lucida Console', 24))
    title.place(relx=0.5, rely=0.5, anchor='center')

    splash_window.after(5000, lambda: splash_window.destroy())
    splash_window.mainloop()


display_splash_screen()
