""" UNITTEST file_storage.py """

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import path, remove

flst = FileStorage()


class TestFileStorage(unittest.TestCase):
    """ UNITTEST FOR FILESTORAGE * """

    def test_filepath(self):
        """ UNITTEST FOR FILEPATH * """
        self.assertTrue(type(flst._FileStorage__file_path) is str)
        tmp = FileStorage()
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        tmp.save()
        self.assertTrue(path.exists("file.json"))

    def test_object(self):
        """ UNITTEST FOR OBJECT """
        tmp = FileStorage()
        self.assertTrue(type(tmp._FileStorage__objects) is dict)
        self.assertTrue(type(tmp.all()) is dict)

    def test_new(self):
        """ UNITTEST FOR NEW TEST * """
        tmp = flst.all().copy()
        BaseModel()
        self.assertFalse(tmp == flst.all())

    def test_save(self):
        """ UNITTEST FOR SAVE * """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        base = BaseModel()
        base.save()
        with open("file.json") as f:
            tmp = json.load(f)
        self.assertTrue(type(tmp) is dict)

    def test_reload(self):
        """ UNITTEST FOR RELOAD * """
        flst1 = FileStorage()
        flst1.save()
        flst1.reload()
        tmp = flst1.all()
        BaseModel()
        flst1.save()
        flst1.reload()
        self.assertNotEqual(tmp, flst1.all())


if __name__ == '__main__':

    unittest.main()
