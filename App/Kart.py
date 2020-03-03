from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from App.auth import login_required
from App.db import get_db

bp = Blueprint('kart', __name__,url_prefix='/kart')

@bp.route('/index')
@login_required
def index():
    db = get_db()

    kart_items = db.execute(
        'SELECT kart.user_id,kart.id,Products.name, Products.price, Products.description, Products.image, Products.id FROM products JOIN kart ON Products.id = Kart.product_id'
        


    ).fetchall()

    return render_template('kart/index.html', kart_items=kart_items)



@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        product_id = request.form['product_id']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO kart (user_id, product_id)'
                ' VALUES (?, ?)',
                (g.user['user_id'], product_id)
            )
            
            db.commit()
            return redirect(url_for('kart.index'))

    return render_template('kart/create.html')



@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    
    db = get_db()
    db.execute('DELETE FROM kart WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('kart.index'))