from setuptools import find_namespace_packages, setup

setup(
    name="odoo-to-many-tracking",
    version="14.0.0",
    url="https://github.com/andersinno/odoo-to-many-tracking",
    description="To-many tracking module for Odoo",
    author="Anders Innovations",
    author_email="support@anders.fi",
    packages=find_namespace_packages(include=["odoo.*"]),
    zip_safe=False,
)
