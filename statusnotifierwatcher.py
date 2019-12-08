"""DBus Service: Status Notifier Watcher
File: statusnotifierwatcher.py
"""

import dbus
import dbus.service

import vars


class StatusNotifierWatcher(dbus.service.Object):
    """ Status Notifier Watcher """
    __shm_path = '/dev/shm/%s' % vars.SERVICE_BUS_NAME

    def __init__(self):
        self.__bus = dbus.SessionBus()
        name = dbus.service.BusName(vars.SERVICE_BUS_NAME, bus=self.__bus)
        super().__init__(name, vars.SERVICE_OBJECT_PATH)

    def shm_flush(self):
        """ Cleanup /dev/shm """
        with open(self.__shm_path, 'w+') as file:
            file.write('')

    def shm_add(self, value: str):
        """ Add DBus app name to /dev/shm """
        with open(self.__shm_path, 'a') as file:
            file.write('%s\r\n' % value)

    def watch(self):
        """ Init Watcher """
        self.shm_flush()
        return True

    @dbus.service.method(vars.SERVICE_BUS_NAME)
    def RegisterStatusNotifierItem(self, item: str):
        """ DBus method: RegisterStatusNotifierItem """
        self.shm_add(item)
        print(vars.ITEM_OBJECT_PATH, item)


if __name__ == '__main__':
    import dbus.mainloop.glib
    from gi.repository import GLib
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    LOOP = GLib.MainLoop()
    SNW = StatusNotifierWatcher()
    SNW.watch()
    LOOP.run()
