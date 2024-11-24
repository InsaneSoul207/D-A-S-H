import psutil
import threading
def battery_perc():
    battery=psutil.sensors_battery()
    perc = int(battery.percent)
    return f"The device is running on {perc}% battery power"
def battery_status():
    battery=psutil.sensors_battery()
    if battery.power_plugged:
        return "The device is currently plugged in"
    else:
        return "The device is currently unplugged"
def battery_time():
    battery=psutil.sensors_battery()
    time = int(battery.secsleft/60)
    return f"The device will run for {time} minutes"
