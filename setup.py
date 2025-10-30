import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youtube-search-python",
    version="1.6.6",  # updated version to reflect httpx 0.28+ fix
    author="CertifiedDevloper (forked from Hitesh Kumar Saini)",
    license='MIT',
    author_email="rajnishmishraaa1@gmail.com",
    description="Search for YouTube content without YouTube Data API v3. Patched for httpx 0.28+.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CertifiedDevloper/youtube-search-python",  # updated repo URL
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'httpx>=0.28.1'  # fixed compatibility issue
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)