# main.py

import tkinter as tk
from gui import App
import torch

def run_application():
    # Check if GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Create root GUI window
    root = tk.Tk()

    # Create App object with device argument
    app = App(root, device=device)

    # Run the application
    root.mainloop()

# Only run the application if this script is executed, not when imported
if __name__ == "__main__":
    run_application()
