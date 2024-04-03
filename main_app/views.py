from django.shortcuts import render

# Create your views here.


def main_index_page(request):
    return render(request, 'index/index.html')
