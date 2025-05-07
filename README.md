# Fatigue Alarm Script for Ubuntu

This Python script displays a full-screen fatigue alarm on Ubuntu (or other systems with Tkinter support) at regular intervals. It's designed to remind users to take short breaks, helping to prevent eye strain and fatigue from prolonged computer use.

## Features

* **Full-Screen Alert:** Grabs your attention with a full-screen notification.
* **Configurable Interval:** Set how often the alarm appears (default is 20 minutes).
* **Visual Countdown:** A progress bar shows a 20-second countdown before the alarm auto-closes.
* **Manual Dismissal:** Close the alarm immediately by pressing any key or clicking the mouse.
* **Customization Appearance:** Easily change background and text colors in the script.
* **Looping:** Runs continuously until manually stopped.

## Prerequisites

* **Python 3:** The script is written for Python 3.
* **Tkinter:** This is the standard Python interface to the Tk GUI toolkit. It's usually included with Python, but if not, you can install it.

## Installation

1.  **Clone the repository or download the script:**
    If you have this script as part of a Git repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    Otherwise, simply download the Python script file (e.g., `fatigue_alarm.py`).

2.  **Install Tkinter (if not already installed):**
    On Debian-based systems like Ubuntu, you can install Tkinter using apt:
    ```bash
    sudo apt-get update
    sudo apt-get install python3-tk
    ```
    For other operating systems, please refer to their respective package managers or Python installation guides.

## How to Run

1.  Navigate to the directory where you saved the script.
2.  Execute the script using Python 3:
    ```bash
    python3 fatigue_alarm.py
    ```
    (Replace `fatigue_alarm.py` with the actual filename if you named it differently).

Upon running, the script will print a confirmation message in the terminal and the first alarm will appear after the configured interval (default 20 minutes).

## How it Works

* The script runs in an infinite loop.
* Every `alarm_interval_minutes` (default: 20), it calls the `display_fatigue_alarm()` function.
* This function creates a full-screen Tkinter window with:
    * A customizable fatigue alert message.
    * A progress bar counting down from `timeout_seconds` (default: 20).
    * A label showing the remaining seconds.
* The alarm window can be closed by:
    * Pressing any key.
    * Clicking the mouse.
    * Waiting for the 20-second timeout.
* After the alarm window is closed (or times out), the script waits for the next interval.

## Stopping the Script

To stop the script, go to the terminal window where it's running and press `Ctrl+C`.

## Customization

You can modify the script to change its behavior:

* **Alarm Interval:**
    Change the `alarm_interval_minutes` variable in the `if __name__ == "__main__":` block:
    ```python
    alarm_interval_minutes = 30 # Change to 30 minutes, for example
    ```

* **Alarm Duration (Timeout):**
    Change the `timeout_seconds` variable inside the `display_fatigue_alarm()` function:
    ```python
    timeout_seconds = 30 # Change to 30 seconds, for example
    ```

* **Colors:**
    Modify the color strings (e.g., `'yellow'`, `'red'`) for `bg` (background) and `fg` (foreground/text) properties of the `root` window, `center_frame`, `message_label`, and `time_remaining_label` within the `display_fatigue_alarm()` function.
    ```python
    # Example: Change to a blue background with white text
    root.configure(bg='blue')
    center_frame.configure(bg='blue')
    message_label.configure(fg="white", bg="blue")
    time_remaining_label.configure(fg="white", bg="blue")
    ```

* **Alarm Message:**
    Edit the `text` property of the `message_label` inside `display_fatigue_alarm()`:
    ```python
    message_label = tk.Label(
        center_frame,
        text="Time for a quick break!\nLook away from the screen.", # Your custom message
        # ... other properties
    )
    ```

## Troubleshooting

* **"couldn't connect to display" or "no display name and no $DISPLAY environment variable":**
    This error means Tkinter cannot find a graphical display to draw the window.
    * Ensure you are running this on a system with a desktop environment (not a headless server).
    * If using SSH, try connecting with X11 forwarding enabled: `ssh -X user@host`.

## Contributing

Feel free to fork this script, suggest improvements, or submit pull requests if you have any enhancements!

## License

This script is provided as-is. You are free to use, modify, and distribute it.
