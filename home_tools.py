import pickle

popular_df  = pickle.load(open('best_products_ht.pkl', 'rb'))
popular_df = popular_df.drop_duplicates('title')

item_name = list(popular_df['title'].values)[1::3]
item_img = list(popular_df['imageURLHighRes'].values)[1::3]
brand = list(popular_df['brand'].values)[1::3]
asin = list(popular_df['asin'].values)[1::3]
price = list(popular_df['price'].values)[1::3]
for i in range(price.__len__()):
    if price[i].startswith('$') and '-' not in price[i]:
        price[i] = round(float(price[i].replace("$", ""))*80)
        # print(price[i])
    else:
        price[i] = 800
ratng_avg = list(popular_df['rating-avg'].values)[1::3]
for i in range(ratng_avg.__len__()):
    ratng_avg[i] = round(float(ratng_avg[i]),1)
ratng_count = list(popular_df['rating-count'].values)[1::3]
main_cat = list(popular_df['main_cat'].values)[1::3]

ht = (item_name,item_img,brand,asin,price,ratng_avg,ratng_count,
main_cat)

def home_tools():
    return ht