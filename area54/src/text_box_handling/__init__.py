# -*- coding: utf-8 -*- 
'''
TODO: accept unicode
'''
import math

from text_box_handling.split_lib import split_text, split_to_line_objects
from text_box_handling.text_box import TextBox
from text_object import TextObject


def task_1():
    '''
    @note: text_object - an object for text data and several methods
           text_object.text_str - Some arbitrary text. It can be any length of characters.
           text_object.setfontsize(fontsize) - A method with one parameter to set the fontsize in points of the text_str.   
           text_object.check_text_dimensions() - A method which returns the height and width in pixels of the text_str using the current font size 
    '''
    print '>>> task 1 - text_object basics\n'
    text_object = TextObject()
    text_object.text_str('foobar') 
    
    text_object.set_font_size(11)
    print 'text size with 11pt:\t{0}'.format(text_object.check_text_dimensions())
    
    text_object.set_font_size(18)
    print 'text size with 18pt:\t{0}'.format(text_object.check_text_dimensions())
    
    text_object.scale(0.5, 0.5)    
    print 'shrinked text:\t{0}'.format(text_object.check_text_dimensions())

    text_object.scale(2, 1.5)    
    print 'bloated text:\t{0}'.format(text_object.check_text_dimensions())
    print 25*'-'

def task_2():
    '''
    @note: text_object.setfontsize(12) - Fontsize has been set to 12
          text_object.scale(a,b) - A method which takes two arguments, one for scaling the width value, one for scaling the
          height value of text_object.text_str.
    '''
    print '>>> task 2 - scale text_object\n'
    text_object = TextObject()
    text_object.text_str('foobar')
    text_object.set_font_size(12)
    print 'original size:\t{0}'.format(text_object.check_text_dimensions())

    text_object.scale(2,1)
    print 'scaled size:\t{0}'.format(text_object.check_text_dimensions())

    text_object.scale(2,4) #scaling handle absolute values, currently values entered before will be overwritten
    print 'rescaled size:\t{0}'.format(text_object.check_text_dimensions())
    print 25*'-'

def task_3():
    '''
    @summary: scale text box with default text size (1pt)
    @note: Write the code that will figure out and implement the scaling necessary for the text to fit in the box best.
    '''
    print '>>> task 3 - fitting text to box\n'

    # define no font size in box element, fallback use font size 1
    text_box = TextBox(100, 50)
    text_box.set_text('foobar')
    width_scaling, height_scaling = text_box.get_scaling()
    
    print 'scale width:\t{0}'.format(width_scaling)
    print 'scale height:\t{0}'.format(height_scaling)
    print 25*'-'

def task_4():
    '''
    @summary: resize font and scale in a 2nd step 
    '''
    text_box = TextBox(100, 50)
    text_box.set_text('foobar')
    
    scaling_params = text_box.get_scaling_advanced()
    
    print '>> task 4 - fitting text to box with font scaling\n'
    print 'best font size:\t{font_size}\n' \
            'width_scaling:\t{width_scale}\n' \
            'height_scale:\t{height_scale}'.format(**scaling_params)
    print 25*'-'

def task_5():
    '''
    @summary: split text in lines of nearly even length
    '''
    text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est'
    line_cnt = 10
    lines = split_to_line_objects(text, line_cnt)

    print '>> task 5 - split text in equal lines\n'
    for line in lines: 
        print len(line), str(line)
    print 25*'-'


def task_6():
    '''
    @summary: calculate line count using scaling
    '''


def main():
    #task_1()
    #task_2()
    #task_3()
    task_4()
    task_5()

if __name__ == '__main__':
    main()