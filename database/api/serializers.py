from rest_framework import serializers
from database.models import Movie
def len_val(value):
    if len(value)<90:
        raise serializers.ValidationError("vbcvbcv")
    else:
        return value

class MovieSerializer(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    disc=serializers.CharField(validators=[len_val])
    active=serializers.BooleanField()

    def create(self,validated_data):
        return Movie.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.disc=validated_data.get('disc',instance.disc)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance

    def validate(self,data):
        if data['name']==data['disc']:
            raise serializers.ValidationError("Name and Description can't be same!")
        else:
            return data

    def validate_name(self,value):
        if len(value)==0:
            raise serializers.ValidationError("Movie Name Must be Provided!")
        else:
            return value
    # def validate_disc(self,value):
    #     if len(value)<90:
    #         raise serializers.ValidationError("Description length must be greater than 90 words")
    #     else:
    #         return value


