# Import necessary modules
import tkinter as tk
from gui import App

def run_application():
    # Create root GUI window
    root = tk.Tk()

    # Create App object
    app = App(root)

    # Run the application
    root.mainloop()

# Only run the application if this script is executed, not when imported
if __name__ == "__main__":
    run_application()
