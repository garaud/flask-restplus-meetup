# coding: utf-8

"""Simple Flask REST API with the FlaskRESTplus extension.
Handle you data music collection imported from beets - http://beets.io/
"""

import logging
import os.path as osp

import sqlite3

from flask import Flask
from flask.ext.restplus import Api, Resource, fields


_here = osp.dirname(osp.abspath(__file__))
DBFILE = osp.join("data", "music.db")

LOG_FORMAT = "%(asctime)s :: %(levelname)s :: %(module)s :: %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
Logger = logging.getLogger(__name__)


app = Flask(__name__)
api = Api(app, title="Music Collection",
          version='0.1',
          description="Retrieve data from your music collection")

MODEL = api.model("CD", {"artist": fields.String,
                         "album": fields.String,
                         "year": fields.Integer,
                         "genre": fields.String,
                         "label": fields.String})


def _query(q, *params):
    with sqlite3.connect(DBFILE) as cnx:
        cu = cnx.cursor()
        cu.execute(q, params)
        columns = [x[0] for x in cu.description]
        return [dict(zip(columns, x)) for x in cu.fetchall()]


def search_artist(name, limit=None):
    """Look for a specific artist in the music collection
    """
    q = """SELECT *
    FROM albums
    WHERE artist LIKE ?
    ORDER BY year
    """
    if limit is not None:
        q += " LIMIT %d" % limit
    return _query(q, name)


@api.route("/album/<album_id>")
class Album(Resource):
    @api.marshal_with(MODEL)
    def get(self, album_id):
        Logger.info("album id: %s", album_id)
        album = _query("SELECT * FROM albums WHERE id=?", album_id)
        if not album:
            api.abort(404, "Album id '{}' not found".format(album_id))
        return album[0]


search_parser = api.parser()
search_parser.add_argument("q", required=True, dest='q', location='args',
                           help='Query')
search_parser.add_argument("limit", default=10, type=int, required=False,
                           dest='limit', location='args', help='Query')


@api.route("/artist")
class SearchAritst(Resource):
    @api.doc(parser=search_parser,
             description="search album from an artist")
    @api.marshal_with(MODEL)
    def get(self):
        args = search_parser.parse_args()
        name = args['q']
        Logger.info("Look for '%s'", name)
        reslimit = args["limit"]
        return search_artist(name, reslimit)


if __name__ == '__main__':
    app.run(debug=True)
