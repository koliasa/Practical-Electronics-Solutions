## An intelligent system for recognizing people and thermal objects at long distances
## Object Detection and Notification System using YOLOv5 and Telegram
This system is designed to detect people and thermal objects in real-time using IP cameras, and notify the operator about their presence via Telegram. The system uses YOLOv5 deep learning model for object detection, OpenCV for image processing, and python-telegram-bot library for sending notifications with images.
## Requirements
- Ubuntu 18.04 or higher
- ZoneMinder installed and configured
- IP cameras with RTSP protocol support
- Python 3.x
- OpenCV (pip install opencv-python)
- pyTelegramBotAPI (pip install python-telegram-bot)
- YOLOv5 or EfficientDet deep learning models
## Installation
1. Clone the YOLOv5 repository to your system and install the dependencies:
```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```
2. Download the pre-trained weights for YOLOv5 from the official repository:
```bash
wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt
```
3. Clone the pyTelegramBotAPI repository to your system:
```bash
wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt
```
4. Install OpenCV and python-telegram-bot using pip:
```bash
pip install opencv-python
pip install python-telegram-bot
```
## Configuration
1. Create a new Telegram bot by following the instructions provided on their website.
2. Obtain the API token for your bot, which you will use to send messages to it.
3. Create a new Telegram group or channel where you want to receive the notifications.
4. Add the bot to the group or channel as an administrator.
5. Note down the chat ID for the group or channel, which you will use to send notifications to it.

The following code snippet shows an example implementation of the object detection script:
```python
import cv2
import numpy as np
import time
import requests
import json


# Define the video stream URL
video_url = 'rtsp://your_stream_url'

# Define the thermal detection model path and configuration file path
thermal_model_path = '/path/to/thermal/detection/model'
thermal_config_path = '/path/to/thermal/detection/config'

# Define the object detection model path and configuration file path
object_model_path = '/path/to/object/detection/model'
object_config_path = '/path/to/object/detection/config'

# Define the confidence threshold for object and thermal detection
object_conf_threshold = 0.5
thermal_conf_threshold = 0.5

# Define the classes for object detection
object_classes = []
with open('/path/to/object/detection/classes', 'r') as f:
    object_classes = [line.strip() for line in f.readlines()]

# Load the thermal detection model
thermal_net = cv2.dnn.readNetFromDarknet(thermal_config_path, thermal_model_path)

# Load the object detection model
object_net = cv2.dnn.readNetFromDarknet(object_config_path, object_model_path)
object_net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
object_net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Define the video stream capture object
cap = cv2.VideoCapture(video_url)

# Define the Telegram bot token and chat ID for sending notifications
bot_token = 'your_bot_token'
chat_id = 'your_chat_id'

# Define the function for sending a notification message with image to Telegram
def send_telegram_image(image):
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    _, buffer = cv2.imencode('.jpg', image)
    files = {'photo': ('image.jpg', buffer.tobytes(), 'image/jpeg')}
    data = {'chat_id': chat_id}
    r = requests.post(url, data=data, files=files)
    if r.status_code != 200:
        print('Failed to send Telegram message:', r.text)

# Start the video stream processing
while True:
    # Read the frame from the video stream
    ret, frame = cap.read()
    
    # If the frame was not successfully read, skip to the next iteration
    if not ret:
        continue
        
    # Detect objects using object detection model
    object_blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True)
    object_net.setInput(object_blob)
    object_outputs = object_net.forward(object_net.getUnconnectedOutLayersNames())
    object_boxes, object_confidences, object_class_ids = [], [], []
    for output in object_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > object_conf_threshold:
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                object_boxes.append([left, top, width, height])
                object_confidences.append(float(confidence))
                object_class_ids.append(class_id)
    
    # Detect objects using thermal detection model
    thermal_blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True)
    thermal_net.setInput(thermal_blob)
# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Start the video stream processing
video_url = 'rtsp://' + IP_ADDRESS + ':' + PORT_NUMBER + '/zm/' + MONITOR_ID + '/monitor.mjpeg'
stream = cv2.VideoCapture(video_url)
while True:
    # Read frame from video stream
    ret, frame = stream.read()
    if not ret:
        break
        
    # Detect objects using thermal detection model
    thermal_blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True)
    thermal_net.setInput(thermal_blob)
    thermal_outputs = thermal_net.forward(thermal_net.getUnconnectedOutLayersNames())
    thermal_boxes, thermal_confidences, thermal_class_ids = [], [], []
    for output in thermal_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > THERMAL_CONFIDENCE_THRESHOLD:
                center_x, center_y, w, h = (detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])).astype('int')
                x, y = int(center_x - w / 2), int(center_y - h / 2)
                thermal_boxes.append([x, y, int(w), int(h)])
                thermal_confidences.append(float(confidence))
                thermal_class_ids.append(class_id)

    # Detect objects using person detection model
    person_blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True)
    person_net.setInput(person_blob)
    person_outputs = person_net.forward(person_net.getUnconnectedOutLayersNames())
    person_boxes, person_confidences, person_class_ids = [], [], []
    for output in person_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if class_id == PERSON_CLASS_ID and confidence > PERSON_CONFIDENCE_THRESHOLD:
                center_x, center_y, w, h = (detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])).astype('int')
                x, y = int(center_x - w / 2), int(center_y - h / 2)
                person_boxes.append([x, y, int(w), int(h)])
                person_confidences.append(float(confidence))
                person_class_ids.append(class_id)

    # Draw bounding boxes on frame
    indices = cv2.dnn.NMSBoxes(thermal_boxes, thermal_confidences, THERMAL_CONFIDENCE_THRESHOLD, THERMAL_NMS_THRESHOLD)
    for i in indices:
        i = i[0]
        box = thermal_boxes[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        label = f'Thermal: {thermal_classes[thermal_class_ids[i]]} {thermal_confidences[i]:.2f}'
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    indices = cv2.dnn.NMSBoxes(person_boxes, person_confidences, PERSON_CONFID
# Initialize the video stream
vs = cv2.VideoCapture(video_url)

# Loop over the frames from the video stream
while True:
    # Read the next frame from the video stream
    ret, frame = vs.read()
    
    # Break the loop if the video stream has ended
    if not ret:
        break
    
    # Resize the frame
    frame = imutils.resize(frame, width=800)
    
    # Detect objects using thermal detection model
    thermal_blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True)
    thermal_net.setInput(thermal_blob)
    thermal_outputs = thermal_net.forward(thermal_net.getUnconnectedOutLayersNames())
    thermal_boxes, thermal_confidences, thermal_class_ids = [], [], []
    for output in thermal_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > thermal_confidence_thresh:
                box = detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                thermal_boxes.append([x, y, int(width), int(height)])
                thermal_confidences.append(float(confidence))
                thermal_class_ids.append(class_id)
    
    # Apply non-maxima suppression to suppress weak, overlapping bounding boxes
    idxs = cv2.dnn.NMSBoxes(thermal_boxes, thermal_confidences, thermal_confidence_thresh, thermal_nms_thresh)
    
    # Loop over the remaining indexes
    for i in idxs.flatten():
        # If the detected object is a person, send a notification to the Telegram bot
        if thermal_class_ids[i] == 0:
            # Draw the bounding box on the frame
            x, y, w, h = thermal_boxes[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Send a notification to the Telegram bot
            send_telegram_notification(bot_token, chat_id, "Person detected!", frame)
        
        # If the detected object is a thermal object, draw a bounding box on the frame
        elif thermal_class_ids[i] == 1:
            x, y, w, h = thermal_boxes[i]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Display the frame
    cv2.imshow("Frame", frame)
    
    # Wait for a key press and break the loop if the 'q' key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the video stream and close all windows
vs.release()
cv2.destroyAllWindows()
```
That the code assumes that you have already defined the following variables:

