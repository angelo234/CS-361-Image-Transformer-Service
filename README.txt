# To create a request to resize image(s), append/create a file called "image_transformer_pipe.txt" and write to a new line:
IN | (new width), (new height), ("image_filename") | (width2), (height2), ("image_filename2") | ...

# When the image(s) have been resized, the service will write the names of the files, all appended with "resized":
OUT | ("resized_image_filename") | ("resized_image_filename2") | ...

# Full Examples: 
IN | 500,500,"image1.png"
OUT | "resized_image1.png"

IN | 800,800,"image1.png" | 600,600,"image2.jpg" | 400, 800, "image3.jpeg"
OUT | "resized_image1.png" | "resized_image2.jpg" | "resized_image3.jpeg"


IN | 500, 500, "1987-BMW-E30-M3-V13-1080.jpg"