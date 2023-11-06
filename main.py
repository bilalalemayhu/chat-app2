import customtkinter as ctk

import socket as sc
import sys



ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()  

        self.resizable(False, False)

        self.title("chat app")

        self.geometry("600x600")

        self.start_Page = Start_Page(self)
        self.start_Page.pack(padx= 0, pady= 0, fill="both", expand= True)

        self.register_Page = Register_Page(self)
        self.register_Page.pack(padx= 0, pady= 0, fill="both", expand= True)
        self.register_Page.forget()

     
        



    

class Start_Page(ctk.CTkFrame):
    def __init__(self, master):

        super().__init__(master, fg_color="#0E1A4E")

        def register():
            master.register_Page.pack(padx= 0, pady= 0, fill="both", expand= True)
            self.forget()

       


        def login(brukernavn, passord):
            if username != var1 or passord != var2:
                print("wrong password or username")
            else:
                print("succes")
                

        def chat():
            print("chat succesfull")

        def addFriend():
            print("friend added")

        self.label = ctk.CTkLabel(self, text= "login", text_color="green", font=("roboto", 20), width=200, corner_radius= 150)
        self.label.pack(pady=100, padx=12)

        self.user_Entry= ctk.CTkEntry(self, placeholder_text = "brukernavn" )
        self.user_Entry.pack(pady = 2, padx= 12, anchor='center')

        self.passord_Entry = ctk.CTkEntry(self, placeholder_text = "Passord")
        self.passord_Entry.pack(pady= 2, padx= 12)

        self.login_Btn = ctk.CTkButton(self, text="login", 
        command= lambda: login(self.user_Entry.get(), self.passord_Entry.get()),
        width=140)
        self.login_Btn.pack(pady=8, padx= 12)
        

        self.signin_btn = ctk.CTkButton(self, text="registrer", command= register, width=140)
        self.signin_btn.place(relx=1, rely=0, anchor="ne")

    

class Register_Page(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="yellow")
            

        def signup(brukernavn, passord):
            file = open("userinformation.txt", "w")
            file.write(brukernavn)
            file.write("\n")
            file.close()

        def back():
            master.start_Page.pack(padx= 0, pady= 0, fill="both", expand= True)
            self.forget()

        self.label2 = ctk.CTkLabel(self, text= "registrer", text_color="green", font=("roboto", 20), width=200, corner_radius= 1)
        self.label2.pack(pady=100, padx=12)

        self.user_Crt= ctk.CTkEntry(self, placeholder_text = "brukernavn" )
        self.user_Crt.pack(pady = 2, padx= 12, anchor='center')

        self.passord_Crt = ctk.CTkEntry(self, placeholder_text = "Passord")
        self.passord_Crt.pack(pady= 2, padx= 12)

        self.acc_crt = ctk.CTkButton(self, text="lag bruker", 
        command= lambda: signup(self.user_Crt.get(), self.passord_Crt.get()))
        self.acc_crt.pack(pady=8, padx= 12)

        self.back_Btn = ctk.CTkButton(self, text="back", command=back)
        self.back_Btn.place(relx =1, rely=0, anchor='ne')



class chat_frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__()

     

    






app = App()


app.mainloop()