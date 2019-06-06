"""
Usage:
   python recorder.py [width] [height]
"""

import os
import StringIO
import sys
import time

import coils
import cv2
import numpy as np
import redis


# Retrieve command line arguments.
width = None if len(sys.argv) <= 1 else int(sys.argv[1])
height = None if len(sys.argv) <= 2 else int(sys.argv[2])

# Create video capture object, retrying until successful.
while True:
    cap = cv2.VideoCapture(-1)
    if cap.isOpened():
        break
    if cur_sleep < max_sleep:
        cur_sleep *= 2
        cur_sleep = min(cur_sleep, max_sleep)
        continue
    cur_sleep = 0

# Create client to the Redis store.
store = redis.Redis()

# Set video dimensions, if given.
if width: cap.set(3, width)
if height: cap.set(4, height)

# Monitor the framerate at 1s, 5s, 10s intervals.
fps = coils.RateTicker((1, 5, 10))

# Repeatedly capture current image, 
# encode, serialize and push to Redis database.
# Then create unique ID, and push to database as well.
while True:
    hello, image = cap.read()
    hello, image = cv2.imencode('.jpg', image)
    sio = StringIO.StringIO()
    np.save(sio, image)
    value = sio.getvalue()
    store.set('image', value)
    image_id = os.urandom(4)
    store.set('image_id', image_id)
    
    # Print the framerate.
    text = '{:.2f}, {:.2f}, {:.2f} fps'.format(*fps.tick())
    print(text)
