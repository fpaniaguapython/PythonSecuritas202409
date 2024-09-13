try:
    int('a')
except ValueError as ve:
    print(ve) #invalid literal for int() with base 10: 'a'
    print(ve.args) #("invalid literal for int() with base 10: 'a'",)


try:
    import abcdefghijklmn
except ImportError as ie:
    print(ie)#No module named 'abcdefghijklmn'
    print(ie.args)#("No module named 'abcdefghijklmn'",)
    print(ie.path)#None
    print(ie.msg)#No module named 'abcdefghijklmn'
    print(ie.name)#abcdefghijklmn
    print(ie.name_from)#None