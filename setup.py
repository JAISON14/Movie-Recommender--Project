from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Movie-Recommender-System"
AUTHOR_USER_NAME = "Jaison"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="1.0.0",
    author=AUTHOR_USER_NAME,
    description="Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="jaisonj1414@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
