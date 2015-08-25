#!/usr/bin/env python3

from setuptools import setup
import re

version = '0.0.1'

setup(
    name = "linkbot_diagnostics",
    packages = ["linkbot_diagnostics", ],
    version = version,
    entry_points = {
        "console_scripts":
        [
         'linkbot-diagnostics=linkbot_diagnostics.LinkbotDiagnosticGui:main',
         'linkbot-diagnostics-summary=linkbot_diagnostics.MassageData:main',
        ]
    },
    install_requires = ["PyLinkbot >= 2.3.4", "appdirs"],
    description = "Tool for testing Linkbots",
    zip_safe = False,
    include_package_data = True,
    author = "David Ko",
    author_email = "david@barobo.com",
    )
