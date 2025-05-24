from django.shortcuts import render
from .forms import DiabetesForm
from .models import PatientData
from ml_model.predictor import predict_diabetes

def index(request):
    result = None
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = [
                data['pregnancies'], data['glucose'], data['blood_pressure'],
                data['skin_thickness'], data['insulin'], data['bmi'],
                data['diabetes_pedigree_function'], data['age']
            ]
            model_choice = data['model_choice']
            result = predict_diabetes(input_data, model_choice)
            PatientData.objects.create(
                **{k: v for k, v in data.items() if k != 'model_choice'},
                prediction_result=result
            )
    else:
        form = DiabetesForm()
    return render(request, 'index.html', {'form': form, 'result': result})
