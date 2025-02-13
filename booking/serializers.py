from rest_framework import serializers
from .models import Booking
from users.serializers import UserAccountSerializer
from artists.serializers import ArtistSerializer
from dispute.serializers import DisputeSerializer
from payment.models import Payment
from artists.models import Artist, Rate
from review.serializers import ReviewsSerializer


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['id','name','amount']


class BookingSerializer(serializers.ModelSerializer):
    disputes = DisputeSerializer(many=True, read_only=True)
    client = UserAccountSerializer(read_only=True)
    artist = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        write_only=True
    )
    rate = serializers.PrimaryKeyRelatedField(
        queryset = Rate.objects.all(),
        write_only=True
    )
    artist_details = ArtistSerializer(source='artist', read_only=True)
    rate_details = RateSerializer(source='rate', read_only=True)
    reviews = ReviewsSerializer(read_only=True, many=True)
    # service_fee = serializers.SerializerMethodField()
    downpayment_amount = serializers.SerializerMethodField()
    is_event_due = serializers.BooleanField(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

    # def get_service_fee(self, obj):
    #     downpayment = Payment.objects.filter(booking=obj, payment_type='downpayment').first()
    #     if downpayment:
    #         return downpayment.service_fee
    #     return None
    def get_downpayment_amount(self,obj):
        return obj.calculate_downpayment()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['formatted_event_date'] = instance.event_date.strftime('%B %d, %Y')
        representation['formatted_start_time'] = instance.start_time.strftime('%I:%M %p')
        representation['formatted_end_time'] = instance.end_time.strftime('%I:%M %p')
        representation['timeslot'] = f'{instance.start_time.strftime('%I:%M %p')} - {instance.end_time.strftime('%I:%M %p')}'
        representation['artist'] = representation.pop('artist_details')
        representation['rate'] = representation.pop('rate_details')
        if representation['reviews']:
            representation['reviews'] = representation['reviews'][0]
        representation['location'] = f'{instance.street}, {instance.barangay}, {instance.municipality}, {instance.province}, Philippines @{instance.landmark}'
        return representation
