#!/usr/bin/env python3
"""
Site24x7 CLI Setup Configuration
Generated automatically by AI from Site24x7 API documentation
"""

import os
import sys
from setuptools import setup, find_packages

# Read version from package
version = "1.20250725.1943"

# Read README for long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Site24x7 CLI - Comprehensive monitoring and management tool"

# Read requirements
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    try:
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        return [
            'click>=8.0.0',
            'rich>=12.0.0',
            'requests>=2.28.0',
            'pydantic>=1.10.0',
        ]

setup(
    name='site24x7-cli',
    version=version,
    description='Comprehensive Site24x7 CLI for monitoring and management',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='Site24x7 AI Agent',
    author_email='support@site24x7.com',
    url='https://github.com/site24x7/site24x7-cli',
    project_urls={
        'Documentation': 'https://github.com/site24x7/site24x7-cli/blob/main/README.md',
        'Source Code': 'https://github.com/site24x7/site24x7-cli',
        'Issue Tracker': 'https://github.com/site24x7/site24x7-cli/issues',
        'Site24x7 Platform': 'https://www.site24x7.com',
        'API Documentation': 'https://www.site24x7.com/help/api/',
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'site24x7=site24x7_cli.main:cli',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    keywords=[
        'site24x7', 'monitoring', 'cli', 'api', 'devops', 'infrastructure',
        'uptime', 'performance', 'alerting', 'synthetic monitoring',
        'real user monitoring', 'apm', 'log management', 'server monitoring'
    ],
    license='MIT',
    zip_safe=False,
    platforms=['any'],
    
    # Package data
    package_data={
        'site24x7_cli': [
            'config/*.json',
            'templates/*.txt',
            'templates/*.json',
        ],
    },
    
    # Additional metadata
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'flake8>=5.0.0',
            'mypy>=0.991',
            'isort>=5.10.0',
        ],
        'yaml': [
            'PyYAML>=6.0',
        ],
        'completion': [
            'click-completion>=0.5.2',
        ],
    },
    
    # CLI options
    cmdclass={},
    
    # Test configuration
    test_suite='tests',
    tests_require=[
        'pytest>=7.0.0',
        'pytest-cov>=4.0.0',
        'responses>=0.22.0',
    ],
)
