from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemView


class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(
            title="Pizza",
            price=7.5,
            inventory=100,
        )
        Menu.objects.create(
            title="Salad",
            price=4.5,
            inventory=100,
        )

    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_items = MenuSerializer(menuitems, many=True)
        factory = APIRequestFactory()
        request = factory.get('restaurant/menu/')
        response = MenuItemView.as_view()(request)
        self.assertEqual(response.data, serialized_items.data)
