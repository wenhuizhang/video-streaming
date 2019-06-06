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

topic = 'test'

def publish_video(video_file):
    """
    Publish given video file to a specified Redis Channel
    :param video_file: path to video file <string>
    """
    r = redis.StrictRedis(host='localhost', port=6379) 
    p = r.pubsub()

    # Open file
    video = cv2.VideoCapture(video_file)
    store = redis.Redis()
    
    print('publishing video...')

    while(video.isOpened()):
        success, frame = video.read()

        # Ensure file was read successfully
        if not success:
            print("bad read!")
            break
        
        # Convert image to png
        ret, buffer = cv2.imencode('.jpg', frame)
        r.publish(topic,  buffer.tobytes())

        # time.sleep(0.2)
    video.release()
    print('publish complete')

def publish_camera():
    """
    Publish camera video stream to specified Redis Channel.
    Redis Server is expected to be running on the localhost. Not partitioned.
    """
    r = redis.StrictRedis(host='localhost', port=6379) 
    p = r.pubsub()

    
    camera = cv2.VideoCapture(0)
    try:
        while(True):
            success, frame = camera.read()
        
            ret, buffer = cv2.imencode('.jpg', frame)
            r.publish(topic, buffer.tobytes())
            print("frame send time, %.20f" % time.time())
            # Choppier stream, reduced load on processor
            # time.sleep(0.2)

    except:
        print("\nExiting.")
        sys.exit(1)

    
    camera.release()


if __name__ == '__main__':
    """
    Producer will publish to Redis Server a video file given as a system arg. 
    Otherwise it will default by streaming webcam feed.
    """
    if(len(sys.argv) > 1):
        video_path = sys.argv[1]
        publish_video(video_path)
    else:
        print("publishing feed!")
        publish_camera()

