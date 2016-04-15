# coding: utf-8

from flask import Flask
from flask.ext.restplus import Api, Resource


app = Flask(__name__)
api = Api(app)


@api.route("/meetup")
class Meetup(Resource):
    def get(self):
        return {"content": "Hello Python Meetup!",
                "location": "Le Node Bordeaux",
                "date": "2016-05-10"}


if __name__ == '__main__':
    app.run(debug=True)
