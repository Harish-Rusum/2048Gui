def center(img, sizex, sizey):
    return (
        (sizex // 2) - (img.get_width() // 2),
        (sizey // 2) - (img.get_height() // 2),
    )
