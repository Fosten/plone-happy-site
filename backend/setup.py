"""Installer for the plone.happy_site package."""

from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="plone.happy_site",
    version="1.0.0a0",
    description="Plone 6 website for Happy Baseball",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Brian Davis",
    author_email="info@happybaseball.com",
    url="https://github.com/fosten/plone.happy_site",
    project_urls={
        "PyPI": "https://pypi.org/project/plone.happy_site",
        "Source": "https://github.com/fosten/plone.happy_site",
        "Tracker": "https://github.com/fosten/plone.happy_site/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["plone"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "Plone",
        "plone.api",
        "plone.restapi",
        "plone.volto",
        "plone.exportimport",
        "collective.volto.formsupport[honeypot]",
        "collective.honeypot",
        "collective.listmonk",
        "eea.banner",
        "rss_provider",
        "kitconcept.seo",
        "pas.plugins.oidc==2.0.0",
        "pas.plugins.keycloakgroups==1.0.0b1",
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "plone.app.testing",
            "plone.restapi[test]",
            "pytest",
            "pytest-cov",
            "pytest-plone>=0.5.0",
        ],
    },
    entry_points="""
    [plone.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = plone.happy_site.locales.update:update_locale
    """,
)
