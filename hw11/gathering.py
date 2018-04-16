import logging
import sys
from hw11.parsers.work_json import data_from_json
from hw11.parsers.work_csv import write_posts_to_csv
from hw11.scrappers.core_scrapy import run_inline_scrapper
from hw11.constants.consts import JSON_SRC_FILE, CSV_FILE
import pandas as pd
from collections import Counter
import ast

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def gather_process():
    """
    Gathering habrahabr.ru
    :return:
    """
    logger.info("Gather begin")
    run_inline_scrapper()
    logger.info("Gather end")


def convert_data_to_table_format():
    """
    This step be may skip if set rule in 'setting.py'
    :return:
    """
    logger.info("Transform begin")
    print("Just convert data from json to csv format.")
    posts_obj = data_from_json(JSON_SRC_FILE)
    write_posts_to_csv(CSV_FILE, posts_obj)
    logger.info("Transform end")


def stats_of_data():
    """
    Show results
    :return:
    """
    logger.info("Stats begin")
    df = pd.read_csv(CSV_FILE, sep='\t')
    print("Example results:")
    print(df.head(4))
    print("Shape results:", df.shape)

    users = df.loc[:, ['user', 'karma', 'ratio', 'followers']]
    users.drop_duplicates(subset=['user'], inplace=True)
    print("Top 10 users:")
    print(users.sort_values(by=['ratio', 'karma', 'followers'], ascending=False).head(10))

    df = df.assign(tags_list=df.tags.apply(lambda x: ast.literal_eval(x)))
    all_tags = []
    [[all_tags.append(tag) for tag in row['tags_list']] for _, row in df.iterrows()]
    tags_ratio = Counter(all_tags)
    df_tags = pd.DataFrame(data=list(tags_ratio.items()), columns=['name', 'count'])
    print("Top 10 tags:")
    print(df_tags.sort_values(['count'], ascending=False).head(10))
    logger.info("Stats end")


if __name__ == '__main__':

    logger.info("Work started")
    assert sys.argv[1], "Do you need get arg: gather, transform or stats"
    if sys.argv[1] == 'gather':
        gather_process()
    elif sys.argv[1] == 'transform':
        convert_data_to_table_format()
    elif sys.argv[1] == 'stats':
        stats_of_data()
    else:
        print("Do you need get arg: gather, transform or stats")

    logger.info("Work ended")
