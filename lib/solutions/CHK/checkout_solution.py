
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    if len(skus) == 0:
        return 0
    
    if not skus.isalpha() or not skus.isupper():
        return -1

    
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

    basketCount = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    for sku in skus:
        if sku in prices:
            basketCount[sku] += 1

    totalPrice = 0

    # deal with if the customer has bought two 'E's

    # check if we can apply special offer E
    if basketCount["E"] >= 2:

        EFrequency = basketCount["E"]

        freeBs = EFrequency // 2

        print(freeBs)
        while freeBs > 0:
        # check if we should apply special offer E
            Bfrequency = basketCount["B"]
        
            # we only want to apply special offer E if we are not a multiple of 2 for B
            # i.e. B would not be getting it's offer
            # if the frequency of B is 0 already that is fine
            if Bfrequency != 0 and (Bfrequency % 2 != 0 or freeBs > 1):
                print("deleting")
                basketCount["B"] -= 1
            
            freeBs -= 1



    for key in basketCount.keys():
        itemFreqBasket = basketCount[key]

        if key == "A" and (itemFreqBasket // 5) > 0:
            divisible = itemFreqBasket // 5
            remainder = itemFreqBasket % 5
            
            # deal with if the remainder is >= 3
            if (remainder // 3) > 0:
                divisibleBy3 = remainder // 3
                remainderAfter3 = remainder % 3
            
                total = (divisibleBy3 * 130) + remainderAfter3 * prices[key]
                totalPrice += total

            total = (divisible * 200) + remainder * prices[key]
            totalPrice += total
            continue

        elif key == "A" and (itemFreqBasket // 3) > 0:
            divisible = itemFreqBasket // 3
            remainder = itemFreqBasket % 3
        
            total = (divisible * 130) + remainder * prices[key]
            totalPrice += total
            continue
        
        
        if key == "B" and (itemFreqBasket // 2) > 0:
            # if the user has ordered at least 2 items  
            divisible = itemFreqBasket // 2

            remainder = itemFreqBasket % 2

            total = (divisible * 45) + remainder * prices[key]
            totalPrice += total
            continue
        
        totalPrice += (prices[key] * itemFreqBasket)

    
    return totalPrice

    
    








