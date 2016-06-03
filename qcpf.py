#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QMainWindow,
                             QApplication,
                             QSystemTrayIcon,
                             QMenu,
                             QShortcut)
from PyQt5.QtGui import QIcon, QClipboard, QKeySequence
import cpf


def gerar_cpf():
    clip = QApplication.clipboard()
    clip.setText(cpf.gerar_cpf(False))

def gerar_cpf_formatado():
    clip = QApplication.clipboard()
    clip.setText(cpf.gerar_cpf(True))

if __name__ == '__main__':
    app = QApplication([])
    icon = QSystemTrayIcon(QIcon("img/icon.png"))
    menu = QMenu()

    menu.addAction("Gerar cpf sem formatação", gerar_cpf)
    menu.addAction("Gerar cpf com formatação", gerar_cpf_formatado)
    menu.addSeparator()
    menu.addAction("Fechar", app.quit)
    icon.setContextMenu(menu)

    icon.show()
    app.exec_()
