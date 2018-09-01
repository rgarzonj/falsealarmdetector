# Improving movement detections in WIFI Outdoor cameras
This code is used with an outdoor ieGeek WIFI camera to filter false movement detection emails. The camera sends an email every time a movement is detected but most of the times there is no real interest in the picture. This code filters the emails and re-sends back only the emails that contain a picture where a person is detected by YOLOv1 neural network.

The code does the following:
- Downloads emails from a mailbox using POP3.
- Checks the pictures in the emails using YOLOv1 network.
- If the picture contains a person, sends back the email with the picture.

If you want to test it:
- Send an email with a picture that includes a person to the following email address: 'incoming_at_lifteye.es'
- If YOLOv1 detects a person in the picture, the email will be sent back to the FROM address.

How to use this with your own WIFI camera (only for testing purposes):
- Configure your camera to send emails to the address 'incoming_at_lifteye.es'.
- You will receive an email only when a person is found in the picture captured by your camera.

## Ideas or comments more than welcome
This service is provided only for testing purposes.
Contact us at support@tamedbytes.com

### TODOs
 - Document how to use the code (requires your own mail server).
 - Make YOLO detection more visible by highlighting the detected area.
 - Improve YOLO detection by testing different parts of the picture received.
 - Add other objects like cars or pets.
