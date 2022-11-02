setup(
    name='baloise-testdatagenerator',
    description='Generates test data for Guidewire TST environments',
    version='0.1.0',
    packages=find_packages(include=['generator', 'names']),
    install_requires=[
        'faker',
        'pandas'
    ],
    setup_requires=[
        'pytest-runner',
        'flake8'
    ],
    tests_require=[
        'pytest'
    ]
)
