# -*- coding: utf-8 -*- 
'''
@summary: library of text splitting functions 
'''
import math

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

def split_lines(text, chunk_count, delimiter = ' '):
    '''
    @summary: split text in almost equal chunks
    @param text: text to split
    @type text: str
    @param chunk_count: amount of chunks
    @type chunk_count: int
    @param delimiter: char for splitting given text
    @type delimiter: char
    '''
    pass