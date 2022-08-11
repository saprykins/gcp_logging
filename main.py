from google.cloud import logging


# def write_entry(logger_name):
def write_entry(logger_name="_Default"):
    """Writes log entries to the given logger."""
    logging_client = logging.Client()

    # This log can be found in the Cloud Logging console under 'Custom Logs'.
    logger = logging_client.logger(logger_name)

    # Make a simple text log
    # logger.log_text("Hello, world!", severity="ERROR")

    # Simple text log with severity.
    # logger.log_text("Goodbye, world!", severity="ERROR")

    # Struct log. The struct can be any JSON-serializable dictionary.
    logger.log_struct(
        {
            "name": "King Arthur",
            "quest": "Find the Holy Grail",
            "favorite_color": "Blue",
        }, 
        severity="ERROR"
    )

    print("Wrote logs to {}.".format(logger.name))


def list_entries(logger_name):
    """Lists the most recent entries for a given logger."""
    logging_client = logging.Client()
    logger = logging_client.logger(logger_name)

    print("Listing entries for logger {}:".format(logger.name))

    for entry in logger.list_entries():
        timestamp = entry.timestamp.isoformat()
        print("* {}: {}".format(timestamp, entry.payload))



def delete_logger(logger_name):
    """Deletes a logger and all its entries.
    Note that a deletion can take several minutes to take effect.
    """
    logging_client = logging.Client()
    logger = logging_client.logger(logger_name)

    logger.delete()

    print("Deleted all logging entries for {}".format(logger.name))

    

write_entry()
# list_entries("_Default")
# delete_logger("_Default")
