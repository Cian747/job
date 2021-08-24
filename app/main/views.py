from flask import render_template,request,redirect,url_for,abort
from ..models import Review,User
from app import db,photos
from . import main
from flask_login import login_required,current_user
import markdown2 