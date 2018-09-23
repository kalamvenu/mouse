import sys



if sys.platform.startswith('win'):
    import win32gui
    import win32con
    from os import getpid, system
    from threading import Timer
    import time


    def force_exit():
        pid = getpid()
        system('taskkill /pid %s /f' % pid)



    t = Timer(1, force_exit)
    t.start()
    SC_MONITORPOWER = 0xF170
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)

    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, -1)
    t.cancel()


