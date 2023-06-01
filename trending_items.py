import pickle
# import numpy as np

popular_df_ht  = pickle.load(open('best_products_ht.pkl', 'rb'))
popular_df_ht = popular_df_ht.drop_duplicates('title')

item_name_ht = list(popular_df_ht['title'].values)[:15:3]
# for i in range(item_name_ht.__len__()):
#     item_name_ht[i] = item_name_ht[:25]
item_img_ht = list(popular_df_ht['imageURLHighRes'].values)[:15:3]
brand_ht = list(popular_df_ht['brand'].values)[:15:3]
asin_ht = list(popular_df_ht['asin'].values)[:15:3]
price_ht = list(popular_df_ht['price'].values)[:15:3]
for i in range(price_ht.__len__()):
    if price_ht[i].startswith('$'):
        price_ht[i] = round(float(price_ht[i].replace("$", ""))*80)
    else:
        price_ht[i] = 800
ratng_avg_ht = list(popular_df_ht['rating-avg'].values)[:15:3]
for i in range(ratng_avg_ht.__len__()):
    ratng_avg_ht[i] = round(float(ratng_avg_ht[i]),1)
ratng_count_ht = list(popular_df_ht['rating-count'].values)[:15:3]
main_cat_ht = list(popular_df_ht['main_cat'].values)[:15:3]

ht = (item_name_ht,item_img_ht,brand_ht,asin_ht,price_ht,ratng_avg_ht,ratng_count_ht,
main_cat_ht)

popular_df_hk  = pickle.load(open('best_products_hk.pkl', 'rb'))
popular_df_hk = popular_df_hk.drop_duplicates('title')

item_name_hk = list(popular_df_hk['title'].values)[:15:3]
item_img_hk = list(popular_df_hk['imageURLHighRes'].values)[:15:3]
brand_hk = list(popular_df_hk['brand'].values)[:15:3]
asin_hk = list(popular_df_hk['asin'].values)[:15:3]
price_hk = list(popular_df_hk['price'].values)[:15:3]
for i in range(price_hk.__len__()):
    if price_hk[i].startswith('$'):
        price_hk[i] = round(float(price_hk[i].replace("$", ""))*80)
    else:
        price_hk[i] = 800
ratng_avg_hk = list(popular_df_hk['rating-avg'].values)[:15:3]
for i in range(ratng_avg_hk.__len__()):
    ratng_avg_hk[i] = round(float(ratng_avg_hk[i]),1)
ratng_count_hk = list(popular_df_hk['rating-count'].values)[:15:3]
main_cat_hk = list(popular_df_hk['main_cat'].values)[:15:3]

hk = (item_name_hk,item_img_hk,brand_hk,asin_hk,price_hk,ratng_avg_hk,ratng_count_hk,
main_cat_hk)

popular_df_g  = pickle.load(open('best_products_g.pkl', 'rb'))
popular_df_g = popular_df_g.drop_duplicates('title')

item_name_g = list(popular_df_g['title'].values)[:15:3]
item_img_g = list(popular_df_g['imageURLHighRes'].values)[:15:3]
brand_g = list(popular_df_g['brand'].values)[:15:3]
asin_g = list(popular_df_g['asin'].values)[:15:3]
price_g = list(popular_df_g['price'].values)[:15:3]
for i in range(price_g.__len__()):
    if price_g[i].startswith('$'):
        price_g[i] = round(float(price_g[i].replace("$", ""))*80)
    else:
        price_g[i] = 800
ratng_avg_g = list(popular_df_g['rating-avg'].values)[:15:3]
for i in range(ratng_avg_g.__len__()):
    ratng_avg_g[i] = round(float(ratng_avg_g[i]),1)
ratng_count_g = list(popular_df_g['rating-count'].values)[:15:3]
main_cat_g = list(popular_df_g['main_cat'].values)[:15:3]

g = (item_name_g,item_img_g,brand_g,asin_g,price_g,ratng_avg_g,ratng_count_g,
main_cat_g)

def best_products():
    return (ht,hk,g)

# def grocery_df():