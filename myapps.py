#!/bin/env python3
# snitray.py

import dbus
import dbus.service

DBUS_PROPERTIES = 'org.freedesktop.DBus.Properties'

SERVICE_NAME = 'StatusNotifierWatcher'
SERVICE_BUS_NAME = 'org.kde.%s' % SERVICE_NAME
SERVICE_OBJECT_PATH = '/%s' % SERVICE_NAME

ITEM_NAME = 'StatusNotifierItem'
ITEM_OBJECT_PATH = '/%s' % ITEM_NAME
ITEM_INTERFACE = 'org.kde.%s' % ITEM_NAME

class Apps:
    """docstring for Apps"""
    __shm_path = '/dev/shm/%s' % SERVICE_BUS_NAME
    def __init__(self):
        self.__bus = dbus.SessionBus()
    def get_bus_props(self, name):
        try:
            proxy = self.__bus.get_object(name, ITEM_OBJECT_PATH)
            iface = dbus.Interface(proxy, dbus_interface=DBUS_PROPERTIES)
            props = iface.GetAll(ITEM_INTERFACE)
            return str(props['Title'])
        except dbus.exceptions.DBusException as e:
            return None
    def shm_bus_names(self):
        names = []
        with open(self.__shm_path, 'r') as fp:
            line = fp.readline()
            cnt = 1
            while line:
                yield line.strip()
                line = fp.readline()
                cnt += 1

    def items(self):
        items = []
        for name in self.shm_bus_names():
            props = self.get_bus_props(name)
            if not props:
                continue
            items.append(props)
        return items

def main():
    apps_iface = Apps()
    apps_list = apps_iface.items()
    print(apps_list)

if __name__ == '__main__':
    main()
