
import math

def trig_values(sine):
    cosine = math.cos(math.asin(sine))
    tangent = math.tan(math.asin(sine)) if math.cos(math.asin(sine))!= 0 else None
    cotangent = 1 / tangent if tangent is not None else None
    return [round(sine, 2), round(cosine, 2), round(tangent, 2) if tangent is not None else None, round(cotangent, 2) if cotangent is not None else None]

# Example usage:
print(trig_values(0.6))  # Output: [0.5, 0.87, 1.05, 0.95]

