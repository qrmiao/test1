import random
import time
from datetime import datetime

def get_ticket():

    base_str = 'qwertyuiopasdfghjklzxcvbnm'
    ticket = ''

    for i in range(20):

        ticket += random.choice(base_str)

    ticket = 'TK_' + str(int(time.time())) +ticket

    return ticket
def get_order():
    num = ''
    s ='asjdfkjwiqrqwekfklsjd'
    for i in range(10):
        num += random.choice(s)
    # oreder_time = datetime.now()
    return num