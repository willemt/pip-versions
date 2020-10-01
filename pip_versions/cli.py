#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

from cliar import Cliar

from .core import find_versions


class Versions(Cliar):
    """Pip versions.
    List the versions available to a pip package"""

    def list(self, package_name: str, include_pre: bool = False):
        """List the versions available to a package"""
        versions = find_versions(package_name, include_pre)
        for v in sorted(set(v.version for v in versions)):
            print(v)

    def latest(self, package_name: str, include_pre: bool = False):
        """Show the latest version of a package"""
        versions = find_versions(package_name, include_pre)
        print(sorted(versions)[-1].version)


def entry_point():
    Versions().parse()


if __name__ == '__main__':
    entry_point()
