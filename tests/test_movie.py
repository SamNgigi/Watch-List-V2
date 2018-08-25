import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
  """  
  Test class to test the behaviour of the Movie class
  """

  def setUp(self):
    """ 
    Set up method that will run before every Test.
    """
    self.new_movie = Movie(1, 'Python is awesome', 'A whole new World', 'khsjha27hbs', 9, 777)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_movie, Movie))

  def test_init(self):
    self.assertEqual(self.new_movie.id, 1)
    self.assertEqual(self.new_movie.title, 'Python is awesome')
    self.assertEqual(self.new_movie.overview, 'A whole new World')
    self.assertEqual(self.new_movie.poster, 'https://image.tmdb.org/t/p/w500/khsjha27hbs')
    self.assertEqual(self.new_movie.vote_average, 9)
    self.assertEqual(self.new_movie.vote_count, 777)

  

# if __name__ == '__main__':
#   unittest.main()