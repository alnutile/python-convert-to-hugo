import pytest
from query_data import QueryData
import mysql.connector
from mysql.connector import MySQLConnection, Error
import dotenv
import os
import dotenv
dotenv.load_dotenv()


class TestQueryData:

    def test_connect(self):
        """ query all """
        client = QueryData()
        assert isinstance(
            client.conn, mysql.connector.connection.MySQLConnection)

    def test_query_all(self):
        client = QueryData()
        results = client.all()
        assert results is not None

    def test_get_tags(self):
        client = QueryData()
        tags = client.get_tags(267)
        assert tags == "windows, linux, wsl, php"

    def test_query_one(self):
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        client = QueryData()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts LIMIT 1")
        row = cursor.fetchone()
        #row = row.items()
        row = client.parse_item(row)
        assert row['id'] == 1
        assert row['title'] == "DrupalCamp Western Mass"
        assert row['active'] == 1
        assert row['created_at'] == "2013-01-14"
