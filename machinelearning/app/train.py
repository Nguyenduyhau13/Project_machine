import joblib
import numpy as np

def model():
    # Load the trained model
    loaded_model = joblib.load('app\\training\KNN.pkl')
    return loaded_model

def get_prediction(model, input_data):
    model = model()

    # Lấy các giá trị đầu vào từ QueryDict
    radius_mean = float(input_data.get('radius_mean', 0))
    texture_mean = float(input_data.get('texture_mean', 0))
    perimeter_mean = float(input_data.get('perimeter_mean', 0))
    area_mean = float(input_data.get('area_mean', 0))
    smoothness_mean = float(input_data.get('smoothness_mean', 0))
    compactness_mean = float(input_data.get('compactness_mean', 0))
    concavity_mean = float(input_data.get('concavity_mean', 0))
    concave_points_mean = float(input_data.get('concave_points_mean', 0))
    symmetry_mean = float(input_data.get('symmetry_mean', 0))
    fractal_dimension_mean = float(input_data.get('fractal_dimension_mean', 0))
    radius_se = float(input_data.get('radius_se', 0))
    texture_se = float(input_data.get('texture_se', 0))
    perimeter_se = float(input_data.get('perimeter_se', 0))
    area_se = float(input_data.get('area_se', 0))
    smoothness_se= float(input_data.get('smoothness_se', 0))
    compactness_se = float(input_data.get('compactness_se', 0))
    concavity_se = float(input_data.get('concavity_se', 0))
    concave_points_se = float(input_data.get('concave_points_se', 0))
    symmetry_se = float(input_data.get('symmetry_se', 0))
    fractal_dimension_se = float(input_data.get('fractal_dimension_se', 0))
    radius_worst = float(input_data.get('radius_worst', 0))
    texture_worst = float(input_data.get('texture_worst', 0))
    perimeter_worst = float(input_data.get('perimeter_worst', 0))
    area_worst = float(input_data.get('area_worst', 0))
    smoothness_worst = float(input_data.get('smoothness_worst', 0))
    compactness_worst = float(input_data.get('compactness_worst', 0))
    concavity_worst = float(input_data.get('concavity_worst', 0))
    concave_points_worst = float(input_data.get('concave_points_worst', 0))
    symmetry_worst = float(input_data.get('symmetry_worst', 0))
    fractal_dimension_worst = float(input_data.get('fractal_dimension_worst', 0))
    # Các giá trị khác tương tự

    # Chuyển đổi các giá trị thành mảng NumPy
    input_array = np.array([[radius_mean, texture_mean, perimeter_mean,area_mean ,smoothness_mean ,compactness_mean ,
                             concavity_mean,concave_points_mean ,symmetry_mean ,fractal_dimension_mean ,radius_se ,
                             texture_se,perimeter_se,area_se , smoothness_se,compactness_se ,concavity_se ,
                             concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst ,perimeter_worst,
                             area_worst,smoothness_worst,compactness_worst, concavity_worst,concave_points_worst,symmetry_worst,
                             fractal_dimension_worst]])  # Thêm các giá trị khác vào đây

    # Dự đoán
    prediction = model.predict(input_array)

    labels = {0: "lành tính", 1: "ác tính"}
    prediction_label = labels[prediction[0]]

    return prediction_label
