# pip install --upgrade google-cloud-logging

from google.cloud import logging

def write_entry(
    process_name,
    start_datetime,
    end_datetime,
    processing_time, 
    number_of_processed_records_passed, 
    number_of_processed_records_failed):

    """
    Writes log entries to the given logger
    """
     
    logger_name="_Default"

    logging_client = logging.Client()

    logger = logging_client.logger(logger_name)

    # Struct log
    logger.log_struct(
        {
            "process_name": process_name,
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
            "processing_time": processing_time,
            "number_of_processed_records_passed": number_of_processed_records_passed, 
            "number_of_processed_records_failed": number_of_processed_records_failed
        },
        
        # high severity level is put to simplify log discovery
        severity="INFO"
    )

    print("Wrote logs to {}.".format(logger.name))


def list_entries(logger_name):
    """
    Lists the most recent entries for a given logger
    """
    logging_client = logging.Client()
    logger = logging_client.logger(logger_name)

    print("Listing entries for logger {}:".format(logger.name))

    for entry in logger.list_entries():
        timestamp = entry.timestamp.isoformat()
        print("* {}: {}".format(timestamp, entry.payload))



def delete_logger(logger_name):
    """
    Deletes a logger and all its entries
    """
    logging_client = logging.Client()
    logger = logging_client.logger(logger_name)

    logger.delete()

    print("Deleted all logging entries for {}".format(logger.name))

    

# write_entry()
write_entry('1', '2', '3', '4', '5', '6')
# list_entries("_Default")
# delete_logger("_Default")
