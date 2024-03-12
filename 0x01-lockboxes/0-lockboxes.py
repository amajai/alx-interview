#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Lockboxes
    """
    if not isinstance(boxes, list) or not boxes or not boxes[0]:
        return False
    keys = boxes[0][:]
    d_boxes = {}
    unlocked_boxed = {0}

    for i in range(len(boxes)):
        d_boxes[i] = boxes[i]

    for key in keys:
        if key not in unlocked_boxed:
            keys += d_boxes[key]
            d_boxes[key] = []
            unlocked_boxed.add(key)
    return len(unlocked_boxed) == len(boxes)
