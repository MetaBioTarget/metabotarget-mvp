from setuptools import setup, find_packages

setup(
    name="metabotarget",
    version="0.2.0",
    description="Autonomous Multi-Scale Target-Based Drug Discovery & Translational AI Platform",
    author="MetaBioTarget Engineering",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.22.0",
        "scipy>=1.9.0",
        "pydantic>=2.0.0",
        "requests>=2.28.0",
        "matplotlib>=3.5.0",
        "networkx>=2.8.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
    ],
    entry_points={
        "console_scripts": [
            "metabotarget = src.cli:main",
        ],
    },
    python_requires=">=3.9",
)
