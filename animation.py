import time
import random 

def animation(word):
    '''
    function that do basic animation of loading 
    '''
    print(f"{word}",end='')
    num = random.randint(3,10)
    for _ in range(1,num+1):
        print('.',end='',flush=True)
        time.sleep(1)
