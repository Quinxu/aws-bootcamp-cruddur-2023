from datetime import datetime, timedelta, timezone

from lib.ddb import Ddb
from lib.db import db


class MessageGroups:
  def run(cognito_user_id):
    model = {
      'errors': None,
      'data': None
    }
    print(f"\n========MessageGroups==================")
    sql = db.template('db/sql/users','uuid_from_cognito_user_id.sql')
    print(f"\n========sql: {sql}==================")
    formattedStr = str(sql).format(cognito_user_id)
    print(f"\n========formatted sql: {formattedStr}==================")

    my_user_uuid = db.query_value(formattedStr)
    
    print(f"\n========UUID: {my_user_uuid}==================")
    ddb = Ddb.client()
    data = Ddb.list_message_groups(ddb, my_user_uuid)
    print("\n===========list_message_groups================")
    print(data)

    #MomentoCounter.reset(f"msgs/{user_handle}")
    model['data'] = data
    return model
  