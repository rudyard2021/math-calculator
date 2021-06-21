from source.function import Function


if __name__ == "__main__":
    function = Function()
    err = function.start("raiz(25;-4+2*(-5+8))")

    if err is not None:
        print("Incompleto => {}".format(err))
    else:
        print("{}".format(function.variable.package))
        value = function.f({"x": 5})
        print("{}".format(value))
