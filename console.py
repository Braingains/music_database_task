import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Fink Ployd')
artist_repository.save(artist_1)

album_1 = Album('Manimals', 'Progressive Rock', artist_1)
album_repository.save(album_1)

artist_1.name = 'Pink Floyd'
artist_repository.update(artist_1)

album_1.title = 'Animals'
album_repository.update(album_1)

# artist_repository.delete(artist_1)
#can't adapt type 'builtin_function_or_method'

res = artist_repository.select_all()
for artist in res:
    print(artist.__dict__)

res = album_repository.select_all()
for album in res:
    print(album.__dict__)

# res = album_repository.list_albums_by_artist(artist_1)
# for albums in res:
#     print(album.__dict__)
#index out of range error





