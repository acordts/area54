'''
@summary:
'''

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
        
    def set_dimensions(self, box_width, box_height):
        '''
        @param box_width: new box width / x dimension
        @type box_width: int
        @param box_height: new box height / y dimension
        @type box_height: int
        @summary: (re)set box dimensions
        '''
        self._width = box_width
        self._height = box_height
        
    def set_font_size(self, font_size):
        '''
        @summary: set font size to box element
        @param font_size: font size in points of box element
        @type font_size: int
        '''
        self._font_size = font_size
        self._txt_obj.set_font_size(self._font_size)