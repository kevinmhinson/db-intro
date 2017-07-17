import datetime, re

from app import db

'''
create human readable urls
  "A Post about Flask" => "a-post-about-flask"
'''

def slugify(s):
  return re.sub('[^\w]+', '-', s).lower()

'''
Entry extends db.Model
.. db is instance of SQLAlchemy class from flask-sqlalchemy
.. by extending db.Model, inherit helpers to query database
'''

class Entry(db.Model):
  # names and data to store in db
  id                 = db.Column(db.Integer, primary_key=True)
  title              = db.Column(db.String(100))
  slug               = db.Column(db.String(100), unique=True)  # url friendly title
  body               = db.Column(db.Text)
  created_timestamp  = db.Column(db.DateTime, default=datetime.datetime.now)
  modified_timestamp = db.Column(db.DateTime,
                                 default=datetime.datetime.now,
                                 onupdate=datetime.datetime.now)


  def __init__(self, *args, **kwargs):           # override __init__
    super(Entry, self).__init__(*args, **kwargs) # normal call to parent constructor.
    self.generate_slug()                         # add-in - automatically set slug

  def generate_slug(self):
    self.slug = ''
    if self.title:
      self.slug = slugify(self.title)

  def __repr__(self):                            # use repr(entry instance) to view specific object when debugging
    return '<Entry: %s>' % self.title            # e = Entry(???); repr(e) => <Entry: Title of Specific Post>