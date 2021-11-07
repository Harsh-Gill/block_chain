# initialize DB for Blockchain
# https://www.christopherlovell.co.uk/blog/2016/04/27/h5py-intro.html
import h5py
import numpy as np



# # To create new DB

# hf = h5py.File('database.h5', 'w')
# hf.create_dataset('block_chain_db', data=[], compression="gzip", chunks=True, maxshape=(None,))
# hf.close()

class transaction_data:
    def __init__(self,transaction):
        self.transaction = None
        self.verify_transaction_format(transaction)

    def verify_transaction_format(self,transaction):
        format = transaction.split('-')
        if len(format) == 3:
            self.transaction = transaction
        else:
            return "Transaction Format not correct"


def add_block_to_db(transaction):

    new_data = np.array([transaction])
    print("adding",new_data)
    print("datashape",new_data.shape[0])
    with h5py.File('/Users/hssingh/PycharmProjects/block_chain/db/database.h5', 'a') as hf:
        hf["block_chain_db"].resize((hf["block_chain_db"].shape[0] + new_data.shape[0]), axis = 0)
        hf["block_chain_db"][-new_data.shape[0]:] = new_data
    hf.close()

def view_db():
    hf = h5py.File('/Users/hssingh/PycharmProjects/block_chain/db/database.h5',
                   'r')
    print(hf.keys())
    np.set_printoptions(suppress=True,
                        formatter={'float_kind': '{:f}'.format})
    db = np.array(hf.get('block_chain_db'))

    return db
