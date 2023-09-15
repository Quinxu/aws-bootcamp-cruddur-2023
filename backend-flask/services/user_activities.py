from datetime import datetime, timedelta, timezone
class UserActivities:
  def run(user_handle):
  # def run(user_handle, xray_recorder):
    
    model = {
      'errors': None,
      'data': None
    }

    #now = datetime.now(timezone.utc).astimezone()

    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['blank_user_handle']
    else:
      sql= db.template('db/sql/users', 'show.sql')
      results = db.query_json_object_array(sql)
      #now = datetime.now()
      #results = [{
      #  'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
      #  'handle':  'Andrew Brown',
      #  'message': 'Cloud is fun!',
      #  'created_at': (now - timedelta(days=1)).isoformat(),
      #  'expires_at': (now + timedelta(days=31)).isoformat()
      #}]
      
      model['data'] = results
      # xray ---
      # subsegment = xray_recorder.begin_subsegment('mock-data')
      
      # dict = {
      #  "now": now.isoformat(),
      #  "results-size": len(model['data']),
      #   "name" : "User Activities",
      #   "id" : "5efb14e9b93499bd",
      #   "start_time" : 1678047744,
      #   "trace_id" : "1-6404F8B7-29640fcb8ee9efaa52f6b18f",
      #   "end_time" : 1678047806
      # }
      # subsegment.put_metadata('key', dict, 'namespace')
      # xray_recorder.end_subsegment()
    
    return model