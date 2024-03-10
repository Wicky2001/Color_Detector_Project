import cv2
from utill import get_limits
from PIL import Image

yellow = [0,255,255]  # yellow in BGR mode
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # get the yellow colour range in HSV
    lowerLimit, upperLimit = get_limits(color=yellow)

    """
    The cv2.inRange() function expects an image in the HSV (Hue, Saturation, Value) color space, so you typically pass 
    HSV values for the lower and upper limits when generating a mask.
    
    
    """
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # convert mask to pillow format
    mask_ = Image.fromarray(mask)
    # get the bounding box of mask
    """
    The getbbox() function is specific to Pillow (Python Imaging Library) and doesn't exist for OpenCV's cv2 module.
    Thats why we convert mask into pillow format
    
    If you're working with OpenCV, you'll need to calculate the bounding box differently. You can achieve this 
    by using cv2.findContours() to find contours in the mask and then calculate the bounding box of the contour(s) using cv2.boundingRect().
    """
    bounding_box = mask_.getbbox()

    if bounding_box is not None:
        x1, y1, x2, y2 = bounding_box
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # print("mask = ", mask)
    cv2.imshow("Mask",mask)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
