# **NeverLock2**: The Virtual Drinking Bird ... Windows Edition!
### _A Simple way keep your desktop from going to sleep_

## **Overview**:
**NeverLock2** is a [Python](https://www.python.org/) app that keeps your Windows desktop from going to sleep by periodically pressing keys. This effectively disables auto-lock, screensavers, power-save sleep timers, and usually keeps you *active* in chat apps. It is written using Python 3 and requries the [pyautogui](https://pyautogui.readthedocs.io/) and [infi.systray](https://github.com/Infinidat/infi.systray) packages.

## **Basic Setup**:
1) Make sure you have Python 3 setup correctly
2) Clone this repository:
```
git clone https://github.com/mptsolutions/NeverLock2.git
```
3) Install ```pyautogui``` and ```infi.systray```
```
pip install pyautogui
pip install infi.systray
```

## **Operation** 
The entire app is contained in the single ```never_lock2.pyw``` file, so it can be run as any other basic Python script. 
```
D:\PythonProjects\NeverLock2> python never_lock.pyw
```
At specific intervals, **NeverLock2** will press the ```volume down``` key and then the ```volume up``` key.  These keys have been chosen because they work on most systems and ensure that no open applications are affected. You can leave **NeverLock2** running even while you are using the computer and it should not have any affect on what you are doing. Note that on some systems a volume adjustment notification will appear on the screen when **NeverLock2** activates. Once running, **NeverLock2** will create an icon in the system tray. The button press frequency can be controlled by right-clicking the icon and choosing the desired option. **NeverLock2** can by stopped by choosing 'Quit' from the tray icon menu.

**NeverLock2** is intended for use as a Windows app. If you are using Linux, or simply prefer a command-line version, see https://github.com/mptsolutions/NeverLock.