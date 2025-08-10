Network Ping Monitor
Hey! This is a simple Python script that helps you check if devices on your network are online or offline.

What it does
It sends a ping to devices by their IP or hostname.

Shows you right in the console whether each device is up or down.

Saves a report with the status in a text file so you can look back anytime.

How to get started
Make sure you have Python 3 installed.

Add the devices you want to check inside the devices list in network_monitor.py.

Run the script like this:

bash
Copy
Edit
python network_monitor.py
You’ll see the status printed on screen, and it’ll also save a report in report.txt.

How it works
The ping(host) function sends a ping to the device and sees if it replies.

The report(devices) function goes through each device and checks their status.

The save(report, file_name) function writes the report to a file.

The if __name__ == "__main__": part makes sure the main code runs only when you run the script directly.

What you could add next
Sending the report by email automatically

Running the ping repeatedly to watch devices in real-time

Keeping detailed logs with timestamps

Building a simple web or graphical interface for easier use
