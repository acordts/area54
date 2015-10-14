'''
@summary:
'''

import math

from text_object import TextObject


class TextBox(object):
    def __init__(self, width, height):
        '''
        @param width: text box width in pixel
        @type width: int
        @param height: text box height in pixel
        @type height: int
        '''
        self._width = width
        self._height = height
        self._txt_obj = TextObject()
        self._font_size = 1
        self._txt_obj.set_font_size(self._font_size)
        self._txt_obj.text_str('')
    
    def set_text(self, text):
        '''
        @param text: input text to fit into box
        @type text: str or unicode
        '''
        self._txt_obj.text_str(text)

    def get_max_font_size(self):
        '''
        @return: best fitting font size in points
        @rtype: int
        @note: font size to use so that the text is as large as it can be but still fit in the box with dimensions box_x,box_y.
        '''
        new_size = best_size = 1
        while self._fitting(new_size):
            best_size = new_size
            new_size += 1
            
        self._txt_obj.set_font_size(self._font_size)
        
        return best_size
    
    def _fitting(self, font_size):
        '''
        @return: given text with given size fit into given boundaries
        @rtype: bool 
        '''
        self._txt_obj.set_font_size(font_size)
        txt_width, txt_height = self._txt_obj.check_text_dimensions()
        return txt_height <= self._height and txt_width <= self._width
    
    def get_scaling(self):
        '''
        @return: width and height scaling to fit given box dimensions
        @rtype: tuple of float
        @note: Write the code that will figure out and implement the scaling necessary for the text to fit in the box best.
        '''
        if not str(self._txt_obj):
            print 'text is missing'
            return 1.0, 1.0
        
        txt_width, txt_height = self._txt_obj.check_text_dimensions()
        width_scale = 1.0 * self._width / txt_width
        height_scale = 1.0 * self._height / txt_height
        return width_scale, height_scale

    def get_scaling_advanced(self):
        '''
        @return: font scaling details
        @rtype: dict
        @note: Write the code that will figure out and implement the scaling necessary for the text to fit in the box best.
        @note: additionally font size will be adjusted
        '''
        self._font_size = self.get_max_font_size()
        self._txt_obj.set_font_size(self._font_size)
        
        txt_width, txt_height = self._txt_obj.check_text_dimensions()
        width_scale = 1.0 * self._width / txt_width
        height_scale = 1.0 * self._height / txt_height
        return {'font_size' : self._font_size,
                'width_scale' : width_scale,
                'height_scale' : height_scale}
        
    def get_min_lines(self):
        '''
        @return: min line count needed to present text
        @rtype: float
        '''
        width_scale, _ = self.get_scaling()
        return math.ceil(1.0 / width_scale)
    
    def get_max_lines(self):
        '''
        @return: max line count possible present text
        @rtype: float
        ''' 
        _, height_scale = self.get_scaling()
        text = str(self._txt_obj)
        return min(math.floor(height_scale), len(text.split()))