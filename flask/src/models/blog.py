import uuid
import datetime
from src.common.database import Database
from src.models.post import Post


class Blog(object):
    def __init__(self, author, title, description, author_id, _id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is  None else _id


        def new_post(self, title, content, date=datetime.datetime.utcnow()):
            post = post(blog_id=self._id,
                        title=title,
                        content=content,
                        author=self.author,
                        created_date=date)
            post.save_to_mongo()

        def get_posts(self):
            Database.insert(colllection='blogs',
                            date=self.json())

        def json(self):
            return {
                'author': self.author,
                'author_id': self.author_id,
                'title': self.title,
                'description': self.description,
                '_id': self._id
            }

        @classmethod
        def from_mongo(cls, id):
            blog_data = Database.find_one(collection='blog',
                                          query={'_id': id})
            return cls(**blog_data)

        @classmethod
        def find_by_author_id(cls, author_id):
            blogs = Database.find(collection='blogs'
            query = {'author_id': author_id})