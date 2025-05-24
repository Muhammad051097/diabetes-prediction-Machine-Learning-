from django import forms

class DiabetesForm(forms.Form):
    pregnancies = forms.IntegerField()
    glucose = forms.FloatField()
    blood_pressure = forms.FloatField()
    skin_thickness = forms.FloatField()
    insulin = forms.FloatField()
    bmi = forms.FloatField()
    diabetes_pedigree_function = forms.FloatField()
    age = forms.IntegerField()
    model_choice = forms.ChoiceField(choices=[
        ('nb', 'Naive Bayes'),
        ('lr', 'Logistic Regression'),
        ('rf', 'Random Forest'),
        ('knn', 'K-Nearest Neighbors'),
        ('svm', 'SVM'),
        ('dt', 'Decision Tree')
    ])
