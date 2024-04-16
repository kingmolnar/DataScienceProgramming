from solution_9_2 import *

def test_9_2():
    df = pd.read_excel('/data/IFI8410/online_retail/online_retail.xlsx', nrows=1000)
    spening_df = customer_spending(df)
    last_value = 9999999999999999999
    for j, cid in enumerate([16029, 16210, 17511, 17850, 13408]):
        assert spening_df.iloc[j].CustomerID == cid, "Incorrect CustomerID"
        assert spening_df.iloc[j].TotalSpent <= last_value, "Incorrect order"
        last_value = spening_df.iloc[j].TotalSpent
