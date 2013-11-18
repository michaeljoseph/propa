from . import BaseTestCase

from propa import propa


class TestPropa(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            propa(),
        )
