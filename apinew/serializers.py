from apinew.models import WatchList,StreamPlatform,Review
from rest_framework  import serializers

                        # '''**** MODAL SERIALIZERS'''



class ReviewSerializer(serializers.ModelSerializer):

    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"



class WatchListSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True,read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__" # we can define all method to define all fields
     
    
   


class StreamPlatformSerializer(serializers.ModelSerializer):

#watchlist is same as we are defined;
    watchlist = WatchListSerializer(many=True,read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"





