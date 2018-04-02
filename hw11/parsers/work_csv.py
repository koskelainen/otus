import csv
from parsers.work_json import Post
import logging

logging.getLogger(__name__)

CSV_DELIMITER = '\t'
CSV_QUOTERCHAR = '"'


def write_csv(file_path, objects, list_attr):
    counter_lines = 0
    with open(file_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile,
                                delimiter=CSV_DELIMITER,
                                quotechar=CSV_QUOTERCHAR,
                                quoting=csv.QUOTE_MINIMAL,
                                fieldnames=list_attr)
        writer.writeheader()
        counter_lines += 1
        for obj in objects:
            row = {}
            for k in obj.__dict__.keys():
                if k in list_attr:
                    row.update({k: getattr(obj, k)})
            writer.writerow(row)
            counter_lines += 1
    logging.info("write_csv: Wrote down {} lines in {}".format(counter_lines, file_path))


def check_attr(file_path, objects, list_attr):
    if isinstance(objects, list) and isinstance(objects[0], Post):
        if not list_attr or not isinstance(list_attr, list):
            list_attr = list(objects[0].__dict__.keys())
        write_csv(file_path, objects, list_attr)
    else:
        logging.error("Func check_attr: ValueError : 'objects'")


def write_posts_to_csv(file_path, objects, list_attr=None):
    check_attr(file_path, objects, list_attr)