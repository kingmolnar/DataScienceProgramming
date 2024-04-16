from solution_9_3 import rank_products_by_customer
import pandas as pd

vrfy = [('22961', 9), ('84879', 7), ('22632', 7), ('22960', 6), ('85123A', 6), ('22866', 6),
        ('22086', 6), ('21212', 6), ('22197', 6), ('22633', 6), ('22619', 6), ('22910', 5),
        ('22900', 5), ('22837', 5), ('22469', 5),  ('21977', 5), ('84029E', 5)]

def test_9_3():
    df = pd.read_excel('/data/IFI8410/online_retail/online_retail.xlsx', nrows=1000)
    flt3 = rank_products_by_customer(df, min_customer=5)
    for i, (j, r) in enumerate(flt3.iterrows()):
        assert vrfy[i][0] == str(r.StockCode), 'Invalid product'
        assert vrfy[i][1] ==  r.NumCustomer, 'Invalid number of customers'
        
