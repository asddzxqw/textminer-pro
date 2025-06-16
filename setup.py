from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="textminer-pro-본인이름",        # PyPI에서 유일해야 함 (예: textminer-pro-kimclaude)
    version="0.1.0",
    author="본인이름",
    author_email="your.email@example.com",
    description="텍스트 분석을 위한 Python 패키지",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/본인깃허브아이디/textminer-pro",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "nltk",
        "scikit-learn",
        "numpy",
        "langdetect",
    ],
)