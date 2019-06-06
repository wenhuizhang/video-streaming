import datetime
import time
import base64

import coils
import numpy as np
import redis
from flask import Flask, Response, render_template
import traceback

topic = 'test'

# Fire up the Redis Consumer
r = redis.StrictRedis(host='localhost', port=6379)
p = r.pubsub()                                                          
p.subscribe(topic) 

# consumer = KafkaConsumer(
#     topic, 
# bootstrap_servers=['localhost:9092'])

message = p.get_message()

# Set the consumer in a Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed', methods=['GET'])
def video_feed():
    """
    This is the heart of our video display. Notice we set the mimetype to 
    multipart/x-mixed-replace. This tells Flask to replace any old images with 
    new values streaming through the pipeline.
    """
    return Response(
        get_video_stream(), 
        mimetype='multipart/x-mixed-replace; boundary=frame')

def get_video_stream():
    """
    Here is where we recieve streamed images from the Redis Server and convert 
    them to a Flask-readable format.
    """
    while True:
        print message['data']
        yield (b'--frame\r\n'
               b'Content-Type: image/jpg\r\n\r\n' + message['data'] + b'\r\n\r\n')
        # print("get")
        print("frame get time, %.20f" % time.time())
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
