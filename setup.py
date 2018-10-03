from setuptools import setup, find_packages

setup(
    name='hoidn.utils',
    version='0.0.1.dev1',
    description='Some util code forked for Oliver Hoidn''s repo, mostly for the caching decorators',
    packages=find_packages('.'),
    install_requires=['plotly', 'meta', 'pathos'],
    zip_safe=False
)
