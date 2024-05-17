from django.shortcuts import render
from app.train import model, get_prediction


def index(request):
    context = {
        'status': 'Input test results'
    }
    return render(request, 'app/index.html', context)


def predict(request):
    context = {
        'status': 'Input test results'
    }
    if request.method == "POST":
        prediction = get_prediction(model, request.POST)
        context = {
            'status': f"Prediction = {prediction}"
        }
        features = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean",
                    "compactness_mean","concavity_mean","concave_points_mean","symmetry_mean",
                    "fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se",
                    "compactness_se","concavity_se","concave_points_se","symmetry_se","fractal_dimension_se",
                    "radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst",
                    "compactness_worst","concavity_worst","concave_points_worst","symmetry_worst","fractal_dimension_worst"]
        for key in features:
            if key in request.POST:
                context[key] = request.POST[key]
    return render(request, 'app/index.html', context)