import logging
import os

import azure.functions as func


def main(event: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                 event.get_body().decode('utf-8'))

    logging.info(os.getenv('ChronicleID'))
    logging.info(os.getenv('ChronicleServiceAccount'))
    logging.info(os.getenv('ChronicleRegion'))
    logging.info(os.getenv('ChronicleDataType'))
