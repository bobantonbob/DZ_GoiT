# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter

class RegularSpiderPipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("authors.sqlite")

        sql_request = (
            "CREATE TABLE IF NOT EXISTS authors ("
                "id integer PRIMARY KEY NOT NULL,"
                "author varchar(255) NOT NULL,"
                "quote text NOT NULL"
            ");"
        )

        cur = self.conn.cursor()

        try:
            cur.execute(sql_request)
            self.conn.commit()
        except sqlite3.Error as e:
            spider.logger.error(e)
        finally:
            cur.close()

    def close_spider(self, spider):
        spider.logger.info("Results from db:")

        cur = self.conn.cursor()

        try:
            cur.execute(f"SELECT * FROM authors")
            rows = cur.fetchall()

            for row in rows:
                spider.logger.info(row)

        except sqlite3.Error as e:
            spider.logger.error(e)
        finally:
            cur.close()

        self.conn.close()

    def process_item(self, item, spider):
        sql_request = f'INSERT INTO authors(author, quote) VALUES(?, ?);'

        cur = self.conn.cursor()

        try:
            cur.execute(sql_request, [item["author"], item["quote"]])
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            cur.close()
        return item
