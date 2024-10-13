from PIL import Image
def main():
    with Image.open("vefore1.jpg") as img:
         print(img.size)
    
main()