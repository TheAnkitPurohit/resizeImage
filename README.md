# Image Resizer with OpenCV

This Python script utilizes the OpenCV library to resize images.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)

## Introduction

This Python script provides a convenient way to resize images using the OpenCV library. It reads an image from the specified input path, resizes it to the desired dimensions, and saves the resized image to the specified output path.

## Installation

Before using the script, ensure you have OpenCV installed. You can install it using the following command:

```bash
pip install opencv-python
```

## Usage

To resize an image, run the script with the desired input and output paths, as well as the new size (width, height).

```bash
python resize_image.py
```

Make sure to update the following variables in the script according to your requirements:

- input_image_path: Path to the input image file.
- output_image_path: Path to save the resized image.
- new_size: Tuple specifying the new dimensions (width, height).

## Example

```bash
# Specify input and output paths
input_image_path = "input_image.jpg"
output_image_path = "output_image_resized.jpg"

# Specify the new size (width, height)
new_size = (300, 200)

# Resize the image
resize_image(input_image_path, output_image_path, new_size)
```




