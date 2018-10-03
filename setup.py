from setuptools import setup, find_packages

setup(
    name='hoidn_utils',
    version='0.0.2',
    description='Some util code forked for Oliver Hoidn''s repo, mostly for the caching decorators',
    packages=find_packages('.'),
    install_requires=['plotly', 'numpy', 'dill', 'meta', 'pathos'],
    python_requires='~=3.6',
    #zip_safe=False
)
