from pip._internal.commands import install
from pip._internal.network.session import PipSession


def find_versions(package_name: str, include_pre: bool = False):
    session = PipSession()
    x = install.InstallCommand("_", "_")
    options = x.parse_args([])[0]
    finder = x._build_package_finder(
        options=options,
        session=session,
        target_python=None,
        ignore_requires_python=False,
    )
    candidates = finder.find_all_candidates(package_name)
    for candidate in candidates:
        if not include_pre and candidate.version.pre:
            continue
        yield candidate
