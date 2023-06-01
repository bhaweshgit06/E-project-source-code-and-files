from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
from trending_items import best_products
import product_detail
import recommender
app = Flask(__name__)

@app.route('/')
def home():
   ht,hk,g = best_products()
   return render_template('index.html', ht=ht,hk=hk,g=g)

@app.route('/grocery')
def browse_grocery():
   from grocery_items import grocery_itmes
   grocery_df = grocery_itmes()
   return render_template('grocery.html', grocery_df = grocery_df )

@app.route('/homekitchen')
def browse_hk():
   from home_kitchen import home_kitchen
   hk = home_kitchen()
   return render_template('home_kitchen.html', hk = hk )

@app.route('/hometools')
def browse_ht():
   from home_tools import home_tools
   ht = home_tools()
   return render_template('home_tools.html', ht = ht )

@app.route('/about')
def about_page():
   return render_template('about.html')

@app.route('/buyproduct')
def product_page():
   args = request.args
   cat = args['cat']
   asin = args['asin']
   price = args['p']
   rc = args['rc']
   ravg = args['ravg']
   if cat == 'ht':
      record = product_detail.product_detail_ht(asin)
      recommends = recommender.recommender_ht(asin)
   elif cat == 'hk':
      record = product_detail.product_detail_hk(asin)
      recommends = recommender.recommender_hk(asin)
   elif cat == 'g':
      record = product_detail.product_detail_g(asin)
      recommends = recommender.recommender_g(asin)
   return render_template('Buy_product.html', record = record, price=price,
   rc= rc, ravg=ravg, recommends=recommends)  



if __name__ == '__main__':
   app.run(debug=True)