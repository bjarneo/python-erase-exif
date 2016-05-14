from PIL import Image


def erase_exif(filename, outfile):
    image_file = open(filename, 'rb')

    image = Image.open(image_file)

    data = list(image.getdata())

    image_without_exif = Image.new(image.mode, image.size)

    image_without_exif.putdata(data)

    image_without_exif.save(outfile)
