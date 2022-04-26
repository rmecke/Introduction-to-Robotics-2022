from setuptools import setup
import os
from glob import glob

package_name = 'reactive_behaviour'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='basti',
    maintainer_email='sebastian.mai@ovgu.de',
    description='package for reactive behaviour tutorial',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller = reactive_behaviour.controller:main',
            'scoring = reactive_behaviour.scoring:main'
        ],
    },
)
