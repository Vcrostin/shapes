from setuptools import find_packages, setup
setup(
    name='GeometricShapes',
    packages=find_packages(include=['shapes']),
    version='0.1.0',
    description='Making calculations of geometric shapes easier',
    author='BikramGhuku',
    long_description=readme(),
    url="https://github.com/Bikram-ghuku/shapes",
    license='MIT',
    install_requires=['scipy==1.8.1'],
    tests_require=['pytest==4.4.1'],
    test_suite='test.py',
)
