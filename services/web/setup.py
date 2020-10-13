from setuptools import setup, find_packages

setup(
    name="blocknbass-site",
    version="2.0.0a",

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    python_requires="~=3.8",

    install_requires=[
        "flask == 1.1.2",
        "requests",
        "simplejson",
    ],
    extras_require={
        "dev": [
            "livereload",
        ],
        "prod": [
            "gunicorn",
        ]
    }
)
