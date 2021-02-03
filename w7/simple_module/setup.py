import setuptools

setuptools.setup(
    name="my_great_math", # Replace with your own username
    version="0.1.0",
    author="Example Author",
    author_email="1alekseik1@gmail.com",
    description="Taylor math",
    long_description='long long',
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    # Собрать
    setup_requires=[],
    # Установить
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
