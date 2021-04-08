""" create a dialog to select a file """
from PyQt5 import QtWidgets


def openfile_dialog(fldr=None):
    """ create dialog"""
    app = QtWidgets.QApplication([fldr])
    fname = QtWidgets.QFileDialog.getOpenFileName(None, "Select a file...", fldr, filter="All files (*)")
    return fname[0]
