from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name='edenredpt',
    packages=["edenredpt"],
    package_dir={"": "src"},
    include_package_data=True,
    version='0.1.2',
    description='Unofficial library for myEdenred (PT)',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='João Miranda',
    author_email='joao.duarte.miranda@gmail.com',
    url='https://github.com/joaoduartemiranda/edenredpt',
    install_requires=[
        "requests>=2.31.0"
    ],
    setup_requires=['pytest-runner>=6.0.1'],
    tests_require=['pytest>=8.1.1'],
    test_suite='tests'
)