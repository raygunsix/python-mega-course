temperatures = [10, -20, -289, 100]
def c_to_f(c):
        f = c* 9/5 + 32
        return f

with open("temperature.txt", "w") as file:
        for t in temperatures:
            if t >= -273.15:
                f = c_to_f(t)
                file.write("%s\n" % f)