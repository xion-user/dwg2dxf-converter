from setuptools import setup, find_packages

setup(
    name="dwg2dxf-converter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["ezdxf>=1.1.0"],
    entry_points={
        'console_scripts': [
            'dwg2dxf=cli:main',
        ],
    },
    author="Your Name",
    description="DWG to DXF converter and DXF entity extractor using ODA File Converter and ezdxf.",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
