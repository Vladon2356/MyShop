from .models import Products, Category

class CategoriesMixin():
    def get_all_categories(self):
        return Category.objects.all()

class ProductsMixin():
    def get_products(self):
        return Products.objects.all().select_related('category')
