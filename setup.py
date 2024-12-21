from setuptools import setup, find_packages
from typing import List

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
HYP="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path,'r') as fileobj:
        requirements=fileobj.readlines()
        requirements=[req.replace("\n","")for req in requirements ]
    if HYP in requirements:
        requirements.remove(HYP)
    return requirements



setup(
    name="diabetes_project",  # Replace with your project name
    version="0.1.0",  # Version of your project
    author="Ashik N",  # Your name
    author_email="warticcotaky@gmail.com",  # Your email
    description="diabetes prediction form pima indians diabetes database",  # Brief description
    long_description=long_description,  # Long description from README
    long_description_content_type="text/markdown",  # Content type for long description
    url="https://github.com/ashiknazar/diabetes_prediction",  # Project URL (GitHub, GitLab, etc.)
    packages=find_packages(),  # Automatically find and include packages
    install_requires=get_requirements('requirements.txt')
    
      # Minimum Python version required
)
