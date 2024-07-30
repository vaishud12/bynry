from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import ServiceRequest
from .forms import ServiceRequestForm

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def track_request(request):
    if not hasattr(request.user, 'customer'):
        return HttpResponseForbidden("You don't have a customer profile associated with your account.")
    
    # Proceed with fetching requests if customer exists
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer_service/track_request.html', {'requests': requests})
