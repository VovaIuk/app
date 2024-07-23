from django.db.models import Q

from goods.models import Products


def q_search(query):
    
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word)>2]

    q_oblects = Q()

    for token in keywords:
        q_oblects |= Q(description__icontains=token)
        q_oblects |= Q(name__icontains=token)

    
    return Products.objects.filter(q_oblects)