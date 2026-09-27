class Solution():
    def rotate(self, image):
        """
        rotate the image by 90 degrees in place
        """
        image[:] = list(zip(*image[::-1]))