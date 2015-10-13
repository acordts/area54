#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
There is a box defined by the following dimensions:
box_x - width of box, in pixels
box_y - height of box, in pixels

text_object - an object for text data and several methods
text_object.text_str - Some arbitrary text. It can be any length of characters.
text_object.setfontsize(fontsize) - A method with one parameter to set the fontsize in points of the text_str.
text_object.check_text_dimensions() - A method which returns the height and width in pixels of the text_str using the current font size

What I would like you to do is to write code that determines which font size to use so that the 
text is as large as it can be but still fit in the box with dimensions box_x,box_y.
'''
from PyQt4 import QtGui, QtCore
from PyQt4.Qt import QString, QStyle
from PyQt4.QtCore import pyqtSlot
import sys

class TextObject(object):
    def __init__(self):
        self._text = ''
        self._fnt_size = 18
        self._fnt_family  = "Times"
    def text_str(self, text):
        '''
        @param text: text for dimension calculation
        @type text: str
        '''
        if not isinstance(text, str):
            print 'invalid text type: {0} - str required'.format(type(text))
            return None
        
        self._text = text
    
    def setfonsize(self, fontsize):
        '''
        @param fontsize: fontsize dimension calculation
        @type fontsize: int
        '''
        if not isinstance(fontsize, int):
            print 'invalid text type: {0} - int required'.format(type(fontsize))
            return None
        
        self._fnt_size = fontsize
    
    def check_text_dimensions(self):
        parent = QtGui.QMainWindow()
        qt_lbl = QtGui.QLabel(parent)
        qt_lbl.setFont(QtGui.QFont(self._fnt_family, self._fnt_size))
        qt_lbl.adjustSize()
        return qt_lbl.size()
    

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
        self._setup_resize_btn()
        self._setup_scale_btn()
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
        
        lbl_txt = QtGui.QLabel(self._main_window)
        lbl_txt.setText('text')
        lbl_txt.resize(lbl_x_range, self._line_height)
        lbl_txt.move(self._margin, self._margin)
        
        self._box_txt = QtGui.QLineEdit('enter text here', self._main_window)
        self._box_txt.resize(600, self._line_height)
        self._box_txt.move(self._margin + lbl_x_range, self._margin)

        lbl_fntsize = QtGui.QLabel(self._main_window)
        lbl_fntsize.setText('fontsize')
        lbl_fntsize.resize(lbl_x_range, self._line_height)
        lbl_fntsize.move(self._margin, self._line_height + self._margin)
        
        lbl_height = QtGui.QLabel(self._main_window)
        lbl_height.setText('lbl height')
        lbl_height.resize(lbl_x_range, self._line_height)
        lbl_height.move(self._margin, 2*self._line_height + self._margin)

        lbl_width = QtGui.QLabel(self._main_window)
        lbl_width.setText('lbl width')
        lbl_width.resize(lbl_x_range, self._line_height)
        lbl_width.move(self._margin, 3*self._line_height + self._margin)

        self._box_fnt_size = QtGui.QLineEdit('18', self._main_window)
        self._box_fnt_size.resize(box_x_range, self._line_height)
        self._box_fnt_size.move(self._margin + lbl_x_range, self._line_height + self._margin)
        
        self._box_height = QtGui.QLineEdit('25', self._main_window)
        self._box_height.resize(box_x_range, self._line_height)
        self._box_height.move(self._margin + lbl_x_range, 2*self._line_height + self._margin)
        
        self._box_width = QtGui.QLineEdit('100', self._main_window)
        self._box_width.resize(box_x_range, self._line_height)
        self._box_width.move(self._margin + lbl_x_range, 3*self._line_height + self._margin)

        self._dst_lbl = QtGui.QLabel(self._main_window)
        self._dst_lbl.move(self._margin, 4*self._line_height + self._margin)
        self._dst_lbl.hide()
        
        self._log_lbl = QtGui.QLabel(self._main_window)
        self._log_lbl.move(self._margin, self._height - 100 - self._margin)
        self._log_lbl.resize(self._width - 2*self._margin, 100)

        
    def _setup_resize_btn(self, name = 'calc ft size'):
        '''
        @summary: setup button for resizing font fitting to label size
        '''
        btn = QtGui.QPushButton(name, self._main_window)
        btn.released.connect(self._adapt_fnt_size)
        btn.move(self._width - btn.width()-self._margin, self._margin)
    
    def _setup_scale_btn(self, name = 'scale'):
        '''
        @summary: setup button to stretch font into label size
        '''
        btn = QtGui.QPushButton(name, self._main_window)
        btn.released.connect(self._scale_font)
        btn.move(self._width - btn.width()-self._margin, 2*self._margin + self._line_height)

    @pyqtSlot()
    def _adapt_fnt_size(self):
        '''
        @summary: get box and text params and calc max fitting font size
        @todo: use box_x, box_y, setfontsize, text_str
        '''
        text = self._box_txt.text()
        text = str(text)
        self.text_str(text)

        width = self._box_width.text()
        width = int(width)
        self.box_x(width)

        height = self._box_height.text()
        height = int(height)
        self.box_y(height)

        self._dst_lbl.setText(text)
        size = 1

        self._dst_lbl.setFont(QtGui.QFont(self._fnt_family, size))
        self._dst_lbl.adjustSize()

        while self._dst_lbl.height() < height and self._dst_lbl.width() < width:
            size += 1
            self._dst_lbl.setFont(QtGui.QFont(self._fnt_family, size))
            self._dst_lbl.adjustSize()
        
        self._dst_lbl.setFont(QtGui.QFont(self._fnt_family, size))
        self._dst_lbl.adjustSize()

        self._dst_lbl.show()
        print self._dst_lbl.size()
        fnt_size = QString(str(size))
        self._box_fnt_size.setText(fnt_size)

    @pyqtSlot()
    def _scale_font(self, text, width, height):
        
        
        #qfnt.setStretch(200)
        pass

    def show(self):
        self._main_window.show()
        
    def box_x(self, width):
        '''
        @param width: required text box width
        @type width: int
        @summary: set height to destination label, update text box content
        '''
        if not isinstance(width, int):
            print 'invalid box_x type: {0}'.format(type(width)) 
            return None
        width_str = QString(str(width))
        self._box_width.setText(width_str)

        dst_lbl_height = self._dst_lbl.height()
        self._dst_lbl.resize(dst_lbl_height, width)

        
    def box_y(self, height):
        '''
        @param height: required text box width
        @type height: int
        @summary: set width to destination label, update text box content
        '''
        if not isinstance(height, int):
            print 'invalid box_y type: {0} str required'.format(type(height)) 
            return None
        
        height_str = QString(str(height))
        self._box_height.setText(height_str)

        dst_lbl_width = self._dst_lbl.width()
        self._dst_lbl.resize(height, dst_lbl_width)

    def text_str(self, text):
        '''
        @param text: text to scale
        @type text: str
        '''
        if not isinstance(text, str):
            print 'invalid text_str type: {0} int required'.format(type(text)) 
            return None
        self._text = text
        
    def setfontsize(self, fnt_size):
        '''
        @param fnt_size: font size 
        @type fnt_size: int
        @summary: set font size
        '''
        if not isinstance(fnt_size, int):
            print 'invalid font size type: {0}, int required'.format(type(fnt_size))
            return None

        self._fnt_size = fnt_size
        self._dst_lbl.setFont(self._fnt_family, self._fnt_size)
        self._dst_lbl.adjustSize()
        
    
    def check_text_dimensions(self):
        '''
        @return: width and height of label
        @rtype: tuple of int
        '''
        self._dst_lbl.setFont(QtGui.QFont(self._fnt_family, self._fnt_size))
        self._dst_lbl.setText(self._text)
        self._dst_lbl.adjustSize()
        w = self._dst_lbl.width()
        h = self._dst_lbl.height()
        return w, h
    

def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec_()

def txt_obj_test():
    app = QtGui.QApplication(sys.argv)
    txt_obj = TextObject()
    txt_obj.setfonsize(18)
    txt_obj.text_str('foooobar')
    print txt_obj.check_text_dimensions()

    txt_obj.text_str('foooobarrrrrrrrrrrrrrrr')
    print txt_obj.check_text_dimensions()

    
    app.exec_()
if __name__ == '__main__':
    txt_obj_test()
    #main()