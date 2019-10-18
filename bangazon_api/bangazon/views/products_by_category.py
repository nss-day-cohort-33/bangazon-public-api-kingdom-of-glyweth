import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Product
from ..models import Product_Category
from ..connection import Connection

def products_by_category(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                p.id,
                p.name,
                p.price,
                p.description,
                c.name as category_name
            from bangazon_product p
            join bangazon_product_category c
            on c.id = p.product_category_id
            group by p.name
            """)

            all_products = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                product = Product()
                product.id = row["id"]
                product.name = row["name"]
                product.price = row["price"]
                product.description = row["description"]
                product.category_name = row["category_name"]

                all_products.append(product)

        return render(request, template_name, context)