from setuptools import setup, find_packages

setup(
    name='balepy',
    version='1.5.0',
    author='Mohammad, AmirAli, Erfan',
    author_email='mohammadmehrabi175@gmail.com',
    description='balepy - The most complete Python library for Bale messenger bot API',
    keywords=['bot', 'Bot', 'bale', 'robot', 'messangers', 'bale-bot', 'balepy'],
    long_description=open("README.md", encoding="utf-8").read(),
    python_requires="~=3.6",
    long_description_content_type='text/markdown',
    url='https://github.com/balepy/balepy',
    packages=find_packages(),
    install_requires=['aiohttp', 'colorama'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
    ]
)
