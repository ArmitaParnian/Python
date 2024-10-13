import sys
import csv
from os.path import splitext
from PIL import Image,ImageOps
def main():

    check_command_line_arg()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirtfile = Image.open("shirt.png")
    size = shirtfile.size
    muppet = ImageOps.fit(imagefile, size)
    muppet.paste(shirtfile, shirt)
    muppet.save(sys.argv[2])
def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("too few command_line arguments")
    if len(sys.argv) > 3:
        sys.exit("too many command_line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    print(file1[1])
    print(file2)
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have diffrent extentions")
def check_extension(file):
    if file in [".jpg","jpeg",".png"]:
        return True
    return False



if __name__=="__main__":
    main()

