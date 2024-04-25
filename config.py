from dotenv import load_dotenv
import os

load_dotenv() #Lectura de las variables entorno .env

user = os.environ['USER']
password = os.environ['PASSWORD']
host = os.environ['HOST']
database = os.environ['DATABASE']
server = os.environ['SERVER']

DATABASE_CONNECTION = f'{server}://{user}:{password}@{host}/{database}'