from setuptools import setup, find_packages

setup(
    name="ritik-devflow",
    version="1.0.0",
    description="DevFlow CLI – Internal DevOps Automation Tool",
    author="Ritik Kumar",
    packages=find_packages(),
    install_requires=[
        "click",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "devflow=cli.devflow:main"
        ]
    },
    python_requires=">=3.9",
)
