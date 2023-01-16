# importing the module
import cv2
from PIL import Image
import numpy as np
import glob
import csv

# function to display the coordinates of
# of the points clicked on the image

def write_to_file(x, y, a, b):
    '''
    Writes the mouse coordinates to a text file
    '''
    # open the mouse coordinates
    with open('mouseCoordinates.txt', 'a') as f:
        # create a string ready to write to the file
        coordinates = str(x) + ',' + str(y) + ',' + str(a) + ',' + str(b) + '\n'

        # write to file
        f.write(coordinates)

def click_event(event, x, y, flags, params):

	
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        # displaying the coordinates
        # on the image window``
        font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(img, str(x) + ',' +
        #             str(y), (x,y), font,
        #             1, (255, 0, 0), 2)
        cv2.imshow('image', img)
		
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:cv2.destroyAllWindows()
		
        # displaying the coordinates
        # on the Shell
		

# driver function
if __name__=="__main__":

	# reading the image
	ls = glob.glob('snuhb/tren_positive/*.png')
	for i in ls:
		img = Image.open(i)
		img = np.array(img)
		fileid = i[-20:-4]
		# displaying the images
		# cv2.imshow('image', img)
		cv2.imshow('image',img)

		# setting mouse handler for the image

		# and calling the click_event() function
		# cv2.setMouseCallback('image', click_event)
		cv2.setMouseCallback('image', click_event)
		# data.append(x,y)
		cv2.waitKey(0)

		# wait for a key to be pressed to exit
		print(i)
		print('--------------')

		# close the windowp
		cv2.destroyAllWindows()
