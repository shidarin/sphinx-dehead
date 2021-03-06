#!/usr/bin/env python
"""

setup.py
========

This is a generic as possible setup.py template. The goal is to retrieve almost
all of the information from the main module file, rather than relying on values
explicitly entered here.

## Usage

This setup.py script needs to modified in the following ways:

- `MAIN_FILE` needs to be pointed at the main metadata file, this can be done
    easily by modifyng the second arg.
- `setup` kwargs need to be modified:
    - `classifiers` needs to be modified to suit your project.
    - `keywords` needs to be modified to suit your project.
- If you have files that need to be included (such as `LICENSE`, you need to
    create a MANIFEST.in file and `include FILENAME` them.

Other than that, all the metadata should live in your main file, just like
the example below.

## Metadata Example

The following should be placed in your project module's __init__.py file:
::
    __author__ = "Ivan Busquets"
    __author_email__ = "ivanbusquets@gmail.com"
    __copyright__ = "Copyright 2011, Ivan Busquets"
    __credits__ = ["Ivan Busquets", "Sean Wallitsch", ]
    __license__ = "MIT"
    __version__ = "1.2"
    __maintainer__ = "Sean Wallitsch"
    __maintainer_email__ = "sean@grenadehop.com"
    __module_name__ = "animatedSnap3D"
    __short_desc__ = "An extension to Nuke's 'snap' options for animated verts"
    __status__ = "Development"
    __url__ = 'http://github.com/ThoriumGroup/animatedSnap3D'

Note: At this time `credits` is unused.

"""
# ==============================================================================
# IMPORTS
# ==============================================================================

from setuptools import setup, find_packages
import codecs
import os
import re

# ==============================================================================
# GLOBALS
# ==============================================================================

HERE = os.path.abspath(os.path.dirname(__file__))
MAIN_FILE = os.path.join(HERE, 'sphinx_dehead', '__init__.py')

# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

# ==============================================================================
# PRIVATE FUNCTIONS
# ==============================================================================


def _find_metadata(filepath):
    """Reads all the metadata from a source file by opening manually.

    Why open and read it and not import?

    https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion

    Args:
        filepath : (str)
            Filepath to the file containing the metadata.

    Returns:
        {str: str}
            Dictionary with metadata keys and values.

    Raises:
        RuntimeError
            Cannot proceed if version or module_name not found

    """
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(filepath, 'r', 'latin1') as meta_file:
        metadata_file = meta_file.read()

    metadata = {}

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              metadata_file, re.M)
    author_match = re.search(r"^__author__ = ['\"]([^'\"]*)['\"]",
                             metadata_file, re.M)
    author_email_match = re.search(r"^__author_email__ = ['\"]([^'\"]*)['\"]",
                             metadata_file, re.M)
    copyright_match = re.search(r"^__copyright__ = ['\"]([^'\"]*)['\"]",
                                metadata_file, re.M)
    credits_match = re.search(r"^__credits__ = ['\"]([^'\"]*)['\"]",
                              metadata_file, re.M)
    license_match = re.search(r"^__license__ = ['\"]([^'\"]*)['\"]",
                              metadata_file, re.M)
    maint_match = re.search(r"^__maintainer__ = ['\"]([^'\"]*)['\"]",
                            metadata_file, re.M)
    maint_email_match = re.search(r"^__maintainer_email__ = ['\"]([^'\"]*)['\"]",
                            metadata_file, re.M)
    module_name_match = re.search(r"^__module_name__ = ['\"]([^'\"]*)['\"]",
                            metadata_file, re.M)
    short_desc_match = re.search(r"^__short_desc__ = ['\"]([^'\"]*)['\"]",
                             metadata_file, re.M)
    status_match = re.search(r"^__status__ = ['\"]([^'\"]*)['\"]",
                             metadata_file, re.M)
    url_match = re.search(r"^__url__ = ['\"]([^'\"]*)['\"]",
                             metadata_file, re.M)

    if not version_match or not module_name_match:
        raise RuntimeError("Unable to find version or module_name string.")

    if author_match:
        metadata['author'] = author_match.group(1)
    if author_email_match:
        metadata['author_email'] = author_email_match.group(1)
    if copyright_match:
        metadata['copyright'] = copyright_match.group(1)
    if credits_match:
        metadata['credits'] = credits_match.group(1)
    if license_match:
        metadata['license'] = license_match.group(1)
    if maint_match:
        metadata['maintainer'] = maint_match.group(1)
    if maint_email_match:
        metadata['maintainer_email'] = maint_email_match.group(1)
    if module_name_match:
        metadata['module_name'] = module_name_match.group(1)
    if short_desc_match:
        metadata['short_desc'] = short_desc_match.group(1)
    if status_match:
        metadata['status'] = status_match.group(1)
    if version_match:
        metadata['version'] = version_match.group(1)
    if url_match:
        metadata['url'] = url_match.group(1)

    return metadata

# ==============================================================================
# MAIN
# ==============================================================================

metadata = _find_metadata(MAIN_FILE)

setup(
    name=metadata['module_name'],
    version=metadata['version'],
    description=metadata.get('short_desc', ''),
    long_description=LONG_DESCRIPTION,

    # The project URL.
    url=metadata.get('url', ''),

    # Author & Maintainer details
    author=metadata.get('author', ''),
    author_email=metadata.get('author_email', ''),
    maintainer=metadata.get('maintainer', ''),
    maintainer_email=metadata.get('maintainer_email', ''),

    # Choose your license
    license=metadata.get('license', ''),

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',

        # OS
        'Operating System :: OS Independent',

        # Language
        'Natural Language :: English',
    ],

    # What does your project relate to?
    keywords='sphinx bootstrap octopress html rst partial',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages.
    packages=find_packages(exclude=['tests']),

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed.
    install_requires=['argparse', 'beautifulsoup4'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={},
    include_package_data=True,

    # Targeted OS
    platforms='any',

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'sphinx-dehead=sphinx_dehead:main',
        ],
    },
)
