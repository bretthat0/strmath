import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strmath",
    version="0.1.1",
    description="String parsing math library for Python",
    long_description_content_type="text/markdown",
    url="https://github.com/emtydev/strmath",
    project_urls={
        "Bug Tracker": "https://github.com/emtydev/strmath/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
