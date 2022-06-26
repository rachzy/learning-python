from math import radians, sin, cos, tan

angle = float(input("Enter the angle that you want: \n"));
angleInRadians = radians(angle);
sine = sin(angleInRadians);
cosine = cos(angleInRadians);
tangent = tan(angleInRadians);

print(f"Sine: {sine:.2f} \n Cosine: {cosine:.2f} \n Tangent: {tangent:.2f}");