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



# Create video capture object, retrying until successful.
while True:
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        break

# Create client to the Redis store.
store = redis.Redis()

i = 0

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
    store.set('image_id', i)
    # print("%d th frame send time, %.20f", i, time.time() )
    print("frame send time, %.20f" % time.time() )
    i = i + 1
    
