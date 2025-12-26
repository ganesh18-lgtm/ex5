from django.shortcuts import render

def calculate_power(request):
    power = None
    intensity = None
    resistance = None
    error = None

    if request.method == "POST":
        try:
            intensity = float(request.POST.get("intensity"))
            resistance = float(request.POST.get("resistance"))

            # Formula: P = I^2 * R
            power = (intensity ** 2) * resistance

        except (TypeError, ValueError):
            error = "Please enter valid numeric values."

    return render(request, "math.html", {
        "power": power,
        "intensity": intensity,
        "resistance": resistance,
        "error": error
    })
