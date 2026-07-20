import customtkinter as ctk


class RentalPage(ctk.CTkFrame):

    def __init__(self,parent):
        super().__init__(parent)

        title=ctk.CTkLabel(
            self,
            text="📋 Rental Management",
            font=("Arial",30,"bold")
        )

        title.pack(pady=30)