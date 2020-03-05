from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from App.auth import login_required
from App.db import get_db

bp = Blueprint('products', __name__)

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method != 'POST':
        db = get_db()
        products = db.execute(
            'SELECT * FROM products'
        ).fetchall()
        return render_template('products/index.html', products=products)
    else:
        # print(request.form['product_id'])
        try:
            logged_in_user_id = g.user['user_id']
        except:
            logged_in_user_id = 1
        db = get_db()
        db.execute(
            'INSERT INTO Cart (user_id, product_id)'
            ' VALUES (?, ?)',
            (logged_in_user_id, request.form['product_id'])
        )
        db.commit()
        return redirect(url_for('products.index'))
