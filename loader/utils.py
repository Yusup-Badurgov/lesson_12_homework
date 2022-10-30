def save_picture(picture):
    filename = picture.filename
    picture.save(f'./uploads/images/{filename}')

    path_to_picture = f'/uploads/images/{filename}'

    return path_to_picture
