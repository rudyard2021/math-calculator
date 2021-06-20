from source.function import Function


if __name__ == "__main__":
    function = Function()
    err = function.start("3pi/sin(10)-raiz(8;3)")

    if err is not None:
        print("Incompleto => {}".format(err))
    else:
        print("{}".format(function.variable.package))
        value = function.f({"x": 5})
        print("{}".format(value))
