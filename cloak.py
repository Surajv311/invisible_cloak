import cv2
import numpy as np

capture = cv2.VideoCapture(0)
background = cv2.imread('images/image.jpg')

while capture.isOpened():
    # take each frame using read() function
    return_, img = capture.read()
    # hsv - hue saturation value
    # hsv tends to describe colors the way our human eye sees colors
    if return_:
        # we must convert rgb to hsv
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

####################
# now below will show the hsv format webcam image
#       cv2.imshow("hsv", hsv)
#       if cv2.waitKey(3) == ord('q'):
#           cv2.imwrite('image2.jpg', img)
#           break
#capture.release()
#cv2.destroyAllWindows()
####################

        # Now if we are using red cloth to hide then we must use hsv-red value
        red = np.uint8([[[0,0,255]]])
#bgr value of red (blue-0,green-0,red-255)
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # to get hsv value of red from bgr we use print
        # print(hsv_red) # we get the hsv value which would be used later in lowerbound & upperbound

        # threshold the hsv value to get only red colors - we are putting up a range for red color
        # from documentation -> lower: hue - 10, 100, 100 & higher: h+10, 255, 255
        lowerbound_red = np.array([0, 100, 100])
        upperbound_red = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, lowerbound_red, upperbound_red)
        # cv2.imshow("mask", mask) # to see if all the red color is highlighted

# in  cloth_detect  all things red would be detected
        cloth_detect  = cv2.bitwise_and(background, background, mask=mask) # bitwise_and would replace the pixels which it senses from your red cloth used to cover to the background behind the cloth
        # cv2.imshow("part1", part1)
# ~ ignoring red and masking it wth background image
# but we want to display whole background so:
# background is './image.jpg'
# now we not only want to detect and ignore red but we must also display the whole background so we will use bitwise_not
#now we can notice that earlier it was masking the 'red' part (from cloth) , now we would unmask that part and let everything else be clearly seen
        mask = cv2.bitwise_not(mask)

        # background_detect is all things not red would also get detected now
        background_detect = cv2.bitwise_and(img, img, mask=mask)
        # cv2.imshow("mask", part2)

        cv2.imshow("cloak",  cloth_detect + background_detect ) # we add them as images are actually arrays

        if cv2.waitKey(3) == ord('q'):
            break

# YOU MAY ADD MORPHOLOGY CONCEPTS FROM OPENCV DOCUMENTATION TO FURTHER IMPROVE......
capture.release()
cv2.destroyAllWindows()