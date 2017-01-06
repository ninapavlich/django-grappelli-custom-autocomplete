from setuptools import setup, find_packages
#this is a test
setup(name = 'django-grappelli-custom-autocomplete',
      description = 'Customize the template for autocomplete lookups.',
      version = '1.2',
      url = 'https://github.com/ninapavlich/django-grappelli-custom-autocomplete',
      author = 'Nina Pavlich',
      author_email='nina@ninalp.com',
      license = 'BSD',
      packages=find_packages(),
      package_data={'': ['*.py','*.css','*.js']},
      include_package_data=True,
      install_requires = [],
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved',
            'Operating System :: OS Independent',
            'Programming Language :: Python'
      ]
)
