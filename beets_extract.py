# coding: utf-8

import os

import sqlite3

import yaml

OUTPUT = "./data/music.db"


def libraryfile():
    with open(os.path.expanduser("~/.config/beets/config.yaml")) as fobj:
        beets = yaml.load(fobj)
    return os.path.expanduser(beets["library"])


def extract_data(fname):
    """extract specific data
    """
    with sqlite3.connect(fname) as cnx:
        cu = cnx.cursor()
        q = """SELECT
         id
        ,albumartist AS artist
        ,album
        ,genre
        ,year
        ,label
        FROM albums
        WHERE album <> ''
        """
        cu.execute(q)
        return cu.fetchall()


def insert(fname, data):
    """Insert some data into a sqlite db file
    """
    create = """CREATE TABLE albums
     (id integer,
      artist varchar(80),
      album varchar(255),
      genre varchar(30),
      year integer,
      label varchar(80)
     )
    """
    insert = """INSERT INTO albums VALUES
    (?,?,?,?,?,?)
    """
    with sqlite3.connect(fname) as cnx:
        cu = cnx.cursor()
        cu.execute(create)
        cnx.commit()
        cu.executemany(insert, data)
        cnx.commit()


if __name__ == '__main__':
    data = extract_data(libraryfile())
    insert(OUTPUT, data)
    print("See generated file '{}".format(OUTPUT))
