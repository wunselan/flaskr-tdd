from flask import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, jsonify
import sqlite3

# Configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'my_precious'
USERNAME = 'admin'
PASSWORD = 'admin'


# Create and initialise app
app = Flask(__name__)
app.config.from_object(__name__)


if __name__ == '__main__':
    app.run()
