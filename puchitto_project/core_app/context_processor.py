from core_app.models import *
from django.db.models import Max,Min
def default(rq):
    categories=Category.objects.all()
    min_max_price = Package.objects.aggregate(Min("price"), Max("price"))

    
    return{
        'categories':categories,
        'min_max_price':min_max_price,
    }