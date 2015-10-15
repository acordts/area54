# -*- coding: utf-8 -*- 
'''

'''
import math

from text_box_handling import split_lib
from text_box_handling.text_box import TextBox
from text_object import TextObject

def task_1():
    '''
    @note: text_object - an object for text data and several methods
           text_object.text_str - Some arbitrary text. It can be any length of characters.
           text_object.setfontsize(fontsize) - A method with one parameter to set the fontsize in points of the text_str.   
           text_object.check_text_dimensions() - A method which returns the height and width in pixels of the text_str using the current font size 
    '''
    print '>>> task 1 -text_object basics\n'
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
    print 50*'-'

def task_2():
    '''
    @note: text_object.setfontsize(12) - Fontsize has been set to 12
          text_object.scale(a,b) - A method which takes two arguments, one for scaling the width value, one for scaling the
          height value of text_object.text_str.
    '''
    print '>>> task 2 -\tscale text_object\n'
    text_object = TextObject()
    text_object.text_str('foobar')
    text_object.set_font_size(12)
    print 'original size:\t{0}'.format(text_object.check_text_dimensions())

    text_object.scale(2,1)
    print 'scaled size:\t{0}'.format(text_object.check_text_dimensions())

    text_object.scale(2,4) #scaling handle absolute values, currently values entered before will be overwritten
    print 'rescaled size:\t{0}'.format(text_object.check_text_dimensions())
    print 50*'-'

def task_3():
    '''
    @summary: scale text box with default text size (1pt)
    @note: Write the code that will figure out and implement the scaling necessary for the text to fit in the box best.
    '''
    print '>>> task 3 -\tfitting text to box\n'

    # define no font size in box element, fallback use font size 1
    text_box = TextBox(100, 50)
    text_box.set_text('foobar')
    width_scaling, height_scaling = text_box.get_scaling()
    
    print 'scale width:\t{0}'.format(width_scaling)
    print 'scale height:\t{0}'.format(height_scaling)
    print 50*'-'

def task_4():
    '''
    @summary: resize font and scale in a 2nd step 
    '''
    print '>> task 4 - fitting text to box with font scaling\n'

    text_box = TextBox(100, 50)
    text_box.set_text('foobar')
    
    scaling_params = text_box.get_scaling_advanced()
    
    print 'best font size:\t{font_size}\n' \
            'width_scaling:\t{width_scale}\n' \
            'height_scale:\t{height_scale}'.format(**scaling_params)
    print 50*'-'

def task_5_1():
    '''
    @summary: split text in lines of nearly even length
    '''
    print '>> task 5_1 - split text in equal lines v1\n'

    text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est'
    line_cnt = 10
    lines = split_lib.split_to_line_objects(text, line_cnt)
     
    for line in lines: 
        print len(line), str(line)
    print 50*'-'

def task_5_2():
    '''
    @summary: split text in lines of nearly even length
    '''
    print '>> task 5_2 - \tsplit text in equal lines v2'
    print '\t\tfill lines from beginning. last line could be nearly empty\n'

    text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est'
    line_cnt = 10
    lines = split_lib.split_to_line_objects_v2(text, line_cnt)
     
    for line in lines: 
        print len(line), str(line)
    print 50*'-'

def task_6():
    '''
    @summary: calculate line cnt for best scaling 
    '''
    print '>> task 6 - calculate best line count fitting to box ratio\n'

    box_width = 800
    box_height = 400
    text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est'

    line_cnt = split_lib.opt_line_cnt(box_width, box_height, text)
    lines = split_lib.split_to_line_objects_v2(text, line_cnt, ' ')
    for l in lines: print len(l), str(l);
    print 50*'-'

def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5_1()
    task_5_2()
    task_6()

if __name__ == '__main__':
    main()