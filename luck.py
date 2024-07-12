import cassava

string_cassava = cassava.string_cassava
string_chips = cassava.string_chips
string_hello = str(cassava.float_number)
string_world = str(cassava.int_number)
string_python = cassava.string_cream

target = string_cassava + string_hello[-1] + string_chips[2:] + string_world[:2] + string_python[1:-1]

number = target.upper()
print(number)
