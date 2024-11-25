import traitlets
import ipywidgets.widgets as widgets
from IPython.display import display
from jetbot import Camera, bgr8_to_jpeg
from jetbot import ObjectDetector
import cv2

model = ObjectDetector('ssd_mobilenet_v2_coco.engine')
camera = Camera.instance(width=300, height=300)

camera_link = traitlets.dlink((camera, 'value'), (image, 'value'), transform=bgr8_to_jpeg)



detections = model(camera.value)
image = camera.value
image_widget = widgets.Image(format='jpeg', width=300, height=300)
width = int(image_widget.width)
height = int(image_widget.height)
# 이미지에 탐지한 모든 객체에 box 그리기
for det in detections[0]:
    bbox = det['bbox']                
    cv2.rectangle(image, (int(width * bbox[0]), int(height * bbox[1])), (int(width * bbox[2]), int(height * bbox[3])), (255, 0, 0), 2)

# 내가 특정한 객체 중 가장 가까운 객체에 box 그리는 코드
det2 = detections[0][2]
bbox = det2['bbox']
cv2.rectangle(image, (int(width * bbox[0]), int(height * bbox[1])), (int(width * bbox[2]), int(height * bbox[3])), (0, 255, 0), 5)
image_widget.value = bgr8_to_jpeg(image)
display(image_widget)
print(detections)