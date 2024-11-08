import unittest 
from myenv.uml_classes import IdentifiableEntity

class TestIdentifiableEntity(unittest.TestCase):
    def test_getId(self):
        identifiable_entity = IdentifiableEntity('orchid-0000-1234-9363-2826')
        identifier = identifiable_entity.getId()
        self.assertEqual(identifier, 'orchid-0000-1234-9363-2826')