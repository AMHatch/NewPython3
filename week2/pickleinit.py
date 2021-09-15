import pickle
todos = {"high": [],
 "medium": [],
 "low": []}
with open('data.pickle', 'wb') as fh:            # wb = write as binary
    pickle.dump(todos, fh)