# we must first code for the background
# we would be removing the pixels from the cloak(we select the color of cloak) that we use to cover and replace that area with the background
import cv2
capture = cv2.VideoCapture(0) # to capture photo from camera we pass 0

while capture.isOpened():
    return_, img = capture.read() # reading from webcam
    # return_ gives bool value of True if function run successfully and img is the captured image
    if return_:
        # img is what the camera is reading
        # so once you move out of sight the webcam & press q your background would be clicked
        cv2.imshow("image", img)
        if cv2.waitKey(3) == ord('q'): # ord gives unicode value of 'q'
            # so with waitKey it would wait for ~ 3 sec and you may press 'q'
            # save the image by name of image.jpg in img
            cv2.imwrite('images/image.jpg', img)
            break

capture.release() # release all resources
cv2.destroyAllWindows() #destroy the windows