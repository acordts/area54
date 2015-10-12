# -*- coding: utf-8 -*- 
'''
@summary: object for text data and several methods
'''
import tkFont
import Tkinter

class TextObject(object):
    '''
    @note: an object for text data and several methods
    '''
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
        self._width = 0.0
        self._height = 0.0
        self._width_scale = 1.0
        self._height_scale = 1.0
    
    def text_str(self, text):
        '''
        @param text: input
        @type text: str
        @note: Some arbitrary text. It can be any length of characters.  
        '''
        self._text = unicode(text)
        
    def set_font_size(self, font_size):
        '''
        @var _font_size: font site in points
        @type _font_size: int
        @note: A method with one parameter to set the fontsize in points of the text_str.
        '''
        self._font_size = font_size
        
    def check_text_dimensions(self):
        '''
        @return: text scaled height and width
        @rtype: tuple of float, float
        @note: text_object.check_text_dimensions() - A method which returns the height and width in pixels of the text_str using the current font size
        '''
        font_family = (self._font_name, self._font_size)
        self._font = tkFont.Font(family = font_family, size = self._font_size)
        
        self._height = self._font.measure(self._text) * self._width_scale
        self._width = self._font.metrics('linespace') * self._height_scale 

        return self._height, self._width
    
    def scale(self, width_scale, height_scale):
        '''
        @param width_scale: set width scaling
        @type width_scale: float
        @param height_scale: set height scaling
        @type height_scale: float
        @summary: set text scaling 
        '''
        self._width_scale = width_scale
        self._height_scale = height_scale