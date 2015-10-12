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
        @var _font_name: font type name
        @type _font_name: str
        @var _scale_width: text scaling in x dimension
        @type _scale_width: float
        @var _scale_height: text scaling in y dimension
        @type _scale_height: float
        '''
        _ = Tkinter.Tk()

        self._text = ''
        self._font_size = 8
        self._font_name = 'times'
        self._scale_width = 1.0
        self._scale_height = 1.0
    
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
        font_family = (self._font_name, self._font_size)
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
        @summary: set text scaling
        @attention: the scale values are absolute and ignore scalings entered before
        @note: text_object.scale(a,b) - A method which takes two arguments, one for scaling the width value, one for scaling the
               height value of text_object.text_str
        '''
        self._scale_width = width_scale * 1.0
        self._scale_height = height_scale * 1.0
        
        #### for relative scaling use following two lines
        #self._scale_width *= width_scale
        #self._scale_height *= height_scale 
