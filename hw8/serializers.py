from rest_framework import serializers

from .models import Employee, Position


class PositionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    position = serializers.CharField(max_length=30)
    department = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.position = validated_data['position']
        instance.department = validated_data['department']
        instance.save()
        return instance


class EmployeeSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=20)
    birth_date = serializers.DateField()
    position = serializers.CharField(max_length=30)
    salary = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.birth_date = validated_data['birth_date']
        instance.position = validated_data['position']
        instance.salary = validated_data['salary']
        instance.save()
        return instance
