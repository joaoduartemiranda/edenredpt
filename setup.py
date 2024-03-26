from setuptools import setup

setup(
    name='edenredpt',
    packages=["edenredpt"],
    package_dir={"": "src"},
    include_package_data=True,
    version='0.1.0',
    description='Unofficial library for myEdenred (PT)',
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