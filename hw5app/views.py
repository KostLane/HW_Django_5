from django.shortcuts import render
from .forms import ProductForm

# Create your views here.

def index(request):
    
    html = """
    <h1>Главная страница</h1>
    <p>Задание №4:</p>
    <p>Измените модель продукта, добавьте поле для хранения фотографии продукта.</p>
    <p>Создайте форму, которая позволит сохранять фото.</p>
    <br></br>
    <p>Задание №5:</p>
    <p>Настройте под свои нужды вывод информации о клиентах,</p> 
    <p>товарах и заказах на страницах вывода информации об объекте и вывода списка объектов.</p>
    """
    title = "Задание №4, №5"
    return render(request, 'hw5app/index.html', {'html': html, 'title': title})

def upload_image_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save()
            return render(request, 'hw5app/upload_image.html', {'answer': 'Данные успешно отправлены на сервер!'})
    else:
        product_form = ProductForm()
    return render(request, 'hw5app/upload_image.html', {'product_form': product_form})

