import pickle
best_products_ht  = pickle.load(open('best_products_ht.pkl', 'rb'))
best_products_hk  = pickle.load(open('best_products_hk.pkl', 'rb'))
best_products_g  = pickle.load(open('best_products_g.pkl', 'rb'))

def product_detail_ht(item_name):
    df = best_products_ht[best_products_ht['asin']==item_name].to_dict(orient='index')
    k = ''
    for i in df:
        k = i
    t = df[k]
    return t

def product_detail_hk(item_name):
    df = best_products_hk[best_products_hk['asin']==item_name].to_dict(orient='index')
    k = ''
    for i in df:
        k = i
    t = df[k]
    t['rating_count'] = t['rating-count']
    t['rating_avg'] = round(float(t['rating-avg']),1)

    return t

def product_detail_g(item_name):
    df = best_products_g[best_products_g['asin']==item_name].to_dict(orient='index')
    k = ''
    for i in df:
        k = i
    t = df[k]
    return t