import imageio as iio
img = iio.v3.imread("python/resource/img/couple.jpg")
iio.v3.imwrite("couple.jpg", img)