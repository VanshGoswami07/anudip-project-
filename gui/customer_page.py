import customtkinter as ctk


class CustomerPage(ctk.CTkFrame):

    def __init__(self,parent):
        super().__init__(parent)

        title=ctk.CTkLabel(
            self,
            text="👤 Customer Management",
            font=("Arial",30,"bold")
        )

        title.pack(pady=30)