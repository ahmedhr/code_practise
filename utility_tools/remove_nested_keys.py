def recursive_remove_keys(data, remove_keys):
    if isinstance(data, dict):
        #pay heed to the list type casting of keys
        #if removing keys from a dictionary while a loop is iterating can cause
        #RuntimeError: dictionary changed size during iteration
        for data_key in list(data.keys()):
            if data_key in remove_keys:
                del data[data_key]
            else:
                recursive_remove_keys(data[data_key], remove_keys)