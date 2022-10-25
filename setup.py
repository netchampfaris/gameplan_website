from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gameplan_website/__init__.py
from gameplan_website import __version__ as version

setup(
	name="gameplan_website",
	version=version,
	description="Marketing pages and SAAS flow",
	author="Frappe Tech",
	author_email="developers@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
