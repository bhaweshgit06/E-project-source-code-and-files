import pickle
import numpy as np

def recommender_g(item_name):
    try:
        best_products  = pickle.load(open('best_products_g.pkl', 'rb'))
        pivottable = pickle.load(open('pivottable_g.pkl', 'rb'))
        cosine_dist = pickle.load(open('cosine_dist_g.pkl', 'rb'))
        index = np.where(pivottable.index==item_name)[0][0]
        similar = list(enumerate(cosine_dist[index]))
        similar.sort(key=lambda a:a[1], reverse=True)
        data=[]
        for i in similar[1:20]:
            item=[]
            temp_df=best_products[best_products['asin']==pivottable.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('title')['asin'].values))
            k=list(temp_df.drop_duplicates('title')['rating-avg'].values)
            k = [round(i,1) for i in k]
            item.extend(k)
            item.extend(list(temp_df.drop_duplicates('title')['rating-count'].values))
            item.extend(list(temp_df.drop_duplicates('title')['title'].values))
            item.extend(list(temp_df.drop_duplicates('title')['price'].values))
            item.extend(list(temp_df.drop_duplicates('title')['imageURLHighRes'].values))
            data.append(item)


        data = [x for x in data if x]
    except:
        data = None
        return data
    return data[:5]

def recommender_ht(item_name):
    try:
        best_products  = pickle.load(open('best_products_ht.pkl', 'rb'))
        pivottable = pickle.load(open('pivottable_ht.pkl', 'rb'))
        cosine_dist = pickle.load(open('cosine_dist_ht.pkl', 'rb'))
        index = np.where(pivottable.index==item_name)[0][0]
        similar = list(enumerate(cosine_dist[index]))
        similar.sort(key=lambda a:a[1], reverse=True)
        data=[]
        for i in similar[1:20]:
            item=[]
            temp_df=best_products[best_products['asin']==pivottable.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('title')['asin'].values))
            k=list(temp_df.drop_duplicates('title')['rating-avg'].values)
            k = [round(i,1) for i in k]
            item.extend(k)
            item.extend(list(temp_df.drop_duplicates('title')['rating-count'].values))
            item.extend(list(temp_df.drop_duplicates('title')['title'].values))
            item.extend(list(temp_df.drop_duplicates('title')['price'].values))
            item.extend(list(temp_df.drop_duplicates('title')['imageURLHighRes'].values))
            data.append(item)


        data = [x for x in data if x]
    except:
        data = None
        return data
    return data[:5]

def recommender_hk(item_name):
    try:
        best_products  = pickle.load(open('best_products_hk.pkl', 'rb'))
        pivottable = pickle.load(open('pivottable_hk.pkl', 'rb'))
        cosine_dist = pickle.load(open('cosine_dist_hk.pkl', 'rb'))
        index = np.where(pivottable.index==item_name)[0][0]
        similar = list(enumerate(cosine_dist[index]))
        similar.sort(key=lambda a:a[1], reverse=True)
        data=[]
        for i in similar[1:20]:
            item=[]
            temp_df=best_products[best_products['asin']==pivottable.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('title')['asin'].values))
            k=list(temp_df.drop_duplicates('title')['rating-avg'].values)
            k = [round(i,1) for i in k]
            item.extend(k)
            item.extend(list(temp_df.drop_duplicates('title')['rating-count'].values))
            item.extend(list(temp_df.drop_duplicates('title')['title'].values))
            item.extend(list(temp_df.drop_duplicates('title')['price'].values))
            item.extend(list(temp_df.drop_duplicates('title')['imageURLHighRes'].values))
            data.append(item)


        data = [x for x in data if x]
    except:
        data = None
        return data
    return data[:5]