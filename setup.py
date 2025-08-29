import setuptools
from setuptools import find_packages,setup

__version__ = "0.1.0"

with open("README.md",encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "01.cnn_classifier_template"
AUTHOR_NAME = "Mahadevkharmate"
AUTHOR_EMAIL = "mahadev.ds994@gmail.com"
# Setup script for the CNN Classifier Template project
setuptools.setup(
    name=REPO_NAME, # Package name
    version=__version__, # Version for release tracking
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A template for building CNN classifiers or any other Deep Learning models",
    long_description=long_description, # Detailed description (from README)
    long_description_content_type="text/markdown",
    url = "https://github.com/Mahadevkharmate/01.cnn_classifier_template",
    download_url = "https://github.com/Mahadevkharmate/01.cnn_classifier_template/archive/refs/tags/v0.1.0.zip",
    project_urls={
        "Bug Tracker": "https://github.com/Mahadevkharmate/01.cnn_classifier_template/issues"
    },
    package_dir={"": "src"},    # Source code is in the src directory
    packages=setuptools.find_packages(where="src"), # Finds packages inside src/
    #include_package_data=True,                   # Include non-code files (e.g., configs, models)

    install_requires=[           # Dependencies for running
        "tensorflow>=2.9.0",
        "opencv-python",
        "fastapi",
        "uvicorn",
        "pydantic",
        "pyyaml",
        "scikit-learn",
        "matplotlib",
        "numpy",
        "pandas",
        "seaborn",
        "requests",
        "tqdm",
        "pillow",
        "scipy",

    ],
    extras_require={            # Optional dependencies
        "dev": [                # For development
            "black",
            "flake8",
            "mypy",
            "pytest",
            "pytest-cov",
            "sphinx",
            "sphinx-rtd-theme"
        ],
        "docs": [               # For documentation
            "sphinx",
            "sphinx-rtd-theme"
        ]
    },
    entry_points={                               # Command line tools
        "console_scripts": [
            "train-model=src.train:main",        # Run `train-model` to start training
            "run-api=api.main:app",              # Run `run-api` for FastAPI
        ]
    },

    classifiers=[                               # Metadata for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Artificial Intelligence:: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",                   # Minimum Python version
)