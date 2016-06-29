class Movie:
  """ Movie class used in entertainment_center.py to create and store Movie objects

  Includes the following attributes:
  - title: which is the movie title
  - poster_image_url: url of the movie poster poster_image_url
  - trailer_youtube_url: url of the youtube video for the movie trailer_youtube_url
  """
  title = ""
  poster_image_url = ""
  trailer_youtube_url = ""
  def __init__(self, title="", poster_image_url="", trailer_youtube_url=""):
    self.title = title
    self.poster_image_url = poster_image_url
    self.trailer_youtube_url = trailer_youtube_url