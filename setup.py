"""Install script for setuptools."""

import setuptools
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="CNOS",
    version="0.0.1",
    author="Nick Heppert",
    author_email="heppert@cs.uni-freiburg.de",
    install_requires=[
        # "matplotlib",
        # "numpy",
        # "opencv-python",
        # "Pillow",
        # "pymeshlab",
        # "scikit-image",
        # "scipy",
        # "torch",
        # "torchvision",
        # "tqdm",
    ],
    description="CNOS Net Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # license="MIT",
    # url="https://github.com/chisarie/jax-agents",
    # Creates the following structure
    # CNOS/
    #   ...
    #    everything under stc/
    #   ...
    #   configs/
    #       ...
    #        everything under configs/
    #       ...
    package_dir={"CNOS": "src", "CNOS/configs": "configs"}, 
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # package_data={"CNOS/configs": ["configs"]}, # This should map configs into CNOS namespace?! --> Actually not needed
    include_package_data=True, # includes everything in the specified folders above, e.g. .yamls, make sure there is a MANIFEST.in file
    python_requires=">=3.7",
)
