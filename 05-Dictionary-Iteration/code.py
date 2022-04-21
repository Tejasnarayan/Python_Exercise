ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

rev_dict = {v: k for k, v in ascii_dict.items()}
print(str(rev_dict))