for i in dir(dict):
    if(not i.startswith('_') or not i.endswith('_')):
        print(i)