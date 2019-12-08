#!/bin/env python3
# statusnotifierwatcher.py

import dbus
import dbus.service

SERVICE_NAME = 'StatusNotifierWatcher'
SERVICE_BUS_NAME = 'org.kde.%s' % SERVICE_NAME
SERVICE_OBJECT_PATH = '/%s' % SERVICE_NAME

ITEM_NAME = 'StatusNotifierItem'
ITEM_OBJECT_PATH = '/%s' % ITEM_NAME
ITEM_INTERFACE = 'org.kde.%s' % ITEM_NAME

class StatusNotifierWatcher(dbus.service.Object):
    __shm_path = '/dev/shm/%s' % SERVICE_BUS_NAME
    def __init__(self):
        self.__bus = dbus.SessionBus()
        name = dbus.service.BusName(SERVICE_BUS_NAME, bus=self.__bus)
        super().__init__(name, SERVICE_OBJECT_PATH)
    def shm_flush(self):
        with open(self.__shm_path, 'w+') as file:
            file.write('')
    def shm_add(self, value: str):
        with open(self.__shm_path, 'a') as file:
            file.write('%s\r\n' % value)
    def watch(self):
        self.shm_flush()
        return True
    @dbus.service.method(SERVICE_BUS_NAME)
    def RegisterStatusNotifierItem(self, item):
        self.shm_add(item)
        print(ITEM_OBJECT_PATH, item)
        return None

if __name__ == '__main__':
    import dbus.mainloop.glib
    from gi.repository import GLib
    
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    
    loop = GLib.MainLoop()
    snw = StatusNotifierWatcher()
    snw.watch()
    loop.run()