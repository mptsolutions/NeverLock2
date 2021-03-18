import pyautogui
from threading import Event, Thread
from infi.systray import SysTrayIcon

"""
NeverLock: The Virtual Drinking Bird
------------------------------------
NeverLock is a Python app that keeps your desktop from going to 
sleep by periodically pressing keys. This effectively disables 
auto-lock, screensavers, power-save sleep timers, and usually 
keeps you active in chat apps. It is written using Python 3 and 
requries the pyautogui and infi.systray packages. For more 
information see the documentation at 
https://github.com/mptsolutions/NeverLock2.
"""
class NeverLock(Thread):
    def __init__(self, press_frequency):
        """
        Initialization of the class will create a new thread
        and set the default button press frequency.
        """
        Thread.__init__(self)
        self.event = Event()
        self.set_press_frequency(press_frequency)
    
    def set_press_frequency(self, press_frequency):
        """
        Function to change the press frequency. This
        function is called by the tray icon menu options.
        """
        self.press_frequency = press_frequency
    
    def start(self):
        """
        Function to handle key presses at the set frequency.
        """
        try:
            while not self.event.is_set():
                self.event.wait(self.press_frequency*60)
                pyautogui.press('volumedown')
                pyautogui.press('volumeup')
        except KeyboardInterrupt:
            pass

def stop(systray):
    """
    Function to stop the NeverLock thread on exit.
    """
    nl.event.set()

if __name__ == "__main__": 
    pyautogui.FAILSAFE = False
    nl = NeverLock(press_frequency=15)
    menu_options = ((' 5 Minutes', None, lambda x: nl.set_press_frequency(5)),
                    ('10 Minutes', None, lambda x: nl.set_press_frequency(10)),
                    ('15 Minutes', None, lambda x: nl.set_press_frequency(15)),
                    ('30 Minutes', None, lambda x: nl.set_press_frequency(30)))

    with SysTrayIcon("nl.ico", "NeverLock", menu_options, default_menu_index=4, on_quit=stop):
        nl.start()
