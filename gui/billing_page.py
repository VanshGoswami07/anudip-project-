import customtkinter as ctk


class BillingPage(ctk.CTkFrame):

    def __init__(self,parent):
        super().__init__(parent)

        title=ctk.CTkLabel(
            self,
            text="💰 Billing",
            font=("Arial",30,"bold")
        )

        title.pack(pady=30)