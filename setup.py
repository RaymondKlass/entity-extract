#! /usr/bin/env python
from setuptools import setup

setup(name="entity-extractor",
      version="0.01",
      author="Raymond Klass",
      author_email="raymondklass@gmail.com",
      description="Entity Extraction, Recognition, and Translation to RDF",
      license="MIT",
      packages=["entity_extract"],
      install_requires=[
        "nltk", 
        "mock >= 1.0.1",
        "wikipedia"
      ],
      url="https://github.com/RaymondKlass/entity-extract"
      )