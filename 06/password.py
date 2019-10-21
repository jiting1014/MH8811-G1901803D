import random
import string

def genPassword(l):
    num_num=random.randint(1,l-3)
    upletter_num=random.randint(1,l-2-num_num)
    lowletter_num=random.randint(1,l-1-num_num-upletter_num)
    symbol_num=l-upletter_num-num_num-lowletter_num
    num=[random.choice(string.digits) for i in range(num_num)]
    upletter=[random.choice(string.ascii_uppercase) for i in range(upletter_num)]
    lowletter=[random.choice(string.ascii_lowercase) for i in range(lowletter_num)]
    symbol=[random.choice(string.punctuation) for i in range(symbol_num)]
    pas_0=num+upletter+lowletter+symbol
    random.shuffle(pas_0)
    res=''
    for i in pas_0:
        res=res+str(i)
    return res

