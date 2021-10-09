from apinew.models import Movie
from rest_framework  import serializers

                        # '''**** MODAL SERIALIZERS'''

class MovieSerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()

    class Meta:

        model = Movie
      
        fields = "__all__" # we can define all method to define all fields
        # fields =['id','name','description'] # We can define fields in our list or map which we want to show.
     
      # if we want to not show a particular field then we can use Exclude method.
      #  rather then specify all the fields which we want to use.
        # exclude =['active']
    
    #define custom field name:
    def get_len_name(self,object):

        length = len(object.name)
        return length

    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description should not be same")
        return data

  
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value






 
                    #   '''****** SERIAL SERIALIZERS****''''
# def name_length(value):
#       if len(value)<2:
#             raise serializers.ValidationError("Name is too short")



     

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name =serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self,validated_data):
#        return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance

# # Object level validation.
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description should not be same")
#         return data

#     # field label validation
#     # def validate_name(self,value):
#     #     if len(value)<2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value
