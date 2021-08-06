import pandas as pd
import numpy as np

print('TASK 1:\n')
authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']}, columns=['author_id', 'author_name'])
print(authors)
print('\n')
books = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                      'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой',
                                     'Гроза', 'Таланты и поклонники'],
                      'price': [450, 300, 350, 500, 450, 370, 290]},
                     columns=['author_id', 'book_title', 'price'])

print(books)

print('\nTASK 2:\n')
authors_price = pd.merge(authors, books, on='author_id', how='outer')
print(authors_price)

print('\nTASK 3:\n')
top5 = authors_price.nlargest(5, 'price')
print(top5)
print('\nTASK 4:\n')
df_1 = authors_price.groupby('author_name').agg({'price': 'min'}).rename(columns={'price': 'min_price'})
df_2 = authors_price.groupby('author_name').agg({'price': 'max'}).rename(columns={'price': 'max_price'})
df_3 = authors_price.groupby('author_name').agg({'price': 'mean'}).rename(columns={'price': 'mean_price'})

authors_stat = pd.concat([df_1, df_2, df_3], axis=1)
print(authors_stat)

print('\nTASK 5:\n')
covers = pd.DataFrame({'cover': ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']},
                      columns=['cover'])
authors_price = pd.concat([authors_price, covers], axis=1)
print(authors_price)
print('\n')
book_info = pd.pivot_table(authors_price, values='price', index=['author_name'],
                           columns=['cover'], aggfunc=np.sum, fill_value=0)

print(book_info)
print('\n')
book_info.to_pickle('book_info.pkl')
book_info2 = pd.read_pickle('book_info.pkl')
print(book_info == book_info2)
