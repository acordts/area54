#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: acordts
'''
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import QString, QStyle
from PyQt4.QtCore import pyqtSlot
import sys

class MainWindow(object):
    '''
    @summary:
    '''
    def __init__(self, width=800, height=600, line_height = 25, margin=5):
        '''
        @summary: setup main window parameter
        '''
        self._fnt_family = 'times'
        self._width = width
        self._height = height
        self._margin = margin
        self._line_height = line_height
        
        self._main_window = None
        self._setup_main_window()
        self._setup_opt()
        
    def _setup_main_window(self):
        '''
        @summary: qt main window setup
        '''
        self._main_window = QtGui.QMainWindow()
        self._main_window.resize(self._width, self._height)
        self._main_window.setWindowTitle(self.__class__.__name__)
    
    def _setup_opt(self):
        '''
        @summary: setup window content with labels and text boxes
        '''
        lbl_x_range = 80
        box_x_range = 50
        #pre_def_txt = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est'
        pre_def_txt = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam'
        
        lbl_txt = QtGui.QLabel(self._main_window)
        lbl_txt.setText('text')
        lbl_txt.resize(lbl_x_range, self._line_height)
        lbl_txt.move(self._margin, self._margin)
        
        lbl_height = QtGui.QLabel(self._main_window)
        lbl_height.setText('box height')
        lbl_height.resize(lbl_x_range, self._line_height)
        lbl_height.move(self._margin, self._line_height + self._margin)

        lbl_width = QtGui.QLabel(self._main_window)
        lbl_width.setText('box width')
        lbl_width.resize(lbl_x_range, self._line_height)
        lbl_width.move(self._margin, 2*self._line_height + self._margin)

        self._box_txt = QtGui.QLineEdit(pre_def_txt, self._main_window)
        self._box_txt.resize(600, self._line_height)
        self._box_txt.move(self._margin + lbl_x_range, self._margin)

        self._box_height = QtGui.QLineEdit('25', self._main_window)
        self._box_height.resize(box_x_range, self._line_height)
        self._box_height.move(self._margin + lbl_x_range, self._line_height + self._margin)
        
        self._box_width = QtGui.QLineEdit('200', self._main_window)
        self._box_width.resize(box_x_range, self._line_height)
        self._box_width.move(self._margin + lbl_x_range, 2 * self._line_height + self._margin)

        self._log_lbl = QtGui.QLabel(self._main_window)
        self._log_lbl.move(self._margin, self._height - 100 - self._margin)
        self._log_lbl.resize(self._width - 2*self._margin, 100)

        btn = QtGui.QPushButton('scale', self._main_window)
        btn.released.connect(self._scale)
        btn.move(self._width - btn.width()-self._margin, self._margin)

        self._dst_lbl = QtGui.QLabel(self._main_window)
        self._dst_lbl.move(self._margin, 4 * self._line_height + self._margin)
        self._dst_lbl.hide()
        
    def show(self):
        '''
        @summary: show main window
        '''
        self._main_window.show()
        
    @pyqtSlot()
    def _scale(self):
        '''
        @summary: calculate best fitting
        '''
        print '>>> scale'

        text = str(self._box_txt.text())
        box_width = int(self._box_width.text())
        box_height = int(self._box_height.text())
        self._dst_lbl.resize(box_width, box_height)
        
        from text_box_handling import split_lib
        line_cnt = split_lib.opt_line_cnt(box_width, box_height, text)
        lines = split_lib.split_to_line_objects_v2(text, line_cnt, ' ')

        text = '\n'.join([str(l) for l in lines])
        self._dst_lbl.setText(text)
        self._dst_lbl.setFont(QtGui.QFont(self._fnt_family, 10))
        self._dst_lbl.show()

def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec_()

if __name__ == '__main__':
    main()