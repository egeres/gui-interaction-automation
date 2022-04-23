from setuptools import setup
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name             = 'gui_interaction_automation',
    install_requires = required,
)