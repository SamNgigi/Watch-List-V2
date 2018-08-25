class Review:

  # List to store all our reviews for now
  all_reviews = []

  def __init__(self, movie_id, title, imageurl, review):
    self.movie_id = movie_id
    self.title = title
    self.imageurl = imageurl
    self.review = review

  def save_review(self):
    """  
    Saves reviews
    """
    Review.all_reviews.append(self)

  @classmethod
  def get_reviews(cls, id):
    """  
    Function that returns all the reviews for a specific movie.
    """
    response = []

    for review in cls.all_reviews:
      if review.movie_id == id:
        response.append(review)

    return response

  @classmethod
  def clear_reviews(cls):
    """  
    Function that removes all reviews from all_reviews
    """
    Review.all_reviews.clear()