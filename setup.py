#! /usr/bin/env python
from setuptools import setup

setup(name="entity-extractor",
      version="0.01",
      author="Raymond Klass",
      author_email="raymondklass@gmail.com",
      description="Entity Extraction, Recognition, and Translation to RDF",
      license="MIT",
      packages=["entity_extractor"],
      install_requires=["nltk"],
      url:"https://github.com/RaymondKlass/entity-extract"
      )