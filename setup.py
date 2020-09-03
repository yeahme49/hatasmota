from setuptools import setup, find_packages


long_description = open("README.md").read()

setup(
    name="HATasmota",
    version="0.0.1",
    license="MIT",
    url="https://github.com/emontnemery/ha-tasmota",
    author="",
    author_email="",
    description="Python module to help parse and construct Tasmota MQTT messages.",
    long_description=long_description,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=list(val.strip() for val in open("requirements.txt")),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)