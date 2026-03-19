from django.shortcuts import render
from .models import Category, Tag, Product

def product_list(request):
    products = Product.objects.all()

    search = request.GET.get("search")
    category = request.GET.get("category")
    tag = request.GET.getlist("tag")

    if search:
        products = products.filter(
            description__icontains=search
        )
    if category:
        products = products.filter(
            category_id = category
        )
    if tag:
        for tag_id in tag:
            products = products.filter(
                tag__id=tag_id
            )

    # pass the data to the template
    context = {
        "products": products,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        # keep the value there after user submitted
        "selected_tag": tag,
        "selected_category": category,
        "search": search or "",
        

    }

    return render(request, "products/product_list.html", context)

