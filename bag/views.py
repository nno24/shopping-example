from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ A view to render add to bag """
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    # In the following way, we can save what's in the basket..and the user can keep browse!
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    return redirect(redirect_url)