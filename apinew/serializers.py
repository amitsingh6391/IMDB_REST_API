from apinew.models import WatchList,StreamPlatform
from rest_framework  import serializers

                        # '''**** MODAL SERIALIZERS'''



class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = "__all__" # we can define all method to define all fields
     
    
   


class StreamPlatformSerializer(serializers.ModelSerializer):

#watchlist is same as we are defined;
    watchlist = WatchListSerializer(many=True,read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"





