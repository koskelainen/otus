import json
from .get_datetime import parse_date
from .get_counter import get_int_counter, get_float_counter, get_views_counter
import logging

logging.getLogger(__name__)


class Post(object):
    def __init__(self, **options):
        self.post_id = get_int_counter(options.get('post_id', 0))
        self.datetime = parse_date(options.get('datetime', []))
        self.hubs = options.get('hubs', [])
        self.tags = options.get('tags', [])
        self.counter_positive = get_int_counter(options.get('counter_positive', 0))
        self.counter_favs = get_int_counter(options.get('counter_favs', 0))
        self.counter_views = get_views_counter(options.get('counter_views', 0))
        self.counter_comments = get_int_counter(options.get('counter_comments', 0))

        self.user = options.get('user', "")
        self.karma = get_float_counter(options.get('karma', 0))
        self.ratio = get_float_counter(options.get('ratio', 0))
        self.followers = get_int_counter(options.get('followers', 0))

    def __str__(self):
        fields = ['    {}={!r}'.format(k, v) for k, v in self.__dict__.items() if not k.startswith('_')]
        return '{}(\n{})'.format(self.__class__.__name__, ',\n'.join(fields))


def read_json(fpath):
    with open(fpath) as json_data:
        posts_from_json = json.load(json_data)
        json_data.close()
    return [Post(**m) for m in posts_from_json]


def data_from_json(file_path):
    posts_obj = read_json(file_path)
    logging.info("data_from_json: Loaded {} objects from {}".format(len(posts_obj), file_path))
    return posts_obj