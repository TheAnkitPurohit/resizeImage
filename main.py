import cv2

def resize_image(input_path, output_path, new_size):
    # Read the image
    img = cv2.imread(input_path)

    # Resize the image
    resized_img = cv2.resize(img, new_size)

    # Save the resized image
    cv2.imwrite(output_path, resized_img)

if __name__ == "__main__":
    # Specify input and output paths
    input_image_path = "raftaar.jpeg"
    output_image_path = "output_image_resized.jpg"

    # Specify the new size (width, height)
    new_size = (400, 500)

    # Resize the image
    resize_image(input_image_path, output_image_path, new_size)
