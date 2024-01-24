import sqlite3, yaml
from yaml.loader import SafeLoader

def loadYAML(path):
  bookmarks = []
  with open(path) as f:
    data = yaml.load(f, Loader=SafeLoader)
    for entry in data:
      bookmarks.append(
        {
          "url": entry["url"],
          "title": entry["title"],
          "tags": entry["tags"],
          "read": entry["read"],
          "type": entry["type"],
          "language": entry["language"],
        }
      )
  return bookmarks

con = sqlite3.connect("database.db")
cur = con.cursor()

existing = map(lambda x: x[0], cur.execute("SELECT (url) FROM bookmarks").fetchall())

bookmarks = loadYAML("data.yaml")
for bookmark in bookmarks:
  if bookmark["url"] in existing:
    continue
  cur.execute(
    "INSERT INTO bookmarks (url, title, tags, read, type, language) VALUES (?, ?, ?, ?, ?, ?)",
    (
      bookmark["url"],
      bookmark["title"],
      bookmark["tags"],
      bookmark["read"],
      bookmark["type"],
      bookmark["language"],     
    ),
  )
con.commit()
