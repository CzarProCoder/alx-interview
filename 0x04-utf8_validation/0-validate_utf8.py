#!/usr/bin/python3

'''
Module to determine if a given dataset represents valid utf-8 encoding
'''


def validUTF8(data) -> bool:
    '''
    Method to determine if a given dataset is of valid utf-8 encoding

    Args:
        data (any): Data to be evaluated
    
    Returns:
        True: If data is of valid utf-8
        False: If data is not valid utf-8
    '''
    num_bytes = 0
    for byte in data:
        mask = 1 << 7
        if not num_bytes:
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            if not num_bytes:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        num_bytes -= 1
    return num_bytes == 0
