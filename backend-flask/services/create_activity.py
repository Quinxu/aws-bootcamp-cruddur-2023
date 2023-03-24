import uuid
from datetime import datetime, timedelta, timezone
from lib.db import db


class CreateActivity:
  def run(message, user_handle, ttl):
    print('enter create activity')
    model = {
      'errors': None,
      'data': None
    }

    now = datetime.now(timezone.utc).astimezone()

    if (ttl == '30-days'):
      ttl_offset = timedelta(days=30) 
    elif (ttl == '7-days'):
      ttl_offset = timedelta(days=7) 
    elif (ttl == '3-days'):
      ttl_offset = timedelta(days=3) 
    elif (ttl == '1-day'):
      ttl_offset = timedelta(days=1) 
    elif (ttl == '12-hours'):
      ttl_offset = timedelta(hours=12) 
    elif (ttl == '3-hours'):
      ttl_offset = timedelta(hours=3) 
    elif (ttl == '1-hour'):
      ttl_offset = timedelta(hours=1) 
    else:
      model['errors'] = ['ttl_blank']

    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['user_handle_blank']

    if message == None or len(message) < 1:
      model['errors'] = ['message_blank'] 
    elif len(message) > 280:
      model['errors'] = ['message_exceed_max_chars'] 

    if model['errors']:
      model['data'] = {
        'handle':  user_handle,
        'message': message
      }   
    else:

      expires_at = (now + ttl_offset).isoformat()
      uuid = CreateActivity.create_activity(user_handle, message, expires_at)
      
      json_object = CreateActivity.query_object_activity(uuid)
      
      model['data'] = json_object

    return model
    
    
  def create_activity(handle, message, expires_at):

    # sql = f"""
    # INSERT INTO  public.activities (user_uuid, message, expires_at)
    # VALUES (%(user_uuid)s, %(message)s, %(expires_at)s) RETURNING uuid;
    #  """
    #print (f"\033[41m------ handle = {handle} ---\033[0m]")

    sql = db.template('db/sql/activities', 'create.sql')

    paramsDict = {'handle': handle,
      'message': message, 'expires_at': expires_at
    }
    
    print ("\033[36m" + f"------ handle = {handle}, message = {message}, expires_at = {expires_at} -----\033[0m]")
    
    uuid = db.querry_commit(sql, handle = handle,
      message = message, expires_at = expires_at)
    
    return uuid

  def query_object_activity(uuid):
    sql = db.template('db/sql/activities', 'object.sql')
    return db.query_json_object(sql, uuid = uuid)


  def print_in_color(title, sql):
    cyan ='\033[96m'
    no_color ='\033[0m'
    print(cyan + f'\n------{title} SQL Statement--------' + no_color)
    print(sql + '\n')

