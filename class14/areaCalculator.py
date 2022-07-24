def area(w, h):
    print(f"The area of a {w:.1f}x{h:.1f} terrain is {(w * h):.1f} m^2")

wid = float(input("WIDTH (m): "))
hei = float(input("HEIGHT: (m): "))
area(wid, hei)