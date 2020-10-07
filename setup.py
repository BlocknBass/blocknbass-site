from setuptools import find_packages, setup

requirements = [
        "flask==1.1.2",
        "python-dotenv",
        "requests",
        "simplejson",
]

setup(
    name="blocknbass-site",
    version="2.0.0",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "autopep8",
            "wheel",
            "livereload"
        ],
        "prod": [
            "gunicorn"
        ]
    }
)
