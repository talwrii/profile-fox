import setuptools
import distutils.core

setuptools.setup(
    name='profile-fox',
    version="1.0.2",
    author='readwithai',
    long_description_content_type='text/markdown',
    author_email='talwrii@gmail.com',
    description='Open things in a particular firefox profile from the command line',
    license='MIT',
    keywords='firefox,tabs,profile',
    url='https://github.com/talwrii/profile-fox',
    packages=["profile_fox"],
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': ['profile-fox=profile_fox.main:main']
    },
)
