import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist_1 = Artist('Pink Floyd')
artist_repository.save(artist_1)

album_1 = Album('Animals', 'Progressive Rock', artist_1)
album_repository.save(album_1)

