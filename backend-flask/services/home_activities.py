from datetime import datetime, timedelta, timezone
from lib.db import db
#Acquiring a Tracer
from opentelemetry import trace
tracer = trace.get_tracer("home.activities")
#

class HomeActivities:
  def run(cognito_user_id=None):
    
    #logger.info('Hello Cloudwatch! from  /api/activities/home')

    #Creating Spans 
    with tracer.start_as_current_span("home-activities-mock-data"):
    #
      #Adding Attributes to Spans
      # span = trace.get_current_span()
      # now = datetime.now(timezone.utc).astimezone()
      # span.set_attribute("app.now", now.isoformat())
      #
      # sql= db.template('db/sql/activities', 'home.sql')
      sql= db.template('activities', 'home.sql')

      results = db.query_json_object_array(sql)
   
      #span.set_attribute("app.result_length", len(results))
    return results
