#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui
import AppKit


def main():
    
    app = QtGui.QApplication(sys.argv)
    screen_size = [(screen.frame().size.width, screen.frame().size.height)
        for screen in AppKit.NSScreen.screens()]
    w = QtGui.QWidget()
    w.resize(screen_size[0][0], screen_size[0][1])
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    w.activateWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()