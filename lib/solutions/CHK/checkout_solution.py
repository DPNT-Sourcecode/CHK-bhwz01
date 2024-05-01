
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}

    basketCount = {"A": 0, "B": 0, "C": 0, "D": 0}

    for sku in skus:
        if sku in prices:
            basketCount[sku] += 1

    totalPrice = 0

    for key in basketCount.keys():
        itemFreqBasket = basketCount[key]

        if key == "A" and (itemFreqBasket // 3) > 0:
            divisible = itemFreqBasket // 3
            remainder = itemFreqBasket - divisible

            total = (divisible * 130) + remainder * prices[key]
            totalPrice += total
            continue
        
        if key == "B" and (itemFreqBasket // 2) > 0:
            # if the user has ordered at least 2 items  
            divisible = itemFreqBasket // 2
            remainder = itemFreqBasket - divisible

            total = (divisible * 45) + remainder * prices[key]
            totalPrice += total
            continue
        
        totalPrice += (prices[key] * itemFreqBasket)

    
    return totalPrice

    
    



