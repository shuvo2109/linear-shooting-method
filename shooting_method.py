import math


# Change this
def p(x):
    value = - 2 / x
    return value


# Change this
def q(x):
    value = 2 / (x ** 2)
    return value


# Change this
def r(x):
    value = math.sin(math.log(x, math.e)) / (x ** 2)
    return value


# Used for refining input. DO NOT CHANGE ANYTHING.
def refine_input(string1='', string2='', type_=None):
    while True:
        variable = input("Enter {} = {} = ".format(string1, string2))
        try:
            variable = type_(variable)
            break
        except ValueError:
            print("That is not a valid input. Value has to be {}.".format(type_.__name__))
    return variable


# Used for refining output. DO NOT CHANGE ANYTHING.
def refine_output(value):
    value_string = str(value)
    if len(value_string) > 8:
        value_string = value_string[0:5] + "..."
    cut = len(value_string)
    fill = 8 - cut
    refined_output = value_string + " " * fill
    return refined_output


# Used for main calculation. DO NOT CHANGE ANYTHING.
def main():
    # Boundary and step-size setup
    # Receive value of a
    a = refine_input('initial x-value', 'a', float)

    # Receive value of alpha = y(a)
    alpha = refine_input('initial y-value', 'y(a) = alpha', float)

    # Receive value of b
    b = refine_input('final x-value', 'b', float)

    # Receive value of beta = y(b)
    beta = refine_input('final y-value', 'y(b) = beta', float)

    # Receive step-size
    N = refine_input('number of steps', 'N', int)

    # Step-size calculation
    h = (b - a) / N

    # Calculation initialization
    # Loop variable
    x = 0

    # Reserved for the x and y-values
    xi = [a]
    yi = [alpha]

    # Vectors for Range-Kutta calculation
    u = [[0], [0] * (N + 1), [0] * (N + 1)]
    v = [[0], [0] * (N + 1), [0] * (N + 1)]
    ku = [[0, 0, 0], [0, 11, 12], [0, 21, 22], [0, 31, 32], [0, 41, 42]]
    kv = [[0, 0, 0], [0, 11, 12], [0, 21, 22], [0, 31, 32], [0, 41, 42]]

    # Vector initialization
    u[1][0] = alpha
    u[2][0] = 0
    v[1][0] = 0
    v[2][0] = 1

    # Loop calculation
    for i in range(0, N):
        x = a + i * h

        # R-K for Equation 1
        ku[1][1] = h * u[2][i]
        ku[1][2] = h * (p(x) * u[2][i] + q(x) * u[1][i] + r(x))
        ku[2][1] = h * (u[2][i] + 0.5 * ku[1][2])
        ku[2][2] = h * (p(x + h / 2) * (u[2][i] + 0.5 * ku[1][2]) + q(x + h / 2) * (u[1][i] + 0.5 * ku[1][1]) + r(x + h / 2))
        ku[3][1] = h * (u[2][i] + 0.5 * ku[2][2])
        ku[3][2] = h * (p(x + h / 2) * (u[2][i] + 0.5 * ku[2][2]) + q(x + h / 2) * (u[1][i] + 0.5 * ku[2][1]) + r(x + h / 2))
        ku[4][1] = h * (u[2][i] + ku[3][2])
        ku[4][2] = h * (p(x + h) * (u[2][i] + ku[3][2]) + q(x + h) * (u[1][i] + ku[3][1]) + r(x + h))

        u[1][i + 1] = u[1][i] + (ku[1][1] + 2 * ku[2][1] + 2 * ku[3][1] + ku[4][1]) / 6
        u[2][i + 1] = u[2][i] + (ku[1][2] + 2 * ku[2][2] + 2 * ku[3][2] + ku[4][2]) / 6

        # R-K for Equation 2
        kv[1][1] = h * v[2][i]
        kv[1][2] = h * (p(x) * v[2][i] + q(x) * v[1][i])
        kv[2][1] = h * (v[2][i] + 0.5 * kv[1][2])
        kv[2][2] = h * (p(x + h / 2) * (v[2][i] + 0.5 * kv[1][2]) + q(x + h / 2) * (v[1][i] + 0.5 * kv[1][1]))
        kv[3][1] = h * (v[2][i] + 0.5 * kv[2][2])
        kv[3][2] = h * (p(x + h / 2) * (v[2][i] + 0.5 * kv[2][2]) + q(x + h / 2) * (v[1][i] + 0.5 * kv[2][1]))
        kv[4][1] = h * (v[2][i] + kv[3][2])
        kv[4][2] = h * (p(x + h) * (v[2][i] + kv[3][2]) + q(x + h) * (v[1][i] + kv[3][1]))

        v[1][i + 1] = v[1][i] + (kv[1][1] + 2 * kv[2][1] + 2 * kv[3][1] + kv[4][1]) / 6
        v[2][i + 1] = v[2][i] + (kv[1][2] + 2 * kv[2][2] + 2 * kv[3][2] + kv[4][2]) / 6

    y2_coefficient = (beta - u[1][N]) / v[1][N]

    # Setting up xi and yi
    for i in range(1, N + 1):
        xi.append(a + i * h)
        yi.append(u[1][i] + y2_coefficient * v[1][i])

    # Printing output values of xi and yi
    print("{} {} {}".format(refine_output('i'), refine_output('xi'), refine_output('yi')))
    print("-" * 26)
    for i in range(0, len(xi)):
        print("{} {} {}".format(refine_output(i), refine_output(round(xi[i], 6)), refine_output(round(yi[i], 6))))

    # Termination
    end = input("\nPress ENTER to quit.")


if __name__ == "__main__":
    main()
