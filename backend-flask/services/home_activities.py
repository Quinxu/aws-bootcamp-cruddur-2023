from datetime import datetime, timedelta, timezone

#Acquiring a Tracer
from opentelemetry import trace
tracer = trace.get_tracer("home.activities")
#

from lib.db import pool, query_wrap_array

class HomeActivities:
  def run():
    
    print("2*********************************")
    #logger.info('Hello Cloudwatch! from  /api/activities/home')

    #Creating Spans 
    with tracer.start_as_current_span("home-activities-mock-data"):
    #
      #Adding Attributes to Spans
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      #
      sql = query_wrap_array("""SELECT * FROM activities""")
      
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
      print("3 jason[0] *********************************")
      print(json[0])
      return json[0]

      span.set_attribute("app.result_length", len(results))
    return results