from rest_framework import serializers
from masters.models import Party

class partySerial(serializers.ModelSerializer):
    class Meta:
        model = Party
        #fields = ['p_uuid' ,'p_name', 'p_address_1', 'p_address_2', 'p_author']
        fields = '__all__'

    def create(self, validated_data):
        return Party.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.p_uuid= validated_data.get('p_uuid', instance.p_uuid)
        instance.p_name= validated_data.get('p_name', instance.p_name) 
        instance.p_address_1= validated_data.get('p_address_1', instance.p_address_1)        
        instance.p_address_2= validated_data.get('p_address_2', instance.p_address_2)        
        instance.p_author= validated_data.get('p_author', instance.p_author) 
        instance.p_date= validated_data.get('p_date', instance.p_date)

        instance.p_contacts_email= validated_data.get('p_contacts_email', instance.p_contacts_email)
        instance.p_contacts_phone= validated_data.get('p_contacts_phone', instance.p_contacts_phone)
        instance.p_contacts_fax= validated_data.get('p_contacts_fax', instance.p_contacts_fax)
        instance.p_contacts_website= validated_data.get('p_contacts_website', instance.p_contacts_website)

        instance.p_id_rccm= validated_data.get('p_id_rccm', instance.p_id_rccm)
        instance.p_id_id= validated_data.get('p_id_id', instance.p_id_id)
        instance.p_id_tva= validated_data.get('p_id_tva', instance.p_id_tva)
        instance.p_id_nif= validated_data.get('p_id_nif', instance.p_id_nif)

        instance.p_cp_1_name= validated_data.get('p_cp_1_name', instance.p_cp_1_name)
        instance.p_cp_1_phone= validated_data.get('p_cp_1_phone', instance.p_cp_1_phone)
        instance.p_cp_1_email= validated_data.get('p_cp_1_email', instance.p_cp_1_email)

        instance.p_cp_2_name= validated_data.get('p_cp_2_name', instance.p_cp_2_name)
        instance.p_cp_2_phone= validated_data.get('p_cp_2_phone', instance.p_cp_2_phone)
        instance.p_cp_2_email= validated_data.get('p_cp_2_email', instance.p_cp_2_email)

        instance.save()
        return instance