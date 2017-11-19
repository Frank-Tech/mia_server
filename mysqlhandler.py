from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData, Column, Integer, DateTime, Index, String, DECIMAL

from config import Config


class MySqlHandler:
    def __init__(self):
        pass

    server = create_engine(Config.MYSQL_SERVER, echo=False, convert_unicode=True)

    @staticmethod
    def users():
        table_name = "users"
        try:
            table = Table(table_name, MetaData(bind=MySqlHandler.server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlHandler.server),
                          Column("id", Integer, primary_key=True),
                          Column("date_created", DateTime(timezone=False), nullable=False,
                                 default=datetime.utcnow()),
                          Column("mid", String(255), nullable=True),
                          Column("name", String(255), nullable=True),
                          Column("email", String(255), nullable=True),
                          Column("gender", String(50), nullable=True),
                          Column("birth_day", DateTime(timezone=False), nullable=True),
                          mysql_engine="InnoDB")
            table.create()
            Index("mid_idx", table.c.mid, unique=False)
        return table

    @staticmethod
    def locations():
        table_name = "users_location"
        try:
            table = Table(table_name, MetaData(bind=MySqlHandler.server), autoload=True)
        except Exception:
            table = Table(table_name, MetaData(bind=MySqlHandler.server),
                          Column("id", Integer, primary_key=True),
                          Column("date_created", DateTime(timezone=False), nullable=False,
                                 default=datetime.utcnow()),
                          Column("date_updated", DateTime(timezone=False), nullable=False,
                                 default=datetime.utcnow()),
                          Column("user_id", Integer, nullable=False),
                          Column("longitude", DECIMAL(11, 8), nullable=True),
                          Column("latitude", DECIMAL(10, 8), nullable=True),
                          mysql_engine="InnoDB")
            table.create(checkfirst=True)
            Index("user_idx", table.c.user_id, unique=False)
        return table
