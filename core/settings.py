import databases
import sqlalchemy

from decouple import config

DEBUG = config("DEBUG", False, cast=bool)

############
# Database #
############

DATABASE_URL = config("DATABASE_URL")

database = databases.Database(DATABASE_URL)
db_engine = sqlalchemy.create_engine(DATABASE_URL)

############
# RabbitMQ #
############

RABBITMQ_URL = config("RABBITMQ_URL")
RABBITMQ_IMPORT_ASTRONAUTS_QUEUE = "astronauts"
