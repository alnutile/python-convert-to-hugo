import pytest
from convert import Convert
from difflib import SequenceMatcher


class TestConvert:

    def test_random_hero(self):
        """ take the raw content and add header """
        client = Convert()
        results = client.random_hero()
        assert results is not None
        assert results in client.heros

    def test_convert_header(self):
        """ take the raw content and add header """
        client = Convert()
        results = client.convert_item({
            "title": "Foo",
            "created_at": "2013-04-12",
            "body": "### Foo Bar",
            "tags": [],
            "id": 5
        })

        assert results is not None

    def test_make_header(self):
        client = Convert()
        results = client.make_header({
            "title": "Foo Baz",
            "created_at": "2013-04-12",
            "body": "### Foo Bar",
            "id": 5,
            "tags": "foo, bar, baz"
        })

        assert "2013-04-12" in results
        assert "Foo" in results
        assert "---" in results
        assert "foo--baz" in results
        assert "weight: 5" in results
        assert "tags: [foo, bar, baz]" in results
