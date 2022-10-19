def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify two images with same shape"
    grey_image1 = 