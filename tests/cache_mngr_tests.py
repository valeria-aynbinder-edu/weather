import unittest

from mngrs.cache_mngr import CacheMngr


class CacheMngrTests(unittest.TestCase):



    def test_check_singleton(self):
        mngr1 = CacheMngr.get_instance()
        mngr2 = CacheMngr.get_instance()
        self.assertEqual(id(mngr1), id(mngr2), "More than one singleton instance created")

    def test_caching(self):
        self.mngr.get_weather("London")
        self.assertEqual("aaa", "aaa")

    def setUp(self):
        print("This is called once - before running each test")

    def tearDown(self):
        print("This is called after each test is done")

    @unittest.skip("skip this")
    def test_aaa(self):
        print("this test will be skipped")
