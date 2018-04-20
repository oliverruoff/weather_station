# handles updates for the Tkinter gui

# Container to store variables that need to be accessed
import Model.Container as cnt
# For time management
import time
# For showing the time on time label
import datetime
# For reading temperature from sensor
import Model.sensor.temp as tmp


def update_window(view):
    '''
    Takes the Tk() object and updates the view
    Update Interval = Container.gui_update_interval
    '''
    counter = cnt.sensor_interval + 1
    while (True):
        set_time()

        if counter > cnt.sensor_interval:
            counter = 0
            set_temp()
            set_humi()
        else:
            counter +=1

        view.update()
        time.sleep(cnt.gui_update_interval)

def set_time():
    '''
    Sets the time on the time label of the gui
    '''
    cnt.time_label['text'] = (str(datetime.datetime.now().strftime("%H:%M")))

def set_temp():
    '''
    Sets the temp on the temp label of the gui
    '''
    cnt.temp_label['text'] = str(tmp.get_temp_humid()[1]),'°C'

def set_humi():
    '''
    Sets the humidity on the humidity label of the gui
    '''
    cnt.humi_label['text'] = str(tmp.get_temp_humid()[0]), '%'
