def album_dict(album,artist):
    
    dictionary={
        'Album':album,
        'Artist':artist
    }
    return dictionary

while True:

    artist_ =input('Please enter an artist:[Entre quite to exit]')
    album_ =input('Please enter an album:[Entre quite to exit]')
    

    if artist_ =='quite':
        break
    if album_ =='quite':
        break
    my_album_dict=album_dict(artist_,album_)

    print(my_album_dict)

