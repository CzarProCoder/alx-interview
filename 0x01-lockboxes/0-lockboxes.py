#!/usr/bin/python3

'''
Module to determine whether each lock box can be opened
'''


def canUnlockAll(boxes):
    '''
    Method to check whether each lockbox can be opened

    Args:
        boxes (List): Contains a list of lists with numbers
    
    Return:
        False: If some boxes cannot be opened
        True: If all boxes can be opened
    '''
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
