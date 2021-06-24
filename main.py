from source.function import Function


if __name__ == "__main__":
    function = Function()
    err = function.start("raiz(25;-4+2*(-5+8))+summa(x;x;1;5)")

    if err is not None:
        print("Incompleto => {}".format(err))
    else:
        value = function.f()
        print("{}".format(value))
