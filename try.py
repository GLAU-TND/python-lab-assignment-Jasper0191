try:
    a = 10
    a = a + "jasper"
    b = 'abcd'
    b = int(b)
    c = "jasper"
    c.rename()
except ValueError as e:
    print("ValueError",e)
except TypeError as e:
    print("TypeError",e)
except AttributeError as e:
    print("AttributeError",e)