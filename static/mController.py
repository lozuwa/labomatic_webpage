import os
import sys
import cv2
import numpy as np
from . import views
from . import LoadObjectDetectionModel as LoadObjDect
from impy.preprocess import preprocessImage
# import LoadObjectDetectionModel as LoadObjDect

# Global variables
obj = LoadObjDect.LoadObjectDetectionModel()
prep = preprocessImage()

def classify_file(path = None, width_patches = None, height_patches = None):
	"""
	Given the path of an image, the image is preprocessed and then
	an instance of an Object detection model classifies it.
	Args:
		path: A string that contains the path where the image is located.
	Returns:
		A string that contains the path of the image after classification.
	"""
	# assertions
	if path == None:
		raise Exception("Path cannot be empty")
	if width_patches == None:
		width_patches = 4
	if height_patches == None:
		height_patches = 3
	assert os.path.isfile(path) == True,\
				 "Image file does not exist in specified path: {}".format(path)
	# Clean tmp directory
	os.system("rm ../tmp/*")
	# Read image
	frame = cv2.imread(path)
	height, width, depth = frame.shape
	# Preprocess image
	patches, nh, nw = prep.divideIntoPatches(image_width=width,
																						image_height=height,
																						padding="VALID_FIT_ALL",
																						number_patches=(width_patches, height_patches))
	# Crop and save patches
	paths_to_patches = []
	for index, patch in enumerate(patches):
		# decode patch
		iy, ix, y, x = patch
		# Save image's patch
		path_to_save = os.path.join(os.getcwd(), "tmp", "".join(["tmp", str(index), ".jpg"]))
		frame_patch = frame[iy:y, ix:x, :]
		cv2.imwrite(path_to_save, frame_patch)
		paths_to_patches.append(path_to_save)
	results = obj.classifyFiles(paths_to_patches)
	paths_to_results = [i for i in results.keys()]
	return paths_to_results

if __name__ == "__main__":
	r = classify_file("/home/pfm/Documents/pfm/web/backend/LabomaticModels/media/Ascaris lumbricoides_17_6_12_589278.jpg", 4, 3)
