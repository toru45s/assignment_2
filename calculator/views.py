from django.shortcuts import render
from django.views import View

from .helper import Helper

# Create your views here.

class CalculatorView(View):
    def get(self, request):
        return render(request, 'calculator/index.html')

    def post(self, request):
        a = int(request.POST.get('num1'))
        b = int(request.POST.get('num2'))
        c = int(request.POST.get('num3'))

        result = Helper.calculate(a, b, c)
        result_date = Helper.get_current_date()

        step1 = round(result["step1"] , 2)
        step2 = round(result["step2"] , 2)
        step3 = round(result["step3"] , 2)
        step4 = round(result["step4"] , 2)
        step5 = round(result["step5"] , 2)
        
        return render(request, 'calculator/result.html', {'result_date': result_date, 'a' : a, 'b' : b, 'c' : c, 'step1': step1, 'step2': step2, 'step3': step3, 'step4': step4, 'step5': step5})