import cv2
import numpy as np
import time


def clean_quantification(image):
    """
    Calculates cleanliness of rail image using brown thresholding.
    params:
        image: an image in RGB format
    returns:
        a black and white image formatted in RGB color space.
    """
    start_time = time.time()

    resized_dimensions = (640, 360)

    downsized_image = cv2.resize(image, resized_dimensions)

    hsv_image = cv2.cvtColor(downsized_image, cv2.COLOR_BGR2HSV)

    browns = []
    for row in hsv_image:
        new_row = []
        for column in row:
            hue = column[0]
            saturation = column[1]
            brightness = column[2]
            if (brightness < 20) or (saturation > 20):
                new_row.append(0)
            else:
                new_row.append(255)
        browns.append(new_row)

    browns = np.array(browns).astype(np.uint8)

    # Calculate the average pixel value
    frame = cv2.cvtColor(browns, cv2.COLOR_GRAY2BGR)

    average_pixel_value = np.mean(frame)
    print(f"Average pixel value: {average_pixel_value}")
    end_time = time.time()
    print(f"time taken = {end_time - start_time}")

    # comparison = np.hstack(
    #     (
    #         cv2.resize(downsized_image, (0, 0), None, 0.25, 0.25),
    #         cv2.resize(
    #             cv2.cvtColor(browns, cv2.COLOR_GRAY2BGR), (0, 0), None, 0.25, 0.25
    #         ),
    #     )
    # )

    # cv2.imwrite("clean3_browns.png", browns)
    # cv2.imwrite("clean3_comparison.png", comparison)

    # cv2.imshow("comparison", comparison)
    # cv2.waitKey(0)


if __name__ == "__main__":
    test_image = cv2.imread("images/IMG_5158.jpg")
    clean_quantification(test_image)
