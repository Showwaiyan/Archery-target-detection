from cv2 import cvtColor, Laplacian, COLOR_BGR2GRAY, CV_64F


def detect_blur(image, threshold=100.0):
    grayscale_image = cvtColor(image, COLOR_BGR2GRAY)
    laplacian = Laplacian(grayscale_image, CV_64F)
    variance = laplacian.var()
    return variance < threshold, variance
