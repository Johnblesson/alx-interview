#!/usr/bin/python3
"""
n number of locked boxes, numberred sequnetially form 0 to n-1
and may contain keys to other boxes. Method to determine if all boxes can open
"""


def canUnlockAll(boxes):
    """method to determine if all boxes can open"""
    if not boxes:
        return False
    unlocked = []
    i = 0
    length = len(boxes)
    
    for i, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < length and key not in unlocked and key != i:
                unlocked.append(key)
    if len(unlocked) == length:
            return True
    return False
