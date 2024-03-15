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
    keys = boxes[0]
    d_boxes = {i: box for i, box in enumerate(boxes)}
    unlocked_boxed = {0}

    for key in keys:
        if len(unlocked_boxed) < len(boxes) and key not in unlocked_boxed:
            if (d_boxes.get(key) is not None):
                keys += d_boxes[key]
                unlocked_boxed.add(key)
    return len(unlocked_boxed) == len(boxes)
