import subprocess

def send_key(key, window_name):
    # Find the window ID for the window with the specified name
    window_id = subprocess.check_output(['xdotool', 'search', '--name', window_name]).strip().decode()
    subprocess.run(['xdotool', 'key', '--window', window_id, key])