`video_url`: the URL of the RTSP stream
`thermal_net`: the thermal detection model
`thermal_confidence_thresh`: the confidence threshold for detecting objects using the thermal detection model
`thermal_nms_thresh`: the threshold for non-maxima suppression when detecting objects using the thermal detection model
`bot_token`: the access token for the Telegram bot
`chat_id`: the chat ID for the Telegram bot

To enable sending notifications to Telegram, we'll use the `python-telegram-bot` library. You can install it via pip by running `pip install python-telegram-bot`.

Here's an example code for sending a message with an image to a Telegram chat:
```python
import cv2
import numpy as np
import telegram
import urllib

# Set up the bot and chat IDs
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'

# Load the YOLOv5 model for object detection
net = cv2.dnn.readNet('yolov5s.pt')

# Load the thermal detection model
thermal_net = cv2.dnn.readNet('thermal_detection_model.weights', 'thermal_detection_model.cfg')

# Start the video stream processing
video_url = 'rtsp://example.com/video_stream'  # Replace with your video stream URL
cap = cv2.VideoCapture(video_url)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        break

    # Detect objects using YOLOv5
    blob = cv2.dnn.blobFromImage(frame, 1/255, (640, 640), swapRB=True)
    net.setInput(blob)
    outputs = net.forward(net.getUnconnectedOutLayersNames())
    boxes, confidences, class_ids = [], [], []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 0:  # Class ID 0 is for people
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                boxes.append([left, top, width, height])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # If a person is detected, send a notification to Telegram
    if len(boxes) > 0:
        photo_url = 'https://koliasa.com/image.jpg'  # Replace with your image URL
        photo_file = urllib.request.urlopen(photo_url)
        bot = telegram.Bot(token=bot_token)
        bot.send_photo(chat_id=chat_id, photo=photo_file, caption='Person detected!')

cap.release()
cv2.destroyAllWindows()

```
You'll need to replace `YOUR_BOT_TOKEN` and `YOUR_CHAT_ID` with your actual bot token and chat ID, respectively. To obtain a bot token, follow the instructions on the BotFather page.