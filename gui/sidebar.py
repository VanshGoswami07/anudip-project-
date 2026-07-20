import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):
        super().__init__(parent, width=200, corner_radius=0)

        self.callback = callback

        title = ctk.CTkLabel(
            self,
            text="🚗 Vehicle Rental",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=(25, 40))

        pages = [
            "Dashboard",
            "Vehicles",
            "Customers",
            "Rentals",
            "Billing",
            "Exit"
        ]

        for page in pages:

            btn = ctk.CTkButton(
                self,
                text=page,
                height=42,
                command=lambda p=page: self.callback(p)
            )

            btn.pack(fill="x", padx=12, pady=8)