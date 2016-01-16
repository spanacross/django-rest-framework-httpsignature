from setuptools import setup


setup(
    name='djangorestframework-httpsignature',
    version='1.0.1',
    url='https://github.com/etoccalino/django-rest-framework-httpsignature',

    license='LICENSE.txt',
    description='HTTP Signature support for Django REST framework',
    long_description=open('README.rst').read(),

    install_requires=[
        'Django>=1.6.2,<1.8',
        'djangorestframework>=2.3.14,<3.4',
        'httpsig',
    ],
    author='Elvio Toccalino',
    author_email='me@etoccalino.com',
    packages=['rest_framework_httpsignature'],
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
    ]
)
