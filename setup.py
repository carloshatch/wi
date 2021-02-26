from setuptools import setup

setup(
    name='wi',
    version='0.0.2',
    description='Wheel packages installation tool',
    url='http://github.com/chromano/wi',
    author='Carlos H. Romano',
    author_email='chromano@gmail.com',
    license='MIT',
    python_requires='>=3.6, <4',
    install_requires=['wheel==0.30.0', 'aiohttp==3.7.4'],
    scripts=[
        './wi'
    ],
)
