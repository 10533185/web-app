from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from App.auth import login_required
from App.db import get_db

bp = Blueprint('Cart', __name__,url_prefix='/Cart')

# Display all items in the cart
@bp.route('/index')
@login_required
def index():
    db = get_db()

    Cart_items = db.execute(
        'SELECT Cart.user_id,Cart.id,Products.name, Products.price, Products.description, Products.image, Products.id FROM products JOIN Cart ON Products.id = Cart.product_id'
        


    ).fetchall()

    return render_template('Cart/index.html', Cart_items=Cart_items)


# For adding items into the cart
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
                'INSERT INTO Cart (user_id, product_id)'
                ' VALUES (?, ?)',
                (g.user['user_id'], product_id)
            )
            
            db.commit()
            return redirect(url_for('Cart.index'))

    return render_template('Cart/create.html')


# Remove the items added in the cart
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    
    db = get_db()
    db.execute('DELETE FROM Cart WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('Cart.index'))