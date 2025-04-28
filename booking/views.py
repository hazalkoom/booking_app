from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Booking
from .forms import BookingForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def property_list(request):
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort = request.GET.get('sort', 'name')  # default sort

    properties = Property.objects.all()

    # Search
    if query:
        properties = properties.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )

    # Filter by price
    if min_price:
        properties = properties.filter(price_per_night__gte=min_price)
    if max_price:
        properties = properties.filter(price_per_night__lte=max_price)

    # Sorting
    if sort in ['name', '-name', 'price_per_night', '-price_per_night']:
        properties = properties.order_by(sort)

    # Pagination
    paginator = Paginator(properties, 6)  # 6 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'properties': page_obj,
        'query': query,
        'min_price': min_price,
        'max_price': max_price,
        'sort': sort,
    }
    return render(request, 'booking/property_list.html', context)

@login_required
def book_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property
            booking.user = request.user  # Link to current logged-in user
            booking.save()

            # Send confirmation email
            send_mail(
                subject='Your Booking is Confirmed!',
                message=(
                    f'Hello {request.user.username},\n\n'
                    f'Your booking for "{property.name}" from {booking.check_in} to {booking.check_out} '
                    f'has been successfully confirmed.\n\n'
                    f'Property location: {property.location}\n'
                    f'Total Guests: {booking.guests}\n\n'
                    'Thank you for booking with us!'
                ),
                from_email=None,
                recipient_list=[request.user.email],
                fail_silently=True,  # You can set this to False during debugging
            )

            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'booking/book_property.html', {
        'form': form,
        'property': property,
    })


def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return render(request, 'booking/booking_confirmation.html', {'booking': booking})