from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    RelatedField,
    ReadOnlyField,
    )
from apps.store.models import Category, Item, Transaction, ItemImage


#------------------------------------------------------------------------------
#Category
#------------------------------------------------------------------------------

class CategoryListSerializer(ModelSerializer):
    '''
    This class is a serializer that will show what information should display
    on the API when listing all Category models.

    Attributes:
        id : the ID of the Category
        name: the name given to that Category
        '''
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]

class CategoryDetailSerializer(ModelSerializer):
    '''
    This class is a serializer that will show what information should display
    on the API when listing all Category models.

    Attributes:
        id : the ID of the Category
        name: the name given to that Category
    '''
    class Meta:
        model = Category
        fields = [
            'id',
            'slug'
        ]
        'name'

#------------------------------------------------------------------------------
#subCategory
#------------------------------------------------------------------------------

'''
class SubCategoryCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'name',
            'parent',
        ]


class SubCategoryDetailSerializer(ModelSerializer):

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'name',
            'parent',
        ]

class SubCategoryListSerializer(ModelSerializer):

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'name',
            'parent',
        ]
'''

#------------------------------------------------------------------------------
#Items
#------------------------------------------------------------------------------
class ItemImageDetailSerializer(ModelSerializer):
    class Meta:
        model = ItemImage 
        image = SerializerMethodField()
        fields = [
            'id',
            'item',
            'item_name',
            'image'
        ]

        def get_image(self,obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

class ItemImageSerializer(ModelSerializer):
    class Meta:
        model = ItemImage
        image = SerializerMethodField()
        fields = [
            'id',
            'image',
            'item'
        ]

class ItemCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'material',
            'category',
        ]

class ItemDetailSeralizer(ModelSerializer):
    images = ItemImageDetailSerializer(many = True, read_only = True)
    class Meta:
        listings = StringRelatedField(many = True)
        category = CategoryDetailSerializer(read_only = True)
        model = Item
        fields = [
            'id',
            'slug',
            'seller_name',
            'name',
            'images',
            'description',
            'material',
            'category',
            'category_name',
            'price',
            'lastActive',
            'visible',
            'stock',
        ]

  

class ItemListlSeralizer(ModelSerializer):
    images = ItemImageDetailSerializer(many = True, read_only = True)
    class Meta:
        category = CategoryDetailSerializer(read_only = True)
        model = Item
        fields = [
            'id',
            'slug',
            'name',
            'seller_name',
            'images',
            'category',
            'category_name',
            'lastActive',
            'visible',
            'stock',
            'price',
        ]




#------------------------------------------------------------------------------
#Listing
#------------------------------------------------------------------------------


# class ListingCreateUpdateSerializer(ModelSerializer):
#
#
#     class Meta:
#         model = Listing
#         fields = [
#             'item',
#             'image',
#             'conditionRating',
#             'location',
#             'price',
#             'size',
#             'image'
#         ]
#
# class ListingDetailSeralizer(ModelSerializer):
#
#     item_name = ReadOnlyField
#     item_slug = ReadOnlyField
#     image = SerializerMethodField()
#
#
#     class Meta:
#         model = Listing
#         fields = [
#             'id',
#             'seller',
#             'image',
#             'item',
#             'item_name',
#             'item_slug',
#             'conditionRating',
#             'description',
#             'location',
#             'price',
#             'size',
#             'available',
#             'created',
#         ]
#     def get_image(self,obj):
#         try:
#             image = obj.image.url
#         except:
#             image = None
#         return image
#
# class ListingListSeralizer(ModelSerializer):
#
#     item_name = ReadOnlyField
#     item_slug = ReadOnlyField
#     image = SerializerMethodField()
#
#     class Meta:
#         model = Listing
#         fields = [
#             'id',
#             'item',
#             'image',
#             'item_name',
#             'item_slug',
#             'conditionRating',
#             'price',
#             'size',
#             'available',
#             'created',
#
#         ]
#     def get_image(self,obj):
#         try:
#             image = obj.image.url
#         except:
#             image = None
#         return image

#------------------------------------------------------------------------------
#Transaction
#------------------------------------------------------------------------------

class TransactionCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Transaction

        fields = [
            'seller',
            'buyer',
            'amountExchanged',
            'deliveryAddress',
            'receiveAddress',
            'listing',
            'ratingSeller',
            'ratingBuyer',
            'isValid'

        ]

class TransactionDetailSerializer(ModelSerializer):
    class Meta:
        model = Transaction

        fields = '__all__'

class TransactionListSerializer(ModelSerializer):
    class Meta:

        model = Transaction

        fields = '__all__'


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
