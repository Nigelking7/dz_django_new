from rest_framework import serializers, validators
from api.models import ApiUser, Good, Storage


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
    choice = serializers.ChoiceField(choices=ApiUser.choice_type)

    def update(self, instance, validated_data):
        if email := validated_data.get("email"):
            instance.email = email
            instance.save(update_fields=["email"])
        if password := validated_data.get("password"):
            instance.set_password(password)
            instance.save(update_fields=["password"])
        return instance

    def create(self, validated_data):
        user = ApiUser.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            choice=validated_data["choice"]
        )
        user.set_password(validated_data["password"])
        user.save(update_fields=["password"])
        return user


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ["name"]


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['name', "goods"]


class FromAndToStorageSerializer(serializers.Serializer):
    good = serializers.CharField()
    quantity = serializers.IntegerField()
