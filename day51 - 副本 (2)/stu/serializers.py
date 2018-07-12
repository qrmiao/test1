
from rest_framework import serializers

from stu.models import Student


class StudentSerializer(serializers.ModelSerializer):
    s_name = serializers.CharField(error_messages={'blank':'用户名不能为空','max_length':'用户名不能超过10个字符'},max_length=10)

    class Meta:
        model = Student
        fields = ['id', 's_name', 's_emil', 's_operate_time']

    def to_representation(self, instance):

        data = super().to_representation(instance)

        return data

