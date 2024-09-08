# Import required libraries
import tkinter as tk  # For creating the GUI
import psutil  # For getting system information
import platform  # For getting OS and Python version information


# Function to get and display system information
def get_system_info():
    # Get CPU usage as a percentage
    cpu_usage = psutil.cpu_percent()

    # Get memory usage information
    memory = psutil.virtual_memory()

    # Get disk usage information for the root directory
    disk = psutil.disk_usage('/')

    # Prepare the information string
    info = f"CPU Usage: {cpu_usage}%\n"
    info += f"Memory Usage: {memory.percent}%\n"
    info += f"Disk Usage: {disk.percent}%\n"
    info += f"OS: {platform.system()} {platform.release()}\n"
    info += f"Python Version: {platform.python_version()}"

    # Clear the text widget and insert the new information
    info_text.delete(1.0, tk.END)
    info_text.insert(tk.END, info)


# Create the main window
window = tk.Tk()
window.title("System Information")

# Create a button to refresh the system information
refresh_button = tk.Button(window, text="Refresh Info", command=get_system_info)
refresh_button.pack(pady=10)

# Create a text widget to display the system information
info_text = tk.Text(window, height=10, width=40)
info_text.pack(padx=10, pady=10)

# Initial call to populate the info when the app starts
get_system_info()

# Start the Tkinter event loop
window.mainloop()