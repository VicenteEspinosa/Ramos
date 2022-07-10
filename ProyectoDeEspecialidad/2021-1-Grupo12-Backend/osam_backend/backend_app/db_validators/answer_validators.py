from backend_app.db_validators.block_validators import validate_blocks_answer
from backend_app.db_validators.technician_validators import validate_technicians
import logging
import re
import datetime
from backend_app.db_helpers.answer_keys import (
    AUDITOR_KEYS,
    CATEGORY_DATA_KEYS,
    EXTRA_KEYS,
    LOCATION_KEYS,
    METADATA_KEYS,
    ROOT_KEYS,
    TIME_KEYS,
    TRUCK_KEYS,
    ADDITIONAL_PHOTOS_KEYS,
)


def validate_answer_data(answer_data):
    """Validate if the answer has the general structure."""

    if type(answer_data) != dict:
        return False
    keys = answer_data.keys()
    if len(keys) != len(ROOT_KEYS):
        return False
    ok_fields = 0
    for key in keys:
        if key in ROOT_KEYS:
            data = answer_data[key]
            if key == "values":
                if not validate_values(data):
                    logging.error("Wrong values data")
                    return False 
                ok_fields += 1
            elif key == "blocks":
                if not validate_blocks_answer(data):
                    logging.error("Wrong blocks data")
                ok_fields += 1
            elif key == "metadata":
                if not validate_metadata(data):
                    logging.error("Wrong metadata")
                    return False 
                ok_fields += 1
        else:
            return False
    if ok_fields == 3: 
        return True


def validate_values(question_values):
    """Validate the answers for all the questions."""

    if type(question_values) != dict:
        return False 
    else:
        for answer in question_values:
            if not type(answer) == str:
                return False
    return True


def validate_metadata(metadata):
    """Validate the metadata info with the specific structure."""

    if type(metadata) != dict:
        logging.error("Metadata invalid format. ")
        return False
    keys = metadata.keys()
    if len(keys) != len(METADATA_KEYS):
        logging.error(f"Metadata should have {len(METADATA_KEYS)} keys")
        return False 
    for key in keys:
        if key in METADATA_KEYS:
            value = metadata[key]
            if key == "timestamp_data":
                if not validate_meta_gnral_section(value, TIME_KEYS):
                    logging.error("Wrong timestamp data")
                    return False
            elif key == "auditor_data":
                if not validate_meta_gnral_section(value, AUDITOR_KEYS):
                    logging.error("Wrong auditor data")
                    return False
            elif key == "technician_data":
                if not validate_technicians(value):
                    logging.error("Wrong techinican data")
                    return False
            elif key == "location_data":
                if not validate_meta_gnral_section(value, LOCATION_KEYS):
                    logging.error("Wrong location data")
                    return False
            elif key == "category_data":
                if not validate_meta_gnral_section(value, CATEGORY_DATA_KEYS):
                    logging.error("Wrong category data")
                    return False
            elif key == "truck_data":
                if not validate_meta_gnral_section(value, TRUCK_KEYS):
                    logging.error("Wrong truck data")
                    return False
            elif key == "extras":
                if not validate_meta_gnral_section(value, EXTRA_KEYS):
                    logging.error("Wrong extra data")
                    return False
            elif key == "additional_photos":
                if not validate_meta_gnral_section(value, ADDITIONAL_PHOTOS_KEYS):
                    logging.error("Wrong additional photos data")
                    return False
        else:
            logging.error(f"Invalid key: {key}")
            return False
    return True


def validate_meta_gnral_section(section, necessary_keys):
    """Validate if the metadata has the general structure."""

    if type(section) != dict:
        return False
    else:
        keys = section.keys()
        if len(keys) != len(necessary_keys):
            return False
        for key in keys:
            if key not in necessary_keys:
                return False
    return True


def validate_timestamps(final_timestamp, initial_timestamp, initial_time, initial_date):
    """Validate if timestamps have a valid format"""

    # final_timestamp format: dd/mm/YY hh/mm/ss
    try:
        datetime.datetime.strptime(final_timestamp, "%d/%m/%Y %H:%M:%S")
    except ValueError:
        return False

    # initial_time format: hh/mm/ss
    if not re.match("(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)", initial_time):
        return False 

    # initial_date format: dd/mm/YY
    try:
        datetime.datetime.strptime(initial_date, "%d-%m-%Y")
    except ValueError:
        return False

    return True
