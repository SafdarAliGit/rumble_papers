from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rumble_papers/__init__.py
from rumble_papers import __version__ as version

setup(
	name="rumble_papers",
	version=version,
	description="App for Rumble Papers.",
	author="Tech Ventures",
	author_email="info@techventures.com.pk",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
