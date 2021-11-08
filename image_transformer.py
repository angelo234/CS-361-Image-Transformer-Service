from PIL import Image

import time

file_path = "image_transformer_pipe.txt"

while True:
	# Source: https://stackoverflow.com/a/54278929
	with open('image_transformer_pipe.txt', 'r+') as pipe_file:
		for line in pipe_file:
			pass
		last_line = line
		
		data = last_line.split("|")
		
		if data[0].strip() == "IN":
			# output message string
			
			out_str = '\nOUT'
		
			end_index = len(data)
			
			# go through the list of images and resize each
			for i in range(1, end_index):
				image_data = data[i].split(",")
				
				new_width = int(image_data[0])
				new_height = int(image_data[1])
				img_name = image_data[2].replace('"', '').lstrip(' ')	
				new_img_name = "resized_" + img_name
				
				print(new_height)
				out_str += ' | "' + new_img_name + '"'
				
			pipe_file.write(out_str)
		
	
	time.sleep(1)
	
	break
	
	