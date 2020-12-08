import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):

    def setUp(self):
        self.animals = Album('Animals', 'Progressive Rock', 'Pink Floyd')

    def test_album_has_title(self):
        self.assertEqual('Animals', self.animals.title)

    def test_album_has_genre(self):
        self.assertEqual('Progressive Rock', self.animals.genre)

    def test_album_has_artist(self):
        self.assertEqual('Pink Floyd', self.animals.artist)