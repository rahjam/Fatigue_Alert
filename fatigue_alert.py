import tkinter as tk
from tkinter import ttk
import time


def display_fatigue_alarm():
    """
    Displays a full-screen fatigue alarm window with a progress bar.
    The window closes after 20 seconds or when any key is pressed.
    """
    root = tk.Tk()
    root.title("Fatigue Alarm")
    # Make the window full-screen
    root.attributes("-fullscreen", True)
    # Set background color to yellow
    root.configure(bg="yellow")

    # A frame to center content in the full-screen window
    # Set frame background to yellow as well
    center_frame = tk.Frame(root, bg="yellow")
    center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Alarm message
    message_label = tk.Label(
        center_frame,
        text="!!Fatigue Alert!!\n\nPlease take a moment to rest and relax your eyes.",
        font=("Tahoma", 40, "bold"),  # Readable and large font
        fg="red",  # Text color red
        bg="yellow",  # Label background color yellow
        justify=tk.CENTER,  # For multi-line messages
        wraplength=root.winfo_screenwidth()
        * 0.8,  # Limit text width for better readability
    )
    message_label.pack(pady=50)

    # Progress bar for the 20-second countdown
    # Style the progress bar if needed, though default often works well
    style = ttk.Style()
    style.theme_use("clam")  # 'clam', 'alt', 'default', 'classic' are options
    style.configure(
        "yellow.Horizontal.TProgressbar",
        foreground="red",
        background="red",
        troughcolor="lightgrey",
    )  # troughcolor is the bar's track

    progress_bar = ttk.Progressbar(
        center_frame,
        orient="horizontal",
        length=root.winfo_screenwidth()
        * 0.6,  # Progress bar length proportional to screen width
        mode="determinate",
        style="yellow.Horizontal.TProgressbar",  # Apply custom style if needed, or remove for default
    )
    progress_bar.pack(pady=30)

    # Label to display remaining time
    time_remaining_label = tk.Label(
        center_frame,
        text="",  # Text is set by the update function
        font=("Tahoma", 20),
        fg="red",  # Text color red
        bg="yellow",  # Background color yellow
    )
    time_remaining_label.pack(pady=20)

    timeout_seconds = 20
    current_elapsed_time = 0
    timer_id_after = None  # To store the 'after' timer ID

    def close_alarm_window(event=None):
        """Closes the alarm window and cancels the 'after' timer."""
        nonlocal timer_id_after
        if timer_id_after:
            root.after_cancel(timer_id_after)
            timer_id_after = None
        root.destroy()

    # Close window on any key press
    root.bind("<Key>", close_alarm_window)
    # Closing the window with a mouse click can also be useful
    root.bind("<Button-1>", close_alarm_window)

    def update_progress_and_timer():
        """Updates the progress bar and remaining time. Closes the window if time runs out."""
        nonlocal current_elapsed_time, timer_id_after
        current_elapsed_time += 1
        progress_value = (current_elapsed_time / timeout_seconds) * 100
        progress_bar["value"] = progress_value

        seconds_left = timeout_seconds - current_elapsed_time
        time_remaining_label.config(text=f"Auto-closing in {seconds_left} seconds")

        if current_elapsed_time < timeout_seconds:
            timer_id_after = root.after(
                1000, update_progress_and_timer
            )  # Update every 1 second
        else:
            close_alarm_window()

    # Ensure the window is displayed at the top level
    root.lift()
    root.attributes("-topmost", True)

    # Start countdown and progress bar update
    update_progress_and_timer()

    root.mainloop()


if __name__ == "__main__":
    alarm_interval_minutes = 2
    # Tkinter might not be installed by default.
    # On Ubuntu/Debian: sudo apt-get install python3-tk
    print(
        f"Fatigue alarm program activated. An alarm will be displayed every {alarm_interval_minutes} minutes."
    )
    print("To stop the program, close this terminal or press Ctrl+C.")

    try:
        while True:
            display_fatigue_alarm()
            print(
                f"Alarm displayed. Waiting for {alarm_interval_minutes} minutes until the next alarm..."
            )
            time.sleep(alarm_interval_minutes * 60)
    except KeyboardInterrupt:
        print("\nFatigue alarm program stopped by user.")
    except tk.TclError as e:
        if (
            "display name" in str(e).lower()
            or "couldn't connect to display" in str(e).lower()
        ):
            print(f"Tkinter error: {e}")
            print("It seems that a graphical environment (like X11) is not available.")
            print("This script requires a display server to run.")
            print(
                "If you are connected via SSH, try using 'ssh -X' or ensure X11 forwarding is enabled."
            )
        else:
            print(f"A Tkinter error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
