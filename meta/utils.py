from os import path

from django.db import models
import yaml


FIELDS = {'char': models.CharField,
          'int': models.IntegerField,
          'date': models.DateField}


def load_models(locals_, filename='models.yaml'):
    PATH = path.dirname(path.abspath(locals_['__file__']))

    with open(path.join(PATH, filename), 'r') as data:
        ymodels = yaml.load(data)

        for model, meta in ymodels.iteritems():

            Meta = type('Meta', (object,), {'verbose_name': meta['title']})

            meta_ = {'Meta': Meta,
                     '__module__': Meta.__module__}
            for field in meta['fields']:
                type_, name, title = field.values()
                meta_.update({name: FIELDS[type_](max_length=100,
                                                  verbose_name=title)})
            model_name = model.capitalize()
            locals_[model_name] = type(model_name, (models.Model,), meta_)
