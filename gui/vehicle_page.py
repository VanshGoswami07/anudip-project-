import customtkinter as ctk


class VehiclePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="🚗 Vehicle Management",
            font=("Arial",30,"bold")
        )

        title.pack(pady=30)

        label = ctk.CTkLabel(
            self,
            text="Vehicle CRUD will be built here.",
            font=("Arial",18)
        )

        label.pack()