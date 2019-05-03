import pymysql
import requests
from bs4 import BeautifulSoup
import datetime

import sys
import logging

import rds_config

import time


def lambda_handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    """
    try:
        res = requests.get("http://www.bbc.com/news/popular/read")
        time.sleep(5)
    except requests.exceptions.ConnectionError:
        print("I failed")

    content = BeautifulSoup(res.content, 'html.parser')

    list_items = content.findAll('li', {'class':"most-popular-list-item"})

    loop = 0
    what_time_is_it = datetime.datetime.now()
    datetimef = '%s-%s-%s' % ( what_time_is_it.year, what_time_is_it.month, what_time_is_it.day )    


    #rds settings
    rds_host  = "rds-demo-mysql.cgs8fay5rk0q.us-east-2.rds.amazonaws.com"
    name = rds_config.db_username
    password = rds_config.db_password
    db_name = rds_config.db_name

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    try:
        conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=15)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        sys.exit()

    logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


    item_count = 0
    val = []

    with conn.cursor() as cur: 
        for item in list_items:
            news_ranking = item.find('span', class_="most-popular-list-item__rank")
            news_title = item.find('span', class_="most-popular-list-item__headline")
        
            if loop ==10:
                break

            elif news_ranking is not None and news_title is not None:
                sql = "INSERT INTO bbc_popular_news (date, ranking, title) VALUES (%s, %s, %s)"
                item = (datetimef, news_ranking.text, news_title.text)
                val.append(item)
                loop += 1

        cur.executemany(sql, val)
        conn.commit()

    return "Added %d items from RDS MySQL table" %(item_count)
