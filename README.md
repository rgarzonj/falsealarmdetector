# Improving movement detections in WIFI Outdoor cameras
I am using this code with an outdoor ieGeek WIFI camera to filter false movement detection emails. My camera sends an email every time a movement is detected but most of the times there is no interest in the picture. This code filters the emails and re-sends back only the emails that contain a picture where a person is detected by YOLOv1 neural network.

This code does the following:
- Downloads emails from a mailbox using POP3.
- Checks the pictures in the emails using YOLOv1 network.
- If the picture contains a person, sends back an email with the picture.

If you want to test it:
- Send an email with a picture that includes a person to the following email address: incoming_at_lifteye.es
- If the picture contains a person, you will receive an email with such picture.

How to use this with your own WIFI camera (only for testing purposes):
- Configure your camera to send emails to incoming_at_lifteye.es.
- You will receive an email only when a person is found in the picture captured by your camera.

## Ideas or comments more than welcome
This service is provided only for testing purposes.
Contact us at support@tamedbytes.com

### TODOs
 - Document how to use the code (requires your own mail server)
 - Improve YOLO detection by testing different parts of the picture received.
 - Add other objects like cars or pets.
