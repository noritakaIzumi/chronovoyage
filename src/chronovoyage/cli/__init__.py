# SPDX-FileCopyrightText: 2024-present Noritaka IZUMI <noritaka.izumi@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from chronovoyage.__about__ import __version__
from chronovoyage.domain.migrate import MigrateDomain
from chronovoyage.internal.config import MigrateDomainConfigFactory
from chronovoyage.internal.logger import get_default_logger

logger = get_default_logger()


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=False)
@click.version_option(version=__version__, prog_name="chronovoyage")
def chronovoyage():
    pass


@chronovoyage.command()
def migrate():
    # TODO: receive directory
    MigrateDomain(MigrateDomainConfigFactory().create_from_directory("TODO"), logger=logger).execute()
