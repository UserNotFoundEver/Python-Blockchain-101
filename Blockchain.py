"""let there be blockchain - experiments
note: work in progress
"""

blockchain = []
open_transactions = []
owner = 'Satoshi'


# [-1] index to get the last value in the blockchain/list
def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    pass


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction ')
    tx_amount = float(input('Your transaction amount please '))
    # tx_sender = input('Enter the sender of the transaction')
    user_input = float(input('Your transaction amount: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your choice ')
    return user_input


def print_blockchain_elements():
    #  Output blockchain list
    for block in blockchain:
        print('Output Block')
        print(block)
    else:
        print('-' * 20)


# Get first transaction input
tx_amount = get_transaction_value()
add_transaction(tx_amount)


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):

        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    #     block_index += 1
    return is_valid


waiting_for_input = True

# Add as many blocks as you want
while waiting_for_input:
    print('Please choose ')
    print('1: Add a new transaction value ')
    print('2: Output the blockchain blocks ')
    print('h: Manipulate the chain ')
    print('q: Quit ')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add transaction amount to blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain_elements()
        # Make sure no one hacks the blockchain if its empty
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] == [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
else:
    print('User left.')

print('Done!!')
