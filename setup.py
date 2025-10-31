import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youtube-search-python",
    version="1.6.6.post2",  # includes httpx 0.28+ & channel.id TypeError fixes
    author="CertifiedDevloper (forked from Hitesh Kumar Saini)",
    author_email="rajnishmishraaa1@gmail.com",
    description="Search for YouTube content without YouTube Data API v3. Patched for httpx 0.28+ and channel.id fix.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/CertifiedDevloper/youtube-search-python",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "httpx>=0.28.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)