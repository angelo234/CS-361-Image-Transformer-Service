This script resizes a jpg/png image to a specified size.

1. Install Python if not installed.

2. To start the service (service will keep running and processing images until you Ctrl + C), run the python script with:
py image_transformer.py


3. To create a request to resize image(s) (as many as you want), append/create a file called "image_transformer_pipe.txt" 
(don't need to clear file contents as only last line is read) and write to a new line:
	IN | (new width), (new height), ("image1") | (new width2), (new height2), ("image2") | (new width3), (new height3), ("image3") ...


When the image(s) have been resized, the service will write the names of the files 
all appended with "resized" on a new line starting with "OUT":
	OUT | ("resized_image1") | ("resized_image2") | ("resized_image3") ...

If you didn't write the request correctly, an error will be outputted to the file.


Full Examples: 
	IN | 500,500,"image1.png"
	OUT | "resized_image1.png"

	IN | 800,800,"image1.png" | 600,600,"image2.jpg" | 400, 800, "image3.jpeg"
	OUT | "resized_image1.png" | "resized_image2.jpg" | "resized_image3.jpeg"

	IN | 500, 500, "bmw.jpg"
	OUT | "resized_bmw.jpg"
	
	
4. To stop the service, press Ctrl + C