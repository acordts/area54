# -*- coding: utf-8 -*- 
'''
@summary: library of text splitting functions 
'''
import math

from text_box_handling.text_object import TextObject

def split_text(text, chunk_count, delimiter=' '):
    '''
    @summary: split text on delimiter in defined count of almost equal length
    @param text: text to split in equal chunks 
    @type text: str
    @param chunk_count: amount of chunks
    @type chunk_count: int
    @param delimiter: char for splitting given text
    @type delimiter: char
    @return: text chunks
    @rtype: list of str
    '''
    chunks = []

    opt_chunk_size = int(math.ceil(1.0 * len(text) / chunk_count))
    next_delimiter = text[opt_chunk_size:].find(delimiter)
    pointer = next_delimiter + opt_chunk_size

    chunks.append(text[:pointer])
    rest = text[pointer:].strip()
    
    if chunk_count > 2:
        chunks.extend(split_text(rest, chunk_count - 1))
    else:
        chunks.append(rest)

    return chunks
    
def split_to_line_objects(text, line_cnt, delimiter=' '):
    '''
    @summary: split text objects in almost equal chunks
    @param text: text to split
    @type text: str
    @param line_cnt: amount of required lines
    @type line_cnt: int
    @param delimiter: delimiter element
    @type delimiter: char
    @param opt_len: optimal line length in pixel
    @type opt_len: float
    @return: splitted text lines
    @rtype: list of TextObject
    @note: text is more homogene than in the 2nd implementation
    '''
    opt_len = len(TextObject(text)) / line_cnt

    delimiter_width = len(TextObject(delimiter))
    words = text.split(delimiter)
    
    line = TextObject()

    for word_nr in xrange(len(words)):
        new_text = str(line) + words[word_nr]
        line.text_str(new_text)

        if len(line) + delimiter_width >= opt_len:
            break
        line.text_str(str(line) + delimiter)

    text = delimiter.join(words[word_nr + 1:])
    if line_cnt == 2:
        return [line, TextObject(text)]

    lines = [line]
    lines.extend(split_to_line_objects(text, line_cnt - 1, delimiter))
    return lines    
    
def split_to_line_objects_v2(text, line_cnt, delimiter=' ', opt_len = 0):
    '''
    @summary: split text objects in almost equal chunks
    @param text: text to split
    @type text: str
    @param line_cnt: amount of required lines
    @type line_cnt: int
    @param delimiter: delimiter element
    @type delimiter: char
    @param opt_len: optimal line length in pixel
    @type opt_len: float
    @return: splitted text lines
    @rtype: list of TextObject 
    @note: unused spacer will be removed, line length will be equal for all lines
           lines contain as many words as possible, thats why the last line could be
           nearly empty
    '''
    if not opt_len:
        deleted_spacer = len(TextObject(10 * delimiter))
        opt_len = (len(TextObject(text))-deleted_spacer) / line_cnt

    delimiter_width = len(TextObject(delimiter))
    words = text.split(delimiter)
    
    line = TextObject()

    for word_nr in xrange(len(words)):
        new_text = str(line) + words[word_nr]
        line.text_str(new_text)

        if len(line) + delimiter_width >= opt_len:
            break
        line.text_str(str(line) + delimiter)

    text = delimiter.join(words[word_nr + 1:])
    if line_cnt == 2:
        return [line, TextObject(text)]

    lines = [line]
    lines.extend(split_to_line_objects_v2(text, line_cnt - 1, delimiter, opt_len))
    return lines