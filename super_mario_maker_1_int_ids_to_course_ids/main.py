import argparse
import logging
import sys

import attr
import logging_tree

from super_mario_maker_1_int_ids_to_course_ids import application
from super_mario_maker_1_int_ids_to_course_ids import utils


def main():
    # if we are being run as a real program

    parser = argparse.ArgumentParser(
        description="scrape the playstation games site",
        epilog="Copyright 2020-10-24 - Mark Grandi",
        fromfile_prefix_chars='@')

    parser.add_argument("--log-to-file-path", dest="log_to_file_path", type=utils.isFileType(False), help="log to the specified file")
    parser.add_argument("--verbose", action="store_true", help="Increase logging verbosity")
    parser.add_argument("--no-stdout", dest="no_stdout", action="store_true", help="if true, will not log to stdout" )
    parser.add_argument("--id-list", dest="id_list", type=utils.isFileType(True), required=True, help="ID list, one per line")


    try:

        # set up logging stuff
        logging.captureWarnings(True) # capture warnings with the logging infrastructure
        root_logger = logging.getLogger()
        logging_formatter = utils.ArrowLoggingFormatter("%(asctime)s %(levelname)-8s: %(message)s")

        parsed_args = parser.parse_args()

        if parsed_args.log_to_file_path:

            file_handler = logging.FileHandler(parsed_args.log_to_file_path, encoding="utf-8")
            file_handler.setFormatter(logging_formatter)
            root_logger.addHandler(file_handler)

        if not parsed_args.no_stdout:
            logging_handler = logging.StreamHandler(sys.stdout)
            logging_handler.setFormatter(logging_formatter)
            root_logger.addHandler(logging_handler)


        # set logging level based on arguments
        if parsed_args.verbose:
            root_logger.setLevel("DEBUG")
        else:
            root_logger.setLevel("INFO")

        root_logger.info("########### STARTING ###########")

        root_logger.debug("Parsed arguments: %s", parsed_args)
        root_logger.debug("Logger hierarchy:\n%s", logging_tree.format.build_description(node=None))


        app = application.Application()
        app.run(parsed_args)

        root_logger.info("Done!")
    except Exception as e:
        root_logger.exception("Something went wrong!")
        sys.exit(1)