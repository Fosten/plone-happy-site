"""Installer for the plone_happy_site package."""
from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)


setup(
    name="plone_happy_site",
    version="1.0.0a1",
    description="Plone Happy Site configuration package.",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Brian Davis",
    author_email="info@happybaseball.com",
    url="https://github.com/fosten/plone-happy-site",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/plone_happy_site",
        "Source": "https://github.com/fosten/plone-happy-site",
        "Tracker": "https://github.com/fosten/plone-happy-site/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "Plone",
        "prettyconf",
        "plone.api",
        "collective.volto.formsupport[honeypot]",
        "collective.honeypot",
        "eea.banner",
    ],
    extras_require={
        "test": [
            "parameterized",
            "zest.releaser[recommended]",
            "plone.app.testing[robot]>=7.0.0a3",
            "plone.restapi[test]",
            "collective.MockMailHost",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = plone_happy_site.locales.update:update_locale
    """,
)
