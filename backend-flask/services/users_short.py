from lib.db import db

class UsersShort:
  def run(handle):
    sql = db.template('db/sql/users','short.sql')
    results = db.query_json_object(sql,
      handle=handle)
    return results