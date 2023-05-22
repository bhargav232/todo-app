# Function decoupling
# Take feet and inch(usually person height) from the user and convert to meter and check child
# is able to use the slide or not!
from bonus.convert6 import convert
from bonus.parse6 import parse

result = parse()
m = convert(result['feet'], result['inch'])

print(f"The feet is {result['feet'] } and inch is { result['inch']}")
if m > 1:
    print('child, can you the slide')
else:
    print('Soory!, child can use ride')
