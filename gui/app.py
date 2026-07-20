import customtkinter as ctk

from sidebar import Sidebar
from dashboard import DashboardPage
from vehicle_page import VehiclePage
from customer_page import CustomerPage
from rental_page import RentalPage
from billing_page import BillingPage

# -----------------------------
# SETTINGS
# -----------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class VehicleRentalApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Vehicle Rental Management System")
        self.geometry("1400x800")
        self.minsize(1200, 700)

        # Window Layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self, self.show_page)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Main Container
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Pages
        self.pages = {
            "Dashboard": DashboardPage(self.container),
            "Vehicles": VehiclePage(self.container),
            "Customers": CustomerPage(self.container),
            "Rentals": RentalPage(self.container),
            "Billing": BillingPage(self.container),
        }

        # Stack all pages
        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        # Show dashboard first
        self.show_page("Dashboard")

    def show_page(self, page_name):

        if page_name == "Exit":
            self.destroy()
            return

        self.pages[page_name].tkraise()


if __name__ == "__main__":
    app = VehicleRentalApp()
    app.mainloop()