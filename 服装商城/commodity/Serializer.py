from rest_framework import serializers

from commodity.models import sweaters, sweater


class SweatersSerializer(serializers.ModelSerializer):


    class Meta:
        model = sweaters
        fields = ['id','sws_name','sws_num','sws_pic','sws_operate_time','ss_id']

    # def to_representation(self, instance):
    #
    #     data = super().to_representation(instance)
    #
    #     return data

class SweaterSerializer(serializers.ModelSerializer):
    class Meta:
         model = sweater
         fields = ['id', 'sw_name','s_id' ]