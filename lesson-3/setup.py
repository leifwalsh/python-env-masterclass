from setuptools import setup

setup(
    name='lesson-3',
    version='0.1',
    py_modules=['npgeometry'],
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'hypotenuse = npgeometry:hypotenuse_main',
        ]
    }
)
