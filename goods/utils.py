from turtle import color
from django.db.models import Q
from django.contrib.postgres.search import SearchHeadline, SearchVector, SearchQuery, SearchRank
from django.utils.termcolors import background

from goods.models import Products


def q_search(query):
    
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = Products.objects.annotate(rank=SearchRank(vector, query),).filter(rank__gt=0).order_by("-rank")
    result = result.annotate(
    headline=SearchHeadline(         
        "name",
        query,
        start_sel='<span style="background-color: yellow;">',
        stop_sel="</span>",
        ),
    )

    result = result.annotate(
    headline=SearchHeadline(         
        "description",
        query,
        start_sel='<span style="background-color: yellow;">',
        stop_sel="</span>",
        ),
    )

    return result