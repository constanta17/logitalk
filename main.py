from customtkinter import *
from PIL import Image

class AuthWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')
        self.title('Вхід')
        self.resizable(True, False)

        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side='left',fill='both')
        img_ctk = CTkImage(light_image=Image.open('img/bg.png'), size=(450,400))
        self.img_label = CTkLabel(self.left_frame, text='Welcome', image=img_ctk, text_color="white", font=('Montserrat', 60, 'bold'))
        self.img_label.pack()

        main_font = ('Montserrat', 20, 'bold')
        self.right_frame = CTkFrame(self, fg_color='white')
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side='right', fill='both', expand='True')

        CTkLabel(self.right_frame, text='LogiTalk', font=main_font, text_color="#6753cc").pack(pady=60)
        self.name_entry = CTkEntry(self.right_frame, placeholder_text='Ім`я',
                                   font=main_font, fg_color='#e6e2fa',
                                   text_color='#6753cc',
                                   placeholder_text_color="#6753cc",
                                   corner_radius=25, height=45,
                                   border_color='#eaeaea')
        self.name_entry.pack(fill='x', padx=10)
        img_set = CTkImage(light_image=Image.open('img/setting.png'), size=(20,20))
        self.setting_button = CTkButton(self.right_frame, text='Налаштування', image=img_set,
                                    corner_radius=25, height=45,
                                    border_color="#eaeaea", fg_color="#e6e2fa",
                                    text_color='#6753cc', font=main_font)
        self.setting_button.pack(fill='x', padx=10, pady=5)


        self.connect_button = CTkButton(self.right_frame, text='Увійти',
                                    corner_radius=25, height=45,
                                    border_color='#6753cc', fg_color='#6753cc',
                                    text_color='#eaeaea', font=main_font)
        self.connect_button.pack(fill='x', padx=50, pady=10)
win = AuthWindow()
win.mainloop()