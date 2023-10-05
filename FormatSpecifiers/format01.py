# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format
price01 = 3233.14159
price02 = -9387.65
price03 = 1332.34
print( f"Price 1  : ${price01:+,.2f}" )
print( f"Price 2  : ${price02:+,.2f}" )
print( f"Price 3  : ${price03:+,.2f}" )