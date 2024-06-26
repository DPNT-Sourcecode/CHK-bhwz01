import heapq

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    if len(skus) == 0:
        return 0
    
    if not skus.isalpha() or not skus.isupper():
        return -1

    
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
              "G": 20, "H": 10, "I": 35, "J": 60, "K": 70, "L": 90, 
              "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
              "S": 20, "T": 20, "U": 40, "V": 50, "W": 20, "X": 17,
              "Y": 20, "Z": 21}

    basketCount = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0,
                "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, 
                "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0,
                "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
                "Y": 0, "Z": 0}
    

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
                basketCount["B"] -= 1
            
            freeBs -= 1


    if (basketCount["N"] // 3) > 0:
        # if the user has order a multiple 3 items of type N
        # 3N get one M free
        # number of times the offer can be applied 
        nFrequency = basketCount["N"]
        offer_count = nFrequency // 3

        while offer_count > 0 and basketCount["M"] > 0:
            basketCount["M"] -= 1
            offer_count -= 1
    
    if (basketCount["R"] // 3) > 0:
        # if the user has order a multiple 3 items of type R
        # 3R get one Q free
        # number of times the offer can be applied 
        rFrequency = basketCount["R"]
        offer_count = rFrequency // 3

        while offer_count > 0 and basketCount["Q"] > 0:
            basketCount["Q"] -= 1
            offer_count -= 1

    
    groupItems = {"S", "T", "X", "Y", "Z"}

    # with groupset we want to get rid of the most expensive items (favour the customer)
    # so let's make a max heap containing all items in this group offer,  we will use the
    # price as the value which maintains order

    maxHeap = []
    heapq.heapify(maxHeap)

    # push all items from the user's basket which in this group offer, onto the heap
    for item in groupItems:
        if basketCount[item] > 0:
            itemFreq = basketCount[item]
            for i in range(itemFreq):
                print("Here")
                # max-heap in python, so we negate values
                heapq.heappush(maxHeap, (-1 * prices[item], item))
    
    while len(maxHeap) >= 3:
        
        itemsInGroup = []
        for _ in range(3):
            item = heapq.heappop(maxHeap)[1]
            itemsInGroup.append(item)

        for item in itemsInGroup:
            basketCount[item] -= 1
        
        totalPrice += 45


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
            
            # number of times the offer can be applied 
            offer_count = itemFreqBasket // 3

            itemFreqBasket -= offer_count

        if key == "H" and (itemFreqBasket // 10) > 0:
            divisible = itemFreqBasket // 10
            remainder = itemFreqBasket % 10
            total = 0
            # deal with if the remainder is >= 5
            if (remainder // 5) > 0:
                divisibleBy5 = remainder // 5
                remainderAfter5 = remainder % 5
            
                total = (divisibleBy5 * 45) + remainderAfter5 * prices[key]
                totalPrice += total
            else:
                # case where remainder isnt >= 5
                totalPrice += remainder * prices[key]

            total = (divisible * 80) 
            totalPrice += total
            continue
        elif key == "H" and (itemFreqBasket // 5) > 0:
            divisible = itemFreqBasket // 5
            remainder = itemFreqBasket % 5
        
            total = (divisible * 45) + remainder * prices[key]
            totalPrice += total
            continue

        if key == "K" and (itemFreqBasket // 2) > 0:
            # if the user has ordered at least 2 items  
            divisible = itemFreqBasket // 2

            remainder = itemFreqBasket % 2

            total = (divisible * 120) + remainder * prices[key]
            totalPrice += total
            continue

        if key == "P" and (itemFreqBasket // 5) > 0:
            # if the user has ordered at least 5 items  
            divisible = itemFreqBasket // 5

            remainder = itemFreqBasket % 5

            total = (divisible * 200) + remainder * prices[key]
            totalPrice += total
            continue

        if key == "Q" and (itemFreqBasket // 3) > 0:
            # if the user has ordered at least 3 items  
            divisible = itemFreqBasket // 3

            remainder = itemFreqBasket % 3

            total = (divisible * 80) + remainder * prices[key]
            totalPrice += total
            continue
        
        if key == "U" and (itemFreqBasket // 4) > 0:
            # if the user has order a multiple 4 items of type U
            # 3U get one U free
            # number of times the offer can be applied 
            offer_count = itemFreqBasket // 4

            itemFreqBasket -= offer_count
        
        if key == "V" and (itemFreqBasket // 3) > 0:
            divisible = itemFreqBasket // 3
            remainder = itemFreqBasket % 3
            total = 0
            # deal with if the remainder is >= 2
            if (remainder // 2) > 0:
                divisibleBy2 = remainder // 2
                remainderAfter2 = remainder % 2
            
                total = (divisibleBy2 * 90) + remainderAfter2 * prices[key]
                totalPrice += total
            else:
                # case where remainder isnt >= 2
                totalPrice += remainder * prices[key]

            total = (divisible * 130) 
            totalPrice += total
            continue

        elif key == "V" and (itemFreqBasket // 2) > 0:
            divisible = itemFreqBasket // 2
            remainder = itemFreqBasket % 2
        
            total = (divisible * 90) + remainder * prices[key]
            totalPrice += total
            continue
        


        
        totalPrice += (prices[key] * itemFreqBasket)

    
    return totalPrice

    
    








