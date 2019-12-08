"""Default vars
File: vars.py
"""
DBUS_PROPERTIES = 'org.freedesktop.DBus.Properties'

SERVICE_NAME = 'StatusNotifierWatcher'
SERVICE_BUS_NAME = 'org.kde.%s' % SERVICE_NAME
SERVICE_OBJECT_PATH = '/%s' % SERVICE_NAME

ITEM_NAME = 'StatusNotifierItem'
ITEM_OBJECT_PATH = '/%s' % ITEM_NAME
ITEM_INTERFACE = 'org.kde.%s' % ITEM_NAME
