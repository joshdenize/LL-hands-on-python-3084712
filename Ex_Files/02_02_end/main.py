greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"
name2 = "John2"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name2)

print(intrupution, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Paul"))
