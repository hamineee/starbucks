import json 
from django.http import JsonResponse 
from django.views import View 
from starbucks.models import Menu, Categories, Drinks

# Create your views here.
class StarbucksView(View): 
    def post(self, request): 
        data = json.loads(request.body)
        print(data)
        """
        {
            "category": "콜드브루",
            "menu": "음료", 
            "product": {
                "name": "맛있는 콜드브루",
                "price": 5400
            }
        }
        """
        
        menu = Menu.objects.create(name=data["menu"])
        category = Categories.objects.get(
            name=data["category"]) #여기서 카테고리는 카테고리가 create되고나서 만들어진 인스턴스를 반환해준다.
        drink = Drinks.objects.create(
            korean_name=data["product"]["name"], category= Categories.objects.get(name=data["category"])) #카테고리 인스턴스의 id속성에 접근
        Menu.objects.create(name=category.menu.name)
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)
        