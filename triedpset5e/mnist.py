import mnist_data

def average_digit(data, label):
    """Compute and return the average 28x28 grayscale digit with the 
    given label in the mnist dataset.
    """
    count = 0  # To keep track of the number of images with the given label
    sum_image = [[0] * 28 for _ in range(28)]  # Initialize a 28x28 zero-filled image

    for image, image_label in mnist_data.items:
        if image_label == label:
            count += 1
            for i in range(28):
                for j in range(28):
                    sum_image[i][j] += image[i][j]

    # Calculate the average only if count is greater than 0 to avoid division by zero
    if count > 0:
        average_image = [[pixel_sum // count for pixel_sum in row] for row in sum_image]
    else:
        # If count is 0, there are no images with the given label, so return None
        average_image = None

    return average_image

def main():
    # Call the average_digit function with the dataset and label 1
    avg_digit_1 = average_digit(mnist_data.items, label=8)

    # Check if there are any images with the given label and print the result accordingly
    if avg_digit_1 is not None:
        for row in avg_digit_1:
            print(row)
    else:
        print("No images found with label 1 in the dataset.")

if __name__ == "__main__":
    main()
