# -*- coding: utf-8 -*- 
'''
'''
from text_box_handling import split_lib
from text_box_handling.text_box import TextBox

class TextScale(object):
    '''
    @summary: object to calculate text formatting for best matching in defined boundaries
    '''
    def __init__(self):
        '''
        @var _box_width: width of text surrounding box
        @type _box_width: int
        @var _box_height: height of text surrounding box
        @type _box_height: int
        @var _font: font name
        @type _font: str
        @var _text: text to format (scale / wrap)
        @type _text: str
        '''
        self._box_width = 0
        self._box_height = 0
        self._font = 'times'
        self._text = ''
    
    def set_size(self, width, height):
        '''
        @param font_name:
        @type font_name: str
        '''
        self._box_width = width
        self._box_height = height
    
    def set_font_type(self, font_family):
        '''
        @param font_family: font_family name
        @type font_family: str
        @TODO: overwrite font family in TextObject
        '''
        self._font = font_family

    def set_text(self, text):
        '''
        @param text:
        @type text: str
        '''
        self._text = text
        
    def get_wrap_scale(self):
        '''
        @return: wrap, scale values 
        @rtype: dict
        '''
        line_cnt = split_lib.opt_line_cnt(self._box_width, self._box_height, self._text)
        line_txt_objs = split_lib.split_to_line_objects_v2(self._text, line_cnt, ' ')
        
        details = {}
        lines = [str(line_obj) for line_obj in line_txt_objs] 
        details['text'] = '\n'.join(lines)

        line_txt_objs.sort(key=lambda x: len(x), reverse=True)
        longest_line = line_txt_objs[0]

        dst_line_height = 1.0 * self._box_height / len(line_txt_objs)
        text_box = TextBox(self._box_width, dst_line_height)
        text_box.set_text(str(longest_line))

        details.update(text_box.get_scaling_advanced())
        return details
