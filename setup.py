from setuptools import setup, find_packages

setup(
  name="someextension",
  packages = find_packages(),
  entry_points={
    'workflows.services': [
       'RANDOMEXTENSION = someextension.ext:Ext'
    ]
  }
)
