import setuptools
from setuptools import setup

setup(
    name="multi_agent_charging_station",
    version="1.0",
    description="",
    author="YeonSu Kim",
    author_email="dustndustn26@gmail.com",
    url="https://github.com/yeonsssu26/Capstone2",
    packages=setuptools.find_packages(),
    install_requires=['scipy>=1.3.0',
                    'numpy>=1.16.4',
                    'pyglet>=1.4.0,<=1.5.0',
                    'cloudpickle>=1.2.0,<1.7.0',
                    'gym==0.19.0',
                    'pillow>=7.2.0',
                    'six>=1.16.0',
                    'imageio',
                    'imageio-ffmpeg'],
    python_requires='>=3.6'
)