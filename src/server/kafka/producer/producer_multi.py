import sys
import time
import cv2
import threading
from kafka import KafkaProducer

topic = "distributed-video1"

def publish_video(video_file):
    """
    Publish given video file to a specified Kafka topic. 
    Kafka Server is expected to be running on the localhost. Not partitioned.
    
    :param video_file: path to video file <string>
    """
    # Start up producer
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    # Open file
    print('hello')
    print("time start video engine %.20f" % time.time())
    video = cv2.VideoCapture(video_file)
    print("time end video engine %.20f" % time.time())
    
    print('publishing video..')

    while(video.isOpened()):
        print("%.20f" % time.time())
        success, frame = video.read()

        # Ensure file was read successfully
        if not success:
            print("bad read!")
            break
        
        # Convert image to png
        ret, buffer = cv2.imencode('.jpg', frame)

        # Convert to bytes and send to kafka
        producer.send(topic, buffer.tobytes())
        print("%.20f" % time.time())
        #time.sleep(0.2)
    
    video.release()
    print('publish complete')

def publish_camera():
    """
    Publish camera video stream to specified Kafka topic.
    Kafka Server is expected to be running on the localhost. Not partitioned.
    """

    # Start up producer
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    
    print("time start video engine %.20f" % time.time())
    camera = cv2.VideoCapture(0)
    print("time end video engine %.20f" % time.time())
    try:
        while(True):
            t0 = threading.Thread(target=pub_one_frame, args=(camera, topic, producer))
            t0.start()
            t0.join()
    except:
        print("\nExiting.")
        sys.exit(1)
    
    camera.release()

def pub_one_frame(camera, topic, producer):
    print("frame start %.20f" % time.time())
    success, frame = camera.read()
    ret, buffer = cv2.imencode('.jpg', frame)
    producer.send(topic, buffer.tobytes())
    print("frame end %.20f" % time.time())
    # Choppier stream, reduced load on processor
    # time.sleep(0.2)



if __name__ == '__main__':
    """
    Producer will publish to Kafka Server a video file given as a system arg. 
    Otherwise it will default by streaming webcam feed.
    """
    if(len(sys.argv) > 1):
        video_path = sys.argv[1]
        publish_video(video_path)
    else:
        print("publishing feed!")
        publish_camera()
