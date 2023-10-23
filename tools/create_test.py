def create_test(result):
    import hashlib
    import pandas as pd
    print("import hashlib")
    if isinstance(result, pd.DataFrame):
        print(f"""assert isinstance(result, pd.DataFrame), "Invalid type"  """)
        print(f"""assert result.shape == ({result.shape[0]}, {result.shape[1]}), "Invalid shape"  """)
    elif isinstance(result, pd.Series):
        print(f"""assert isinstance(result, pd.Series), "Invalid type"  """)
        print(f"""assert len(result) == ({len(result)}), "Invalid type"  """)
    else:
        typ = type(result)
        print(f"""assert isinstance(result, {typ}), "Invalid type"  """)
    
    hash = hashlib.sha256(str(result).encode('utf-8')).hexdigest()
    print(f"""assert hashlib.sha256(str(result).encode('utf-8')).hexdigest() == '{hash}', "Invalid result" """)
    


