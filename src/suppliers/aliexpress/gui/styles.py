## \file hypotez/src/suppliers/aliexpress/gui/styles.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.aliexpress.gui """
MODE = 'debug'
""" module: src.suppliers.aliexpress.gui """
MODE = 'debug'
""" Common styling functions for UI elements """

from PyQt6 import QtWidgets

def set_fixed_size(widget: QtWidgets.QWidget, width: int, height: int):
    """ Set a fixed size for a given widget """
    widget.setFixedSize(width, height)
