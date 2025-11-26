
# physics_formulas.py
# Physics formulas a–e

import math

def formula_a_displacement(u, t, acc):
    return u * t + 0.5 * acc * t**2

def formula_b_final_velocity_squared(u, acc, s):
    v2 = u**2 + 2 * acc * s
    v = math.sqrt(v2) if v2 >= 0 else float('nan')
    return v2, v

def formula_c_force(mass, acc):
    return mass * acc

def formula_d_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

def formula_e_gravitational_potential(mass, height, g=9.81):
    return mass * g * height

def prompt_float(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Invalid number. Try again.")

def main():
    print("Physics formulas (choose a letter):")
    print("a - Displacement s = u*t + 0.5*a*t^2")
    print("b - Final velocity squared v^2 = u^2 + 2*a*s")
    print("c - Force F = m * a")
    print("d - Kinetic energy KE = 0.5 * m * v^2")
    print("e - Gravitational potential PE = m * g * h")
    choice = input("Pick letter (a, b, c, d, e): ").strip().lower()

    if choice == 'a':
        u = prompt_float("Enter initial velocity u (m/s): ")
        t = prompt_float("Enter time t (s): ")
        acc = prompt_float("Enter acceleration a (m/s^2): ")
        s = formula_a_displacement(u, t, acc)
        print(f"Displacement s = {s} m")

    elif choice == 'b':
        u = prompt_float("Enter initial velocity u (m/s): ")
        acc = prompt_float("Enter acceleration a (m/s^2): ")
        s = prompt_float("Enter displacement s (m): ")
        v2, v = formula_b_final_velocity_squared(u, acc, s)
        print(f"v^2 = {v2}")
        print(f"v = {v}")

    elif choice == 'c':
        m = prompt_float("Enter mass m (kg): ")
        acc = prompt_float("Enter acceleration a (m/s^2): ")
        F = formula_c_force(m, acc)
        print(f"Force F = {F} N")

    elif choice == 'd':
        m = prompt_float("Enter mass m (kg): ")
        v = prompt_float("Enter speed v (m/s): ")
        ke = formula_d_kinetic_energy(m, v)
        print(f"Kinetic Energy KE = {ke} J")
    choice = input("Pick letter (a, b, c, d, e): ").strip().lower()


        m = prompt_float("Enter mass m (kg): ")
        h = prompt_float("Enter height h (m): ")
        g = prompt_float("Enter g (m/s^2) or press Enter for 9.81: ") if False else 9.81
        pe = formula_e_gravitational_potential(m, h, g)
        print(f"Potential Energy PE = {pe} J")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
