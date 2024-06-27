#!/usr/bin/env python3
"API's blueprint"
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.expenses import *
from api.v1.views.categories import *
