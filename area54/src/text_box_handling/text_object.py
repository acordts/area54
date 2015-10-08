'''
@summary:
'''

import tkFont
import Tkinter

class TextObject(object):
    def __init__(self):
        '''
        @var _text: input
        @type _text: str
        @var _font_size: font site in points
        @type _font_size: int
        '''
        _ = Tkinter.Tk()

        self._text = ''
        self._font_size = 8
        self._font_name = 'times'
        self._width = 300
        self._height = 200

    def text_str(self, text):
        '''
        @param text: input
        @type text: str
        @todo: use e.g. unicode  
        '''
        self._text = text
        
    def set_font_size(self, font_size):
        '''
        @var _font_size: font site in points
        @type _font_size: int
        '''
        self._font_size = font_size
        
    def check_text_dimensions(self):
        '''
        @return: text height and width
        @rtype: tuple of float, float
        '''
        font_family = (self._font_name, self._font_size)
        self._font = tkFont.Font(family = font_family, size = self._font_size)
        return self._font.measure(self._text), self._font.metrics('linespace')