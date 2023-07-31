# error handling

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print("Hatalı bilgi")
#     print(e)

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as e:
        print("Hatalı bilgi")
        print(e)
    else:
        break
    # finally:
    #     print("try except sonlandı")