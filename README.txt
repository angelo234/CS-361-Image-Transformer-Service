1. Install Python if not installed.

2. To start the service (service will keep running and processing images until you Ctrl + C), run the python script with:
py image_transformer.py


3. To create a request to resize image(s), append/create a file called "image_transformer_pipe.txt" 
(don't need to clear file contents as only last line is read) and write to a new line:
	IN | (new width), (new height), ("image_filename") | (width2), (height2), ("image_filename2") | ...


When the image(s) have been resized, the service will write the names of the files 
all appended with "resized" on a new line starting with "OUT":
	OUT | ("resized_image_filename") | ("resized_image_filename2") | ...

If you didn't write the request correctly, an error will be outputted to the file.


Full Examples: 
	IN | 500,500,"image1.png"
	OUT | "resized_image1.png"

	IN | 800,800,"image1.png" | 600,600,"image2.jpg" | 400, 800, "image3.jpeg"
	OUT | "resized_image1.png" | "resized_image2.jpg" | "resized_image3.jpeg"

	IN | 500, 500, "1987-BMW-E30-M3-V13-1080.jpg"
	OUT | "resized_1987-BMW-E30-M3-V13-1080.jpg"
	
	
4. To stop the service, press Ctrl + C