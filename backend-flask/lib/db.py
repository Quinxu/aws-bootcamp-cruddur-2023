from psycopg_pool import ConnectionPool
import os


class Db:
  def __init__(self):
    self.init_pool()

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

  def querry_commit_with_returning_id(self, sql, *args):
    try:
          with self.pool.connection() as conn:
              with conn.cursor() as cur:
                cur.execute(sql,*args)
                returning_id = cur.fetchone()[0]
                conn.commit() 
                return returning_id

      except Exception as error:
            self.print_sql_err(error)

      finally:
            if conn is not None:
                cur.close()
                conn.close()
                print('Database connection closed.')

  def querry_commit(self, sql):
      try:
          with self.pool.connection() as conn:
              with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit() 

      except Exception as error:
            self.print_sql_err(error)

      finally:
            if conn is not None:
                cur.close()
                conn.close()
                print('Database connection closed.')

  def query_json_object(self, sql):
    print("--------query json object sql-----")
    print(sql + "\n")
    
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(wrapped_sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
          return json[0]
    
  def query_json_object_array(self, sql):
    print("--------query json object array sql-----")
    print(sql + "\n")
    
    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(wrapped_sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
          return json[0]
  
  def query_wrap_object(self, template):
      sql = f"""
      (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
      {template}
      ) object_row);
      """
      return sql

  def query_wrap_array(self, template):
    sql = f"""  
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql

  def print_sql_err(self, err):
      # get details about the exception
      err_type, err_obj, traceback = sys.exc_info()

      # get the line number when exception occured
      line_num = traceback.tb_lineno

      # print the connect() error
      print ("\npsycopg ERROR:", err, "on line number:", line_num)
      print ("psycopg traceback:", traceback, "-- type:", err_type)

      # print the pgcode and pgerror exceptions
      print ("pgerror:", err.pgerror)
      print ("pgcode:", err.pgcode, "\n")

db = Db() 


