# -*- coding: utf-8 -*- 
'''
@summary: text box with text_object
@note: There is a box defined by the following dimensions:
       box_x - width of box, in pixels
       box_y - height of box, in pixels
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
        self.box_x = width
        self.box_y = height
        self._txt_obj = TextObject()
        self._txt_obj.set_font_size(1)
        self._txt_obj.text_str('')
    
    def set_text(self, text):
        '''
        @param text: input text to fit into box
        @type text: str or unicode
        '''
        self._txt_obj.text_str(text)

    def get_max_fnt_size(self):
        '''
        @return: best fitting font size in points
        @rtype: int
        '''
        new_size = best_size = 1
        while self._fits(new_size):
            best_size = new_size
            new_size += 1
        
        self._txt_obj.set_font_size(best_size)
        return best_size
    
    def _fits(self, font_size):
        '''
        @return: given text with given size fit into given boundaries
        @rtype: bool 
        '''
        self._txt_obj.set_font_size(font_size)
        txt_height, txt_width = self._txt_obj.check_text_dimensions()
        return txt_height <= self.box_y and txt_width <= self.box_x
    
    def get_scaling(self):
        '''
        @summary: calculate max font-size and perfect scaling in given box width and height
                  while text is in one line
        @return: font adjustment details
        @rtype: dict
        @note: figure out the scaling necessary for the text to fit in the box best.
        '''
        txt_height, txt_width = self._txt_obj.check_text_dimensions()
        width_scale = 1.0 * self.box_x / txt_width
        height_scale = 1.0 * self.box_y / txt_height
        return {'font_size' : self.get_max_fnt_size(),
                'width_scale' : width_scale,
                'height_scale' : height_scale}