def nfruits(basket,eatenFruits):
    '''
    Every fruit that is eaten adds another fruit to the remainded ones
    except for one that is eaten.
    We dont add any fruit at the last fruit eaten.
    input:  basket      -> dictionary, non-empty dictionary < 10
            eatenFruits -> string
    output: maximum quantity of any fruit in the basket
    '''
    basket[eatenFruits[0]] -=1
    #Fruit eaten
    assert len(basket)<10 and len(basket)>0,'Non-empty dictionary < 10 by definition'
    if len(eatenFruits) == 1:
        return max(basket.values())
    else:
        assert basket[eatenFruits[0]] > 0, 'There is not more ' + i + ' fruits, check your fruits eaten'
        for k in basket:
            if eatenFruits[0] != k:
                basket[k] +=1
                #Adding fruits
        return nfruits(basket,eatenFruits[1:])

basket = {'D': 8, 'H': 6, 'J': 5, 'Q': 9, 'U': 8, 'X': 5}
eatenFruits = 'DHHD'

print nfruits(basket,eatenFruits)