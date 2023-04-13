from datetime import datetime, timedelta, timezone
from lib.ddb import Ddb
from lib.db import db

class Messages:
  def run(cognito_user_id, message_group_uuid):
    model = {
      'errors': None,
      'data': None
    }
    print(f"\n========Messages==================")
    print(f"\ncognito_user_id = {cognito_user_id}")
    print(f"\nmessage_group_uuid = {message_group_uuid}")

    sql = db.template('db/sql/users','uuid_from_cognito_user_id.sql')
    formattedStr = str(sql).format(cognito_user_id)
    my_user_uuid = db.query_value(formattedStr)

    print(f"\n========UUID: {my_user_uuid}==================")

    ddb = Ddb.client()
    data = Ddb.list_messages(ddb, message_group_uuid)
    print("\n============list_messages======================")
    print(data)

    model['data'] = data
    return model