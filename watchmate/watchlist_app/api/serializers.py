from rest_framework import serializers
from watchlist_app.models import WatchList,StreamingPlatform,Review



class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ("watchlist",)

class WatchListSerializer(serializers.ModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name="watchlist:watch-detail")
    
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamingPlatformSerializer(serializers.HyperlinkedModelSerializer):
    movies = WatchListSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="watchlist:streamingplatform-detail")

    class Meta:
        model = StreamingPlatform
        fields = "__all__"

# class MovieSerializer(serializers.ModelSerializer):
#     name_length = serializers.SerializerMethodField()
#     class Meta:
#         model = Movie
#         # fields = "__all__"
#         # fields = ["id","name","description"]
#         exclude = ["id"]
    
#     def get_name_length(self,obj):
#         return len(obj.name)
        

# def min_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Name should have minimum 3 letter.")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[min_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name",instance.name)
#         instance.description = validated_data.get("description",instance.description)
#         instance.active = validated_data.get("active",instance.active)
#         instance.save()
#         return instance
    
    # def validate_name(self,value):
    #     if len(value) < 3:
    #         raise serializers.ValidationError("Name should have minimum 3 letter.")
    #     else:
    #         return value
    
    # def validate(self,data):
    #     if data["name"] == data["about"]:
    #         raise serializers.ValidationError("Name and Description are same.")
