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



# Remove the items added in the cart
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    
    db = get_db()
    db.execute('DELETE FROM Cart WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('Cart.index'))