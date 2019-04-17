"""Command line interface to check the database info."""

import argparse
import logging
import os


from module import module


def _main(args):
    """Actual program (without command line parsing). This is so we can profile.
    Parameters
    ----------
    args: namespace object as returned by ArgumentParser.parse_args()
    """

    object = module.module( )
    object.otherMethod( )

    return


def main():
    """CLI to check the database info"""

    # Args parser
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-a", "--aaa", help="Help a", default=0)
    argparser.add_argument('-b', '--bbb', help="Help b", default='bbbbbbb')
    argparser.add_argument('-v', '--verbose', help="Increase logging output "
                            "(can be specified several times)", action="count", default=0)
    args = vars(argparser.parse_args())

    FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    _V_LEVELS = [logging.WARNING, logging.INFO, logging.DEBUG]
    loglevel = min(len(_V_LEVELS)-1, args['verbose'])
    logging.basicConfig(format=FORMAT, level = _V_LEVELS[loglevel])

    r = _main(args)

    logging.shutdown()

    return r

if __name__ == '__main__':
    exit(main())
