""" My Apps
See Apps in tray
File: snitray.py
"""

import dbus
import dbus.service

import vars


class Apps:
    """ Apps """
    __shm_path = '/dev/shm/%s' % vars.SERVICE_BUS_NAME

    def __init__(self):
        self.__bus = dbus.SessionBus()

    def get_bus_props(self, name) -> str:
        """ Get Title prop by DBus name """
        try:
            proxy = self.__bus.get_object(name, vars.ITEM_OBJECT_PATH)
            iface = dbus.Interface(proxy, dbus_interface=vars.DBUS_PROPERTIES)
            props = iface.GetAll(vars.ITEM_INTERFACE)
            return str(props['Title'])
        except dbus.exceptions.DBusException:
            return ''

    def shm_bus_names(self):
        """ Read cache file """
        with open(self.__shm_path, 'r') as file:
            line = file.readline()
            cnt = 1
            while line:
                yield line.strip()
                line = file.readline()
                cnt += 1

    def items(self):
        """ Collect apps names """
        items = []
        for name in self.shm_bus_names():
            props = self.get_bus_props(name)
            if not props:
                continue
            items.append(props)
        return items


def main():
    """ Init """
    apps_iface = Apps()
    apps_list = apps_iface.items()
    print(apps_list)


if __name__ == '__main__':
    main()
