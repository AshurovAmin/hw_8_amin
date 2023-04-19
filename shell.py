import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from hw8.serializers import PositionSerializer, EmployeeSerializer
from django.utils import timezone



json_str = b"""{
    "email": "aminashurov@gmail.com",
    "content": "THIS IS GOOD",
    "created": "2021-04-19"
    }
"""

stream = io.BytesIO(json_str)

data = JSONParser().parse(stream)

serializer = PositionSerializer(data=data)
serializer.is_valid()
print(serializer.errors)
print(serializer.validated_data)

comment = serializer.save(created='2025-12-12')

print(comment)



json_str = b"""{
    "email": "aminashurov@gmail.com",
    "content": "THIS IS GOOD",
    "created": "2021-04-19"
    }
"""

stream = io.BytesIO(json_str)

data = JSONParser().parse(stream)

serializer = EmployeeSerializer(data=data)
serializer.is_valid()
print(serializer.errors)
print(serializer.validated_data)



