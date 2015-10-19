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
    font_name = 'times'
    def __init__(self, text = ''):
        '''
        @var _text: input
        @type _text: str
        @var _font_size: font site in points
        @type _font_size: int
        @var _scale_width: text scaling in x dimension
        @type _scale_width: float
        @var _scale_height: text scaling in y dimension
        @type _scale_height: float
        '''
        _ = Tkinter.Tk()

        self._text = text
        self._font_size = 1
        self._scale_width = 1.0
        self._scale_height = 1.0
        self._width, self._height = self.check_text_dimensions()

    def text_str(self, text):
        '''
        @param text: input
        @type text: str
        @note: Some arbitrary text. It can be any length of characters.  
        '''
        self._text = text
        self._width, self._height = self.check_text_dimensions()
    
    def __str__(self):
        '''
        @return: setted text
        @rtype: str
        '''
        return self._text
    
    def __len__(self):
        '''
        @return: text width
        @rtype: int
        '''
        return self._width
    
    def get_line_height(self):
        '''
        @return: text line height
        @rtype: int
        '''
        return int(self._height)
    
    def set_font_size(self, font_size):
        '''
        @var _font_size: font site in points
        @type _font_size: int
        @note: A method with one parameter to set the fontsize in points of the text_str.
        '''
        self._font_size = font_size

    def get_font_size(self):
        '''
        @return: current font size in points
        @rtype: int
        '''
        return self._font_size

    def check_text_dimensions(self):
        '''
        @return: scaled text height and width dimensions
        @rtype: tuple of float, float
        @note: text_object.check_text_dimensions() - A method which returns the height and width in pixels of the text_str using the current font size
        '''
        font_family = (TextObject.font_name, self._font_size)
        self._font = tkFont.Font(family = font_family, size = self._font_size)
        
        txt_height = self._font.metrics('linespace') 
        txt_width = self._font.measure(self._text)

        return txt_width * self._scale_width, txt_height * self._scale_height
    
    def scale(self, width_scale, height_scale):
        '''
        @param width_scale: set text width scaling
        @type width_scale: float
        @param height_scale: set text height scaling
        @type height_scale: float
        @summary: set absolute text scaling
        @attention: the scale values are absolute and ignore scalings entered before
        @note: text_object.scale(a,b) - A method which takes two arguments, one for scaling the width value, one for scaling the
        '''
        self._scale_width = width_scale * 1.0
        self._scale_height = height_scale * 1.0
    
    def scale_rel(self, width_scale, height_scale):
        '''
        @param width_scale: set text width scaling
        @type width_scale: float
        @param height_scale: set text height scaling
        @type height_scale: float
        @summary: set relative text scaling
        '''
        self._scale_width *= width_scale
        self._scale_height *= height_scale
        
    def set_font_name(self, font_name):
        '''
        @summary: 
        @param font_name: set new font name
        @type font_name: str 
        '''
        self.font_name = font_name
    # alias
    scale_abs = scale
