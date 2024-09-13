try:
    print(int('a'))
except:
    print("Error 'indeterminado'")

try:
    print(int('a'))
except ValueError:
    print("ValueError")

try:
    print(int('a'))
except ValueError as ve:
    print("ValueError recogiendo objeto")
    print(ve)
    print(ve.args)