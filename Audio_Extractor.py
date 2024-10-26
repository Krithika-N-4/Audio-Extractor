#Video2Audio
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def error_msg_1():
    # Create a root window (optional, can be hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    # Show an information message box
    messagebox.showerror("Error", "Please select a video file.")

def error_msg_2():
    
    root = tk.Tk()
    root.withdraw()

    messagebox.showerror("Warning", "Could not read or process the file.")

def error_msg_3():
    
    root = tk.Tk()
    root.withdraw()

    messagebox.showerror("Warning", f"An unexpected error occurred: {e}")

def completed():    
    
    root = tk.Tk()
    root.withdraw() 

    messagebox.showinfo("Completed", "Audio is successfully extracted from the video.")

def select_file():
    
    global file_path
    # Create a root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog and get the selected file path
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py"),("Video Files", "*.mp4")]
    )
        
try:
    select_file()
    
    if not file_path:
        error_msg_1()
    
    if file_path[-3:] != "mp4":
        error_msg_1()

    cvt_video = mp.VideoFileClip(file_path)

    ext_audio = cvt_video.audio

    ext_audio.write_audiofile("Extracted_audio.mp3")
    
    completed()

except OSError as os_error:
    error_msg_2()

except Exception as e:
    error_msg_3()

finally:
    # Clean up any resources, if necessary
    if 'cvt_video' in locals():
        cvt_video.close()
