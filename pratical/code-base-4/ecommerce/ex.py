from ecommerce.inventory.models import Product, ProductAttribute,ProductAttributeValue,ProductAttributeValues,ProductInventory,ProductType,ProductTypeAttribute,Category,Stock,Media,Brand
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresLexer
from sqlparse import format

def sql(x):
    formatted = format(str(x.query), reindent=True)
    print(highlight(formatted, PostgresLexer(), TerminalFormatter()))

# 102. Retrieve all sub-products for an individual product
Product.objects.all().filter(id=1)