import cv2
import numpy as np


def auto_canny(img, k=1.0):
    sigma = img.std()
    mean = img.mean()

    # thresholds from contrast
    lower = 0.66 * sigma
    upper = 1.33 * sigma

    # brightness compensation
    brightness_factor = np.clip(mean / 128, 0.5, 1.5)

    lower = int(max(0, lower * brightness_factor * k))
    upper = int(min(255, upper * brightness_factor * k))

    return cv2.Canny(img, lower, upper)


for i in range(250, 261):
    img = cv2.imread(f"data/targets/{i}.jpeg", 0)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    # img = cv2.equalizeHist(img)
    edges = auto_canny(img, k=1.4)
    cv2.imshow("Canny", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
