"""Exercise #18: Buy 8 Get 1 Free

Write a function named `getCostOfCoffee()` that has a parameters named
`numberOfCoffees` and `pricePerCoffee`. 

Given this information, the function returns the total cost of the
coffee order. This is not a simple multiplication of cost and quantity,
however, because the coffee shop has an offer where you get one free
coffee for every eight coffees you buy.

For example, buying eight coffees for $2.50 each costs $20 (or 8 x 2.5).
But buying nine coffees also costs $20, since the first eight makes the
ninth coffee free.

Buying ten coffees calculates as follows:
$20 for the first eight coffees, a free ninth coffee, and $2.50 for the
tenth coffee for a total of $22.50.
"""

def getCostOfCoffee(numberOfCoffees: int, pricePerCoffee: float) -> float:
    """Calculate the total cost of coffees.
    
    Every 9th coffee is free and does not add to the total costs.
    """
    return 0
