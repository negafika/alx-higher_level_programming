#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4.pyc
    all_dir = dir(hidden_4.pyc)
    asset = [x for x in all_dir if x[0:2] != '__']
    for each in asset:
        print(each)
