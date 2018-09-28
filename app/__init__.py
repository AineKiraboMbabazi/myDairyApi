from flask import Flask
app = Flask(__name__)
from app.fetch_entries import *
from app.fetch_single_entry import *
from app.create_entry import *
from app.modify_entry import *
