# TODO решить с помощью list comprehension и распечатать его
import pprint

numbers = [{'bin': bin(i), 'dec': i, 'oct': oct(i), 'hex': hex(i)} for i in range(16)]
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(numbers)