#!/usr/bin/env python
import unittest

from tests.test_custom_dict import BaseCustomDictTestCase

try:
    from requests_cache.backends.storage.gridfspickledict import GridFSPickleDict
    from requests_cache.backends.storage.mongodict import MongoDict

except ImportError:
    print("pymongo not installed")
else:

    class MongoDictTestCase(BaseCustomDictTestCase, unittest.TestCase):
        dict_class = MongoDict
        pickled_dict_class = GridFSPickleDict

    if __name__ == '__main__':
        unittest.main()
