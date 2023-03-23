from psycopg_pool import ConnectionPool
import os, sys, re
from flask import current_app as app




class Db:
  def __init__(self):
    self.init_pool()
    

  def print_in_color(self, title, sql):
    cyan ='\033[96m'
    no_color ='\033[0m'
    print(cyan + f'\n------{title} SQL Statement--------' + no_color)
    print(sql + '\n')

  def template (self, name):
    template_path = os.path.join(app.root_path, 'db', 'sql', name + '.sql')

    with open(template_path, 'r') as f:
      template_content = f.read()
    return template_content


  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

  def querry_commit(self, sql, **kwargs):
    # print("--------query commit sql-----")
    # print(sql + "\n")
    
    self.print_in_color('query commit',sql)
    
    try:
        pattern = r"\bRETURNING\b"

        with self.pool.connection() as conn:
            with conn.cursor() as cur:
              cur.execute(sql, kwargs)
              returning_id = cur.fetchone()[0]
              conn.commit() 
              if re.match(pattern,sql) is not None:
                print("--------query commit returning id")
                return returning_id

    except Exception as error:
            #self.print_sql_err(error)
          print(error)

    finally:
          if conn is not None:
              cur.close()
              conn.close()
              print('Database connection closed.')

  # def querry_commit(self, sql):
  #     try:
  #         with self.pool.connection() as conn:
  #             with conn.cursor() as cur:
  #               cur.execute(sql)
  #               conn.commit() 

  #     except Exception as error:
  #           self.print_sql_err(error)

  #     finally:
  #           if conn is not None:
  #               cur.close()
  #               conn.close()
  #               print('Database connection closed.')

  def query_json_object(self, sql):
    # print("--------query json object sql-----")
    # print(sql + "\n")
    self.print_in_color('query json object',sql)
    
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(wrapped_sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
          return json[0]
    
  def query_json_object_array(self, sql):
    # print("--------query json object array sql-----")
    # print(sql + "\n")
    
    self.print_in_color('query json object array',sql)
    
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


