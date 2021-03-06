import pickle


def save_obj(obj, name):
    with open(f"{name}.pkl", 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    try:
        with open(f"{name}.pkl", 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None