import json

import datetime
from flask import request
from sqlalchemy import select
from sqlalchemy import text

from mysqlhandler import MySqlHandler


class QueryHandler:
    def __init__(self):
        self._request = request.args
        pass

    def new_user(self):
        try:
            data = self._request.get("d", "")
            json_data = json.loads(data)

            row = {
                "date_created": datetime.datetime.now(),
                "mid": json_data["mid"],
                "email": json_data["email"],
                "name": json_data["name"],
                "gender": json_data["gender"],
                "birth_day": json_data["birth_day"],
            }

            users_table = MySqlHandler.users()

            existing_user = select([users_table.c.id, users_table.c.email]) \
                .where(users_table.c.email == row["email"]) \
                .execute().first()

            if existing_user is None:
                users_table.insert().values(row).execute()

            print json_data

        except Exception, e:
            print e
        return "OK"

    def location_update(self):
        try:
            longitude = self._request.get("lo", "")
            latitude = self._request.get("la", "")
            user_id = self._request.get("uid", "")

            location = {
                "date_created": datetime.datetime.now(),
                "date_updated": datetime.datetime.now(),
                "user_id": user_id,
                "longitude": longitude,
                "latitude": latitude,
            }

            locations_table = MySqlHandler.locations()
            users_table = MySqlHandler.users()

            existing_user = select([users_table.c.id]) \
                .where(users_table.c.id == location["user_id"]) \
                .execute().first()

            if existing_user is not None:

                existing_location = select([locations_table.c.user_id]) \
                    .where(locations_table.c.user_id == existing_user[0]) \
                    .execute().first()

                if existing_location is None:
                    locations_table.insert().values(location).execute()
                else:
                    updated_location = {
                        "date_updated": datetime.datetime.now(),
                        "longitude": longitude,
                        "latitude": latitude,
                    }

                    locations_table.update().where(locations_table.c.user_id == existing_user[0]) \
                        .values(updated_location).execute()

        except Exception, e:
            print e
        return "OK"

    def locations_get(self):
        try:
            user_id = self._request.get("uid", "")

            locations_table = MySqlHandler.locations()
            users_table = MySqlHandler.users()

            existing_user = select([users_table.c.id]) \
                .where(users_table.c.id == user_id) \
                .execute().first()

            if existing_user is not None:

                current_location = select([locations_table.c.longitude,
                                           locations_table.c.latitude]) \
                    .where(locations_table.c.user_id == user_id) \
                    .execute().first()

                query = ("SELECT *, ( ( ( Acos(Sin(( {0} * Pi() / 180 )) * Sin(( `latitude` * Pi() / 180 ))+ Cos (( {0} * Pi() / 180 )) * Cos(( `latitude` * Pi() / 180 )) * Cos(( ( {1} - `longitude` ) * Pi() / 180 ))) ) * 180 / Pi ()) * 60 * 1.1515 * 1.609344 * 1000 ) AS METERS FROM users_location HAVING  METERS <= 100")\
                    .format(current_location[1], current_location[0])

                sql = text(query)
                result = MySqlHandler.server.execute(sql)
                names = []
                for row in result:
                    names.append(row[0])

                print names

        except Exception, e:
            print e
        return "OK"
