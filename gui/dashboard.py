import customtkinter as ctk
import sys
import os

# Allow importing from src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import get_dashboard_data


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure((0, 1), weight=1)

        heading = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )
        heading.grid(row=0, column=0, columnspan=2, pady=(20, 30))

        self.load_dashboard()

    def load_dashboard(self):

        data = get_dashboard_data()

        cards = [
            ("🚗 Total Vehicles", data["vehicles"]),
            ("👤 Customers", data["customers"]),
            ("📋 Rentals", data["rentals"]),
            ("💰 Revenue", f"₹{data['revenue']}")
        ]

        positions = [
            (1, 0),
            (1, 1),
            (2, 0),
            (2, 1)
        ]

        for (title, value), (r, c) in zip(cards, positions):

            card = ctk.CTkFrame(
                self,
                corner_radius=15,
                height=140
            )

            card.grid(row=r, column=c, padx=20, pady=20, sticky="nsew")

            label = ctk.CTkLabel(
                card,
                text=title,
                font=("Arial", 18)
            )
            label.pack(pady=(25, 10))

            number = ctk.CTkLabel(
                card,
                text=str(value),
                font=("Arial", 32, "bold")
            )
            number.pack()