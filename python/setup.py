from setuptools import setup

package_name = 'first_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=[
        'first_pub_node'],
    data_files=[],
    install_requires=['setuptools'],
    zip_safe=True,
    author='ShotaAk',
    author_email='hoge@hoge.com',
    maintainer='ShotaAk',
    maintainer_email='hoge@hoge.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='My first ROS2 package.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'first_pub_node = first_pub_node:main',
        ],
    },
)
