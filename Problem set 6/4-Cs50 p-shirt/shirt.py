from PIL import Image,ImageOps
import sys
if len(sys.argv)==3:
  if sys.argv[2] in ["jpg", "jpeg", "png"]:
    try:
     image = Image.open(sys.argv[1])
    except FileNotFoundError:
     sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    image = ImageOps.fit(image, size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])
  else:
    sys.exit("Invalid Output")
elif len(sys.argv) <3 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
 sys.exit("Too many command-line arguments")
else:
  sys.exit("Input and output have different extensions")