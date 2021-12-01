from PIL import Image

import time

file_path = "image_transformer_pipe.txt"

def parse_user_request(str_request):
	image_data = str_request.split(",")
	
	new_width = -1
	new_height = -1
	img_name = ""
	new_img_name = ""
	
	try:
		if len(image_data) != 3:
			return False, new_width, new_height, img_name, new_img_name
		
		new_width = int(image_data[0])
		new_height = int(image_data[1])
		img_name = image_data[2].replace('"', '').lstrip(' ').rstrip(' ')
		new_img_name = "resized_" + img_name
	
		return True, new_width, new_height, img_name, new_img_name
	
	except:
		return False, new_width, new_height, img_name, new_img_name
	

# Returns true if successful and false if an error occurred
def resize_image(img_name, new_img_name, new_width, new_height):
	try:			
		# Opens and resizes the image
		# and creates the new resized image
		with Image.open(img_name)	as img:
			new_img = img.resize((new_width, new_height))
			new_img.save(new_img_name)
			
			return True
		
	# If any exception was thrown, return false
	except:
		return False
	

def process_resizing_requests(data):
	out_str = '\nOUT'
	
	# Go through the list of images and resize each
	for i in range(1, len(data)):
		# Parse the current image resizing request
		result, new_width, new_height, img_name, new_img_name = parse_user_request(data[i])
		
		# Stop if couldn't parse user request
		if not result:
			out_str += " | ERROR PARSING USER REQUEST!"
			return out_str
		
		result = resize_image(img_name, new_img_name, new_width, new_height)
		
		if result:
			out_str += ' | "' + new_img_name + '"'
		else:
			out_str += " | ERROR RESIZING IMAGE: " + img_name
			return out_str
	
	return out_str


# Process user requests until they press Ctrl + C
while True:
	
	try:
		# Source: https://stackoverflow.com/a/54278929
		# Read in the pipe file
		with open(file_path, 'r+') as pipe_file:
			line = ""
			
			# Get data from last line of file
			for line in pipe_file:
				pass
			last_line = line
			
			data = last_line.split("|")
			
			# If last line of the file begins with IN, then process the user request
			if data[0].strip() == "IN":
				# Process the current requests 
				# and return output message string containing resized image filenames	
				out_str = process_resizing_requests(data)

				# Write the outputted resized images
				pipe_file.write(out_str)
				
	except FileNotFoundError:
		pass
	
	# Sleep for one second before checking pipe file again for user requests
	time.sleep(1)
	
