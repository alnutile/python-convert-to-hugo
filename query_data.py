from convert import Convert
import mysql.connector
from mysql.connector import MySQLConnection, Error
import dotenv
import os

dotenv.load_dotenv()


class QueryData:

    def __init__(self):
        self.table = os.getenv("DB_TABLE")
        self.tagging = os.getenv("TAGGING")
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )

        self.convert = Convert()

        self.cursor = self.conn.cursor()

    def handle(self):
        """ get all the data and iterate over the content """
        try:
            rows = self.all()
            for row in rows:
                item = self.parse_item(row)
                print(f"Writing item {item['title']}")
                item = self.convert.convert_item(item)
                self.convert.write_converted_item(item)

        except Error as e:
            print(e)

        finally:
            self.cursor.close()
            self.conn.close()

    def all(self):
        """ connect to db """
        self.cursor.execute(f"SELECT * FROM {self.table}")
        return self.cursor.fetchall()

    def get_tags(self, model_id):
        """ get all the tags from the system """
        self.cursor.execute(
            f"SELECT tags.name FROM post_tag LEFT JOIN tags on tags.id=post_tag.tag_id where post_id={model_id}")
        tags = self.cursor.fetchall()
        all_tags = []
        for tag in tags:
            all_tags.append(tag[0])

        return ", ".join(all_tags)

    def parse_item(self, item):
        """ pass the one item to convert """
        tags = None
        if self.tagging == True:
            tags = self.get_tags(item[0])
        model = {
            "id": item[0],
            "title": item[1],
            "body": item[2],
            "active": item[4],
            "tags": tags,
            "created_at": item[5].strftime("%Y-%m-%d")
        }
        return model
