#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: acordts
'''
from PyQt4 import QtGui, QtCore
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
        #pre_def_txt = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam'
        pre_def_txt = 'Lorem ipsum foobar'
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

        lbl_font_size = QtGui.QLabel(self._main_window)
        lbl_font_size.setText('font size')
        lbl_font_size.resize(lbl_x_range, self._line_height)
        lbl_font_size.move(self._margin, 3*self._line_height + self._margin)

        lbl_lines = QtGui.QLabel(self._main_window)
        lbl_lines.setText('lines')
        lbl_lines.resize(lbl_x_range, self._line_height)
        lbl_lines.move(self._margin, 4*self._line_height + self._margin)

        self._box_txt = QtGui.QLineEdit(pre_def_txt, self._main_window)
        self._box_txt.resize(600, self._line_height)
        self._box_txt.move(self._margin + lbl_x_range, self._margin)

        self._box_height = QtGui.QLineEdit('25', self._main_window)
        self._box_height.resize(box_x_range, self._line_height)
        self._box_height.move(self._margin + lbl_x_range, self._line_height + self._margin)
        
        self._box_width = QtGui.QLineEdit('200', self._main_window)
        self._box_width.resize(box_x_range, self._line_height)
        self._box_width.move(self._margin + lbl_x_range, 2 * self._line_height + self._margin)

        self._box_font_size = QtGui.QLineEdit('1', self._main_window)
        self._box_font_size.resize(box_x_range, self._line_height)
        self._box_font_size.move(self._margin + lbl_x_range, 3 * self._line_height + self._margin)

        self._box_lines = QtGui.QLineEdit('1', self._main_window)
        self._box_lines.resize(box_x_range, self._line_height)
        self._box_lines.move(self._margin + lbl_x_range, 4 * self._line_height + self._margin)

        btn = QtGui.QPushButton('calc font size', self._main_window)
        btn.released.connect(self._scale_font_size)
        btn.move(self._width - btn.width()-self._margin, self._margin)

        btn = QtGui.QPushButton('stretch', self._main_window)
        btn.released.connect(self._stretch)
        btn.move(self._width - btn.width()-self._margin, self._line_height + 2*self._margin)

        btn = QtGui.QPushButton('linebreaks', self._main_window)
        btn.released.connect(self._linebreaks)
        btn.move(self._width - btn.width()-self._margin, 2*self._line_height + 3*self._margin)

        self._dst_lbl = QtGui.QLabel(self._main_window)
        self._dst_lbl.move(self._margin, 6 * self._line_height + self._margin)
        self._dst_lbl.setAutoFillBackground(True)
        self._dst_lbl.setAlignment(QtCore.Qt.AlignTop)
        self._dst_lbl.setStyleSheet("QLabel { background-color: rgba(255, 255, 255, 255); }")        

        self._dst_lbl.hide()
        
    def show(self):
        '''
        @summary: show main window
        '''
        self._main_window.show()
        
    @pyqtSlot()
    def _scale_font_size(self):
        '''
        @summary: calculate best fitting of font size and line breaks
        '''
        print '>>> best font size'
        box_width = int(self._box_width.text())
        box_height = int(self._box_height.text())
        text = str(self._box_txt.text())

        self._dst_lbl.resize(box_width, box_height)

        self._dst_lbl.setText(text)
        
        qfont = QtGui.QFont(self._fnt_family, 1)
        self._dst_lbl.setFont(qfont)

        while box_width >= self._dst_lbl.width() and box_height >= self._dst_lbl.height():
            qfont.setPointSize(qfont.pointSize() + 1)
            self._dst_lbl.setFont(qfont)
            self._dst_lbl.adjustSize()
        else:
            qfont.setPointSize(qfont.pointSize() - 1)
            self._dst_lbl.setFont(qfont)
            self._dst_lbl.adjustSize()
        
        self._dst_lbl.resize(box_width, box_height)
        self._dst_lbl.show()
        
        self._box_font_size.setText(str(qfont.pointSize()))
    
    def _stretch(self):
        '''
        @summary: scale label width
        '''
        print 'stretch'
        box_width = int(self._box_width.text())
        box_height = int(self._box_height.text())
        text = str(self._box_txt.text())

        self._dst_lbl.resize(box_width, box_height)

        self._dst_lbl.setText(text)
        
        qfont = QtGui.QFont(self._fnt_family, 1)
        self._dst_lbl.setFont(qfont)

        while box_height >= self._dst_lbl.height():
            qfont.setPointSize(qfont.pointSize() + 1)
            self._dst_lbl.setFont(qfont)
            self._dst_lbl.adjustSize()
        else:
            qfont.setPointSize(qfont.pointSize() - 1)
            self._dst_lbl.setFont(qfont)
            self._dst_lbl.adjustSize()
        
        txt_width = self._dst_lbl.width()
        width_scale = 100 * box_width / txt_width
        qfont.setStretch(width_scale)
        self._dst_lbl.setFont(qfont)
        
        self._dst_lbl.resize(box_width, box_height)
        self._dst_lbl.show()
        self._box_font_size.setText(str(qfont.pointSize()))
    
    def _linebreaks(self):
        print 'linebreaks'
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec_()

if __name__ == '__main__':
    main()