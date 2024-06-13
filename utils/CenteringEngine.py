def centerImageX(image, surface, y):
    imgWidth = image.get_width()
    surfWidth = surface.get_width()
    return (surfWidth // 2) - (imgWidth // 2), y


def centerImageY(image, surface, x):
    imgHeight = image.get_height()
    surfHeight = surface.get_height()
    return x, (surfHeight // 2) - (imgHeight // 2)
