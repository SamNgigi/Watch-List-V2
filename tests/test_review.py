import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
  """  
  Test class to test the behaviour of the Movie class
  """

  def setUp(self):
    """ 
    Set up method that will run before every Test.
    """
    self.new_review = Review(1, 'Python is awesome', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 'A whole new World')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_review, Review))

  def test_init(self):
    self.assertEqual(self.new_review.movie_id, 1)
    self.assertEqual(self.new_review.title, 'Python is awesome')
    self.assertEqual(self.new_review.imageurl, 'https://image.tmdb.org/t/p/w500/khsjha27hbs')
    self.assertEqual(self.new_review.review, 'A whole new World')

  def tearDown(self):
    Review.all_reviews = []

  def test_save_review(self):
    self.new_review.save_reviews()
    self.assertEqual(len(Review.all_reviews), 1)

  def test_clear_review(self):
    self.new_review.clear_review()
    self
    self.assertEqual(len(Review.all_reviews), 0)

  def test_get_reviews(self):
    self.new_review.save_reviews()
    self.assertEqual(len(Review.get_reviews(self.new_review.movie_id)),1)

# if __name__ == '__main__':
#   unittest.main()