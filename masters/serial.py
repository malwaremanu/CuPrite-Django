from rest_framework import serializers
from masters.models import Party

class partySerial(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['p_uuid' ,'p_name', 'p_address', 'p_author','p_email','p_date', 'p_company','p_is_active']

    def create(seld, validated_data):
        return Party.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.p_uuid= validated_data.get('p_uuid', instance.p_uuid)
        instance.p_name= validated_data.get('p_name', instance.p_name) 
        instance.p_address= validated_data.get('p_address', instance.p_address)        
        instance.p_author= validated_data.get('p_author', instance.p_author)        
        instance.p_email= validated_data.get('p_email', instance.p_email)
        instance.p_date= validated_data.get('p_date', instance.p_date)        
        instance.p_company= validated_data.get('p_company', instance.p_company)        
        instance.p_author= validated_data.get('p_author', instance.p_author)
        instance.save()
        return instance