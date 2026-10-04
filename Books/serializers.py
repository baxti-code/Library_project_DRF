from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError
import re
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id','title', 'subtitle', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        
        if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\s\-]+$', title):
            raise ValidationError(
                {
                    'status':False,
                    'message':'title has to be all alphabetical'
                }
            )
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status':False,
                    'message' : 'You can not create duplicate books'
                }
            )
        return data
    def validate_price(self, price):
        if price < 0 or price > 999999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Price must be between 0 and 999999999'
                }
            )
        return price