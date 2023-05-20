# This script creates a transparent window that covers the top
# of the screen and stays on top of other windows. 
# This is done to disable the UI (X) button that appears when the 
# user puts their cursor at the top of the display when using
# edge-dev browser in fullscreen.

import tkinter as tk

# Create a root window with no title bar or borders
root = tk.Tk()
root.overrideredirect(True)

# Set the window size
root.geometry("1920x20+0+0")

# Keep the window on top of other windows
root.attributes("-topmost", True)

# Make the window transparent
root.attributes("-alpha", 0.0)
root.configure(bg='')

# Start the main loop
root.mainloop()
