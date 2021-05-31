#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import ipgetter
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QAbstractNativeEventFilter, QAbstractEventDispatcher
import cpf
import signal
from pyqtkeybind import keybinder
from requests import get
# from pynput import keyboard


class WinEventFilter(QAbstractNativeEventFilter):
    def __init__(self, keybinder):
        self.keybinder = keybinder
        super().__init__()

    def nativeEventFilter(self, eventType, message):
        ret = self.keybinder.handler(eventType, message)
        return ret, 0


def gerar_cpf():
    clip = app.clipboard()
    clip.setText(cpf.gerar_cpf(False))

    return False


def gerar_cpf_formatado():
    print("setting clipboard")
    clip = QApplication.clipboard()
    clip.setText(cpf.gerar_cpf(True))
    print("clipboard set")

    return False


def buscar_ip():
    ip = get("https://api.ipify.org").text

    clip = QApplication.clipboard()
    clip.setText(ip)


def keyboard_setup():
    keybinder.init()

    window = QMainWindow()

    keybinder.register_hotkey(window.winId(), "Ctrl+Alt+C", gerar_cpf)
    keybinder.register_hotkey(window.winId(), "Shift+Alt+I", buscar_ip)

    window.show()

    return keybinder


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication([])

    icon = QSystemTrayIcon(QIcon("img/icon.png"))
    menu = QMenu()

    menu.addAction("Gerar cpf sem formatação", gerar_cpf)
    menu.addAction("Gerar cpf com formatação", gerar_cpf_formatado)
    menu.addSeparator()
    menu.addAction("Buscar id público", buscar_ip)
    menu.addSeparator()
    menu.addAction("Fechar", app.quit)
    icon.setContextMenu(menu)

    binder = keyboard_setup()

    win_event_filter = WinEventFilter(binder)
    event_dispatcher = QAbstractEventDispatcher.instance()
    event_dispatcher.installNativeEventFilter(win_event_filter)

    icon.show()

    app.exec_()
