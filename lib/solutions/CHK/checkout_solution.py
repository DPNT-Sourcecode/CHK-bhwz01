
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    if len(skus) == 0:
        return 0
    
    if not skus.isalpha() or not skus.isupper():
        return -1

    
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}

    basketCount = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

    for sku in skus:
        if sku in prices:
            basketCount[sku] += 1

    totalPrice = 0

    # deal with if the customer has bought two 'E's

    # check if we can apply special offer E
    if basketCount["E"] >= 2:

        EFrequency = basketCount["E"]

        freeBs = EFrequency // 2

        while freeBs > 0:
        # check if we should apply special offer E
            Bfrequency = basketCount["B"]
        
            # we only want to apply special offer E if we haven't reached a frequency of 0 for B
            # if the frequency of B is 0 already that is fine
            # and (Bfrequency % 2 != 0 or freeBs > 1)
            if Bfrequency != 0:
                print("deleting")
                basketCount["B"] -= 1
            
            freeBs -= 1


    for key in basketCount.keys():
        itemFreqBasket = basketCount[key]

        if key == "A" and (itemFreqBasket // 5) > 0:
            divisible = itemFreqBasket // 5
            remainder = itemFreqBasket % 5
            total = 0
            # deal with if the remainder is >= 3
            if (remainder // 3) > 0:
                divisibleBy3 = remainder // 3
                remainderAfter3 = remainder % 3
            
                total = (divisibleBy3 * 130) + remainderAfter3 * prices[key]
                totalPrice += total
            else:
                # case where remainder isnt >= 3
                totalPrice += remainder * prices[key]


            total = (divisible * 200) 
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


        if key == "F" and (itemFreqBasket // 3) > 0:
            # if the user has order a multiple 3 items of type F
            divisible = itemFreqBasket // 2
            print(divisible)
            itemFreqBasket -= divisible

        
        totalPrice += (prices[key] * itemFreqBasket)

    
    return totalPrice

    
    



