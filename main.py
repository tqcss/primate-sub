import customtkinter
from PIL import Image
import pyautogui
import keyboard
import json

VERSION = 'v0.1.1'
SCREEN_SIZE = pyautogui.size()

customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('color-theme.json')


class Window:
    def __init__(self, width: int, height: int, overrideredirect: bool=False):
        center_width = SCREEN_SIZE.width // 2 - width // 2
        center_height = SCREEN_SIZE.height // 2 - height // 2

        self.root = customtkinter.CTk()
        self.root.overrideredirect(overrideredirect)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, center_width, center_height))

    def display(self):
        self.root.mainloop()


class SplashScreen(Window):
    def __init__(self, width: int, height: int) -> object:
        super().__init__(width=width, height=height, overrideredirect=True)
        self.LIGHT_BG_IMG = None #! Missing Asset
        self.DARK_BG_IMG = Image.open('assets/god-icon.png')

        self.FONT1 = 'Lucida Console'
        self.FONT2 = 'Arial'

        self.bg_size = (500, 500)
        self.duration = 5 # time splash screen should display in seconds

        # Root Properties
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.attributes('-topmost', True)

        # Frame (Inner box)
        frame = customtkinter.CTkFrame(master=self.root)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        # Background Image
        image = customtkinter.CTkImage(light_image=self.LIGHT_BG_IMG, dark_image=self.DARK_BG_IMG, size=self.bg_size)
        image_label = customtkinter.CTkLabel(frame, image=image, text='')
        image_label.place(x=-60, anchor='nw')

        # Title
        title = customtkinter.CTkLabel(master=frame, text='Primate', font=(self.FONT1, 35))
        title.place(relx=0.75, rely=0.45, anchor='center')

        # Version Label
        version_label = customtkinter.CTkLabel(master=frame, text=VERSION, font=(self.FONT2, 16), text_color='#384856')
        version_label.place(relx=0.75, rely=0.55, anchor='center')

        # Watermark
        watermark = customtkinter.CTkLabel(master=frame, text='@returned_nil', font=(self.FONT1, 12), text_color='#384856')
        watermark.place(x=-12, relx=1, rely=1, anchor='se')

    def display(self):
        self.root.after(self.duration * 1000, lambda: self.root.destroy())
        self.root.mainloop()


splash_screen = SplashScreen(600, 350)
splash_screen.display()
