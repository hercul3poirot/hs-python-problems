def dis(price, discount):
    discountedprice = price - (price*(discount/100))
    return discountedprice

print(dis(89,20))