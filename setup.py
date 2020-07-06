import os

from setuptools import setup

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, "README.md"), encoding="utf-8") as fd:
    long_description = fd.read()

extras_require = {"image": ["utoolbox-image"]}

# add complete packages
extras_require["complete"] = list(sum(extras_require.values(), []))

setup(
    # published project name
    name="utoolbox",
    # from dev to release
    #   bumpversion release
    # to next version
    #   bump patch/minor/major
    version="0.6.7",
    # one-line description for the summary field
    description="Metapackage for uToolbox, a Python image processing package for LLSM.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # project homepage
    url="https://github.com/liuyenting/utoolbox",
    # name or organization
    author="Liu, Yen-Ting",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
    ],
    keywords="microscopy",
    python_requires="~=3.7",
    # use pyproject.toml to define build system requirement
    # setup_requires=[
    # ],
    # other packages the project depends on to run
    #   install_requires -> necessity
    #   requirements.txt
    install_requires=["utoolbox-core>=0.0.21"],
    # additional groups of dependencies here for the "extras" syntax
    extras_require=extras_require,
    zip_safe=True,
)
