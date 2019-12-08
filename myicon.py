import pystray


if __name__ == '__main__':
    import dbus.mainloop.glib
    from gi.repository import GLib
    
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    
    loop = GLib.MainLoop()
    
    icon = pystray.Icon('test name')

    loop.run()