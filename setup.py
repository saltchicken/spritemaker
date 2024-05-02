from setuptools import setup, find_packages
from spritemaker import Spritemaker

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name='spritemaker',
    version='0.0.1',
    author='John Eicher',
    author_email='john.eicher89@gmail.com',
    description='Testing installation of Package',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url='https://github.com/saltchicken/spritemaker',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/saltchicken/spritemaker/issues"
    # },
    # license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'spritemaker = spritemaker:main',
        ],
    },
    install_requires=['numpy']
)