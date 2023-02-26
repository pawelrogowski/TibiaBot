import subprocess

def get_tibia_windows():
    command_output = subprocess.check_output("wmctrl -l | grep 'Tibia - '", shell=True)
    if command_output:
        lines = command_output.decode("utf-8").split("\n")
        if lines:
            windows = [line.split("-")[-1].strip() for line in lines]
            return windows

    print("Tibia windows not found.")
    return []


def get_window_id():
    # Use the subprocess module to run the wmctrl command and capture its output
    output = subprocess.check_output("wmctrl -l | grep 'Tibia - Nighttide'", shell=True)

    # Extract the window ID from the output using string manipulation
    window_id = output.decode().split()[0]

    return window_id
