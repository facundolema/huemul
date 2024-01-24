import sqlite3 from 'sqlite3'

export default {
  async load() {
    return await getURLs()
  }
}

function getURLs() {
  return new Promise((resolve, reject) => {
    const db = new sqlite3.Database('./data/database.db');
    db.all('SELECT * FROM bookmarks', (err, rows) => {
      if (err) {
        reject(err);
      } else {
        console.log(rows);
        resolve(rows);
      }
    });
  });
}