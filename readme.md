## Python Conversion to Hugo

So I can move my db based Laravel blog to Hugo

```
python3 write_posts.py
```

will output all the posts to the output folder with random hero images

make sure to have a .env file with the following

DB_HOST=
DB_NAME=
DB_USER=
DB_PASS=
DB_TABLE=posts
TAGGING=false