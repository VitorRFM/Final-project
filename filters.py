from PIL import Image, ImageFilter

# Apply a blur filter
def apply_blur(user_image, filter_image):
    image = Image.open(user_image)
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(filter_image.replace(".jpg", "_blurred.jpg"))

# Apply a contour filter
def apply_contour(user_image, filter_image):
    image = Image.open(user_image)
    contour_image = image.filter(ImageFilter.CONTOUR)
    contour_image.save(filter_image.replace(".jpg", "_contoured.jpg"))
    
# Apply a edge enhance filter
def apply_edge(user_image, filter_image):
    image = Image.open(user_image)
    edge_image = image.filter(ImageFilter.EDGE_ENHANCE)
    edge_image.save(filter_image.replace(".jpg", "_edge.jpg"))
    
# Apply a sharpen filter
def apply_sharpen(user_image, filter_image):
    image = Image.open(user_image)
    sharpen_image = image.filter(ImageFilter.SHARPEN)
    sharpen_image.save(filter_image.replace(".jpg", "_edge.jpg"))
    
# Apply a smooth filter
def apply_smooth(user_image, filter_image):
    image = Image.open(user_image)
    smooth_image = image.filter(ImageFilter.SMOOTH)
    smooth_image.save(filter_image.replace(".jpg", "_edge.jpg"))
    
# Apply a grayscale filter
def apply_greyscale(user_image, filter_image):
    image = Image.open(user_image)
    grayscale_image = image.convert('L')
    grayscale_image.save(filter_image.replace(".jpg", "_grayscale.jpg"))
