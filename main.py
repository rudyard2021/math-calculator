from function import Function


if __name__ == "__main__":
    function = Function()
    function.start("3pi/sin(10)-raiz(8;3)")

    if function.message is not None:
        print("Incompleto => {}".format(function.message))
    else:
        print("{}".format(function.variable.package))
        value = function.f({"x": 5})
        print("{}".format(value))
