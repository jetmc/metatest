from os import path

from django.db import models
import yaml

FIELDS = {'char': models.CharField,
          'int': models.IntegerField,
          'date': models.DateField}


def load_yaml_models(locals_, filename='models.yaml'):
    PATH = path.dirname(path.abspath(locals_['__file__']))

    with open(path.join(PATH, filename), 'r') as data:
        yaml_data = yaml.load(data)

        for model, meta in yaml_data.iteritems():

            Meta = type('Meta', (object,), {'verbose_name': meta['title']})
            model_meta = {'Meta': Meta,
                          '__module__': Meta.__module__}

            for field in meta['fields']:
                type_, name, title = field.values()
                model_meta.update({name: FIELDS[type_](max_length=100,
                                                       verbose_name=title)})
            model_name = model.capitalize()
            locals_[model_name] = type(model_name, (models.Model,), model_meta)
