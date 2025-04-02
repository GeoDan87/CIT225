from sqlalchemy import MetaData, Table, select, create_engine, text
from sqlalchemy.engine.base import Engine, Connection
import os
import warnings

#Construct the URL to use in the database connection
#Set it up with defaults and environment varialbes for username and password
def set_db_url(dbms = 'mariadb'
               ,driver = 'pymysql'
               ,host = '127.0.0.1'
               ,port = '3306'
               ,db = 'hfh'):
    
    #Obtain the system environment variables holding the username and password
    DB_USER = os.getenv('MDB_USER', None)
    DB_PASS = os.getenv('MDB_PASS', None)
    
    #Only proceed if the DB_USER and DB_PASS are not null
    if DB_USER and DB_PASS:

        db_url = "{dbms}+{driver}://{user}:{pwd}@{host}:{port}/{db}".format(dbms=dbms,
                                                                            driver=driver,
                                                                            user=DB_USER,
                                                                            pwd=DB_PASS,
                                                                            host=host,
                                                                            port=port,
                                                                            db=db)
        return db_url
    else:
        raise Exception('Database username and/or password are None.')
        
#Create the database engine and return a SQLAlchemy Engine class
def create_db_engine() -> Engine:
    db_url = set_db_url()
    try:
        engine = create_engine(db_url)
        
    except Exception as error:
        raise Exception('Exception encountered when creating engine. {}'.format(error))
        engine = None
        
    return engine

#Connect the database engine and return a SQLAlchemy Engine class that has been connected
def connect_db_engine() -> Connection:
    engine = create_db_engine()
    
    if engine:
        try:
            engine = engine.connect()
        except:
            raise Exception('Failed to connect to database. {}'.format(error))
            
    return engine
            
#Connect to a specific database object (aka table) and return a SQLAlchemy table class    
def connect_db_object(connected_engine, object_name, schema) -> Table:
    try:
        metadata = MetaData(schema = schema)
        
        target_object = Table(object_name, metadata, autoload_with = connected_engine)
        
    except Exception as error:
        metadata = None
        
        target_object = None
        
        raise Exception('Failed to connect to the {} object in the database. {}'.format(object_name, error))
    return target_object

def insert_data(connected_engine, table, schema, data):
    
    #Connect to the target table
    target_table = connect_db_object(connected_engine, table, schema)        
    
    #Otherwise try the insert and raise exception if there is
    try:
        insert_statement = (target_table.insert()
                            .values(data))

        connected_engine.execute(insert_statement)

        connected_engine.commit()
    except Exception as error:
        raise Exception('Failed to connect to database or object. {}'.format(error))
            
def select_data(connected_engine, table, schema):
    #Try to connect to the table, create the select query and fetch the results
    try:
        #Connect to the target table
        target_table = connect_db_object(connected_engine, table, schema)
        
        #Create the select statement
        select_stmt = select(target_table)
        
        #Execute the select statement
        results = connected_engine.execute(select_stmt)
        
        #Get the columns
        columns = tuple(results.keys())
        
        #Fetch all of the results
        results = results.fetchall()
        
        results_dict = [{k:v for k,v in zip(columns,data)} for data in results]
    
    #Otherwise raise an exception
    except Exception as error:
        results = None
        raise Exception('Failed to connect to database and/or table object. {}'.format(error))
        
    return results_dict