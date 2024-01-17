from setuptools import find_packages,setup

from typing import List  # for adding return type hint to function

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
     this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # repacing '\n' with '' from requirements using list comprehension
        requirements=[ req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements 

setup(
    name='ml-project',
    version='0.0.1',
    author='Gautam',
    author_email='pahwagautam786@gmail.com',
    packages=find_packages(),
    # defining function for getting requirements since I will not be typing all the packages I need.
    install_requires=get_requirements('requirements.txt') # it takes list of values.
)