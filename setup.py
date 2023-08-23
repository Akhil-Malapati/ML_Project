from setuptools import find_packages,setup 
from typing import List

hypen = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this funtion will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hypen in requirements:
            requirements.remove(hypen)
            
    return requirements



setup(
    name = 'MLProject',
    version = '0.0.1',
    author = 'Akhil',
    author_mail = 'akhil_m@mfs.iitr.ac.in',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
    
)