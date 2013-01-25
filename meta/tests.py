from os import path

import models

from django.test import TestCase
import yaml


models_path = path.join(path.dirname(path.abspath(__file__)), 'models.yaml')
models_info = yaml.load(open(models_path, 'r'))


class SimpleTest(TestCase):

    fixtures = ['data.json']
    info = {}

    def setUp(self):
        for name, meta in models_info.items():
            self.info[name.capitalize()] = meta

    def test_has_created_models(self):
        for name in self.info:
            self.assertTrue(hasattr(models, name))

    def test_model_fields(self):
        for name, meta in self.info.iteritems():
            model = getattr(models, name)()
            for field in meta['fields']:
                type, name_, title = field.values()
                self.assertTrue(hasattr(model, name_))
