from solution_9_1 import *
import pandas as pd

vrfy = {
    'NumberOfInvoices': 66,
    'TotalAmount': 24506,
    'NumberOfCancelledInvoices': 4,
    'CancelledAmount': -199,
    'NumberWithoutCustomer': 1,
    'NoCustomerAmount': 0
}


def test_9_1():
    # assert True, "No Test"
    df = pd.read_excel('/data/IFI8410/online_retail/online_retail.xlsx', nrows=1000)
    res = analyse_invoices(df)
    for k in vrfy.keys():
        assert vrfy[k] == res[k], f"Error in `k`"
    
