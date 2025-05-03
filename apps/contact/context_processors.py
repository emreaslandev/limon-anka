from .models import Contact

def contact_info(request):
    contact = Contact.objects.first()
    return {'contact': contact}