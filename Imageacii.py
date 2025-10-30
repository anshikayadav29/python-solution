from PIL import Image

# Characters used to build the output text
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

def image_to_ascii(path, new_width=100):
    try:
        image = Image.open(path)
    except:
        print("Image not found at given path!")
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    
    pixel_count = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:(i+new_width)] for i in range(0, pixel_count, new_width)])
    
    print(ascii_img)
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)
    print("\n✅ ASCII Art saved as 'ascii_image.txt'")

# Example use
path = input("Enter image path: ")
image_to_ascii(path)
