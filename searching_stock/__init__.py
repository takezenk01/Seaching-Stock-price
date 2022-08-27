from flask import Flask
app = Flask(__name__, static_folder='images')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
import searching_stock.main

""" from searching_stock import db
db.create_books_table() """