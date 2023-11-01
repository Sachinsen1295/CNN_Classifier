import setuptools

_version_ = '0.0.1'
REPO_NAME = 'CNN_Classifier' 
AUTHOR_NAME = 'Sachinsen1295'
SOURCE_REPO = "CNNClassifer"
AUTHOR_EMAIL = "sachin.sen1295@gmail.com"


with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION=f.read()


setuptools.setup(
                 name=SOURCE_REPO,
                 version=_version_,
                 author=AUTHOR_NAME,
                 author_email=AUTHOR_EMAIL,
                 description="This is my CNN classification Project",
                 long_description=LONG_DESCRIPTION,
                 long_description_content = "text/markdown",
                 url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
                 
                  project_urls={
                      
                    "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",  
                      
                     },
                      package_dir={"":"src"},
                      packages=setuptools.find_packages(where="src")
                 )

