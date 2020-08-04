from setuptools import setup, find_packages

setup(
    long_description=open("README.md", "r").read(),
    name="imgsend",
    version="0.1",
    description="send images to an url every x seconds",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/smthnspcl/imgsend",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    entry_points={'console_scripts': ['imgsend = imgsend.__main__:main']}
)
