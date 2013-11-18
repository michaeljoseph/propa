"""
propa.

Usage:
  propa [options] command <param> <another_params>
  propa [options] another-command <param>

  propa -h | --help

Options:
  --kw-arg=<kw>         Keyword option description.
  -b --boolean          Boolean option description.
  --debug               Debug.

  -h --help             Show this screen.
"""

from docopt import docopt
import logging

import propa

log = logging.getLogger(__name__)


def main():
    arguments = docopt(__doc__, version=propa.__version__)
    debug = arguments['--debug']
    logging.basicConfig(level=logging.DEBUG if debug else logging.INFO)
    log.debug('arguments: %s', arguments)
