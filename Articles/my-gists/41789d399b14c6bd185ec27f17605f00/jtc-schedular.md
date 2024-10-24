## TL;DR

### Meeting Helper Dashboard

Zoom meeting participation is used for attendance management, and can be skipped by automating participation and recording.

Launch Zoom and Quicktime with Launchctl and Launchd. → Cut out the silence → Save.


### How

- Pass the execution policy
- cron Start a conference app (default, teams, /zoom, /discord, /telegram, /line, /session, /chrome, etc)
- cron Start a recording software (default: obs, /quicktime, etc)
- cron Take a screenshot of the active window periodically (every 30 seconds) (read crontab.txt)
- Save (to: %y%m%d-%H%M%S/{index:05d}.mkv (/ mp4 ))

- (optional) cron Take a screenshot of the active window every time audio starts after silence (silence is less than 10% of the threshold)
- (optional) Prevent going into sleep mode
- (optional) Change various values ​​to appropriate default values ​​and replace them with variables.
- (optional) Cut silence

```py
import argparse
import subprocess
import time
import os
import signal
import pygetwindow as gw
from datetime import datetime
from threading import Timer
from rich.console import Console
from PIL import ImageGrab

console = Console()

class AudioProcessor:
    def __init__(self, silence_threshold=10):
        self.silence_threshold = silence_threshold
        self.audio_active = False

    def check_audio(self):
        # Implement audio check logic here
        # For now, this is just a placeholder
        return False

class ConferenceAppLauncher:
    def __init__(self, app_name='teams'):
        self.app_name = app_name

    def start_app(self):
        try:
            subprocess.Popen(self.app_name)
        except Exception as e:
            console.log(f"Error starting conference app: {e}")

class RecordingSoftware:
    def __init__(self, software='obs'):
        self.software = software

    def start_recording(self):
        try:
            subprocess.Popen(self.software)
        except Exception as e:
            console.log(f"Error starting recording software: {e}")

class ScreenshotTaker:
    def __init__(self, interval=30):
        self.interval = interval
        self.index = 0
        self.directory = datetime.now().strftime("%Y%m%d-%H%M%S")
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def take_screenshot(self):
        window = gw.getActiveWindow()
        if window:
            screenshot = ImageGrab.grab(bbox=(window.left, window.top, window.right, window.bottom))
            filename = os.path.join(self.directory, f"{self.index:05d}.png")
            screenshot.save(filename)
            self.index += 1
        else:
            console.log("No active window found.")
        self.schedule_next_screenshot()

    def schedule_next_screenshot(self):
        Timer(self.interval, self.take_screenshot).start()

class PreventSleep:
    @staticmethod
    def prevent_sleep():
        try:
            if os.name == 'nt':  # Windows
                subprocess.run('powercfg /change monitor-timeout-ac 0', shell=True)
                subprocess.run('powercfg /change monitor-timeout-dc 0', shell=True)
            elif os.name == 'posix':  # Unix/Linux/Mac
                subprocess.run('caffeinate', shell=True)
        except Exception as e:
            console.log(f"Error preventing sleep mode: {e}")

def parse_args():
    parser = argparse.ArgumentParser(description="Automate conference setup")
    parser.add_argument('--conference_app', type=str, default='teams', help='Conference app to launch')
    parser.add_argument('--recording_software', type=str, default='obs', help='Recording software to launch')
    parser.add_argument('--screenshot_interval', type=int, default=30, help='Interval between screenshots in seconds')
    parser.add_argument('--prevent_sleep', action='store_true', help='Prevent system from sleeping')
    return parser.parse_args()

def signal_handler(sig, frame):
    console.log("Exiting gracefully")
    sys.exit(0)

def main():
    args = parse_args()
    signal.signal(signal.SIGINT, signal_handler)

    conference_app = ConferenceAppLauncher(args.conference_app)
    recording_software = RecordingSoftware(args.recording_software)
    screenshot_taker = ScreenshotTaker(args.screenshot_interval)
    audio_processor = AudioProcessor()

    console.log("Starting conference app...")
    conference_app.start_app()
    time.sleep(5)  # Wait for the app to start

    console.log("Starting recording software...")
    recording_software.start_recording()
    time.sleep(5)  # Wait for the software to start

    console.log("Starting periodic screenshot taker...")
    screenshot_taker.schedule_next_screenshot()

    if args.prevent_sleep:
        console.log("Preventing system from sleeping...")
        PreventSleep.prevent_sleep()

    while True:
        if audio_processor.check_audio():
            console.log("Audio activity detected. Taking screenshot...")
            screenshot_taker.take_screenshot()
        time.sleep(1)

if __name__ == '__main__':
    main()
```