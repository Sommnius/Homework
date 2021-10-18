import argparse
import logging

import rss
import logger

__PROGRAM_NAME__ = "RSS_Reader"
__VERSION__ = 1.1


@logger.log
def main():
    interface = argparse.ArgumentParser(prog=__PROGRAM_NAME__,
                                        description="Pure Python command-line RSS reader.",
                                        )

    interface.add_argument("--version",
                           action="version",
                           version=f"{interface.prog} version {__VERSION__}",
                           help="Print version info"
                           )

    interface.add_argument("--json",
                           action="store_true",
                           help="Print result as JSON in stdout"
                           )

    interface.add_argument("--verbose",
                           action="store_true",
                           help="Outputs verbose status messages"
                           )

    interface.add_argument("--limit",
                           type=int,
                           default=-1,
                           help="Limit news topics"
                           )

    interface.add_argument("source",
                           type=str,
                           help="RSS URL"
                           )

    args = interface.parse_args()
    if args.verbose:
        logger.logging.basicConfig(level=logging.DEBUG)
    # else:
        # logger.logging.basicConfig(level=logging.INFO)
    rss_parser = rss.Rss(args.source, args.limit)
    rss_parser.print_rss(args.json)


if __name__ == "__main__":
    main()
