from setuptools import setup, find_packages


def get_requirements(file_path):

    with open(filename, 'r') as f:
        requirements = f.read().splitlines()
    
    # Remove the -e . entry if present
    requirements = [req for req in requirements if req != '-e .']
    
    return requirements
        


setup(
    name='ml_project',
    version='0.0.1',
    author='Naina Said',
    author_email='nainasaid2015@gmail.com',
    description='A simple machine learning project',
    packages=find_packages(),
   install_requires=get_requirements('requirement.txt')
)