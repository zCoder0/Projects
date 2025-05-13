from setuptools import setup , find_packages


def get_requirements() -> list[str]:
    
    requirements_list :list[str]=[]
    
    with open("requirements.txt", "r") as f:
        lines = f.readlines()
        
        for line in lines:
            if line and line != '-e .':
                requirements_list.append(line)
    
    return requirements_list


setup(
    name="Mini Gpt-4",
    author="Prem",
    author_email="rajp37590@gmail.com",
    description="Mini Gpt-4",
    packages=find_packages(),
    install_requires=get_requirements(),
)