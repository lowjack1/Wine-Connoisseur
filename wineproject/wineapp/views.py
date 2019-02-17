import csv, io
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Contact
from .forms import ContactForm
import re
# from .forms import ContacForm, AddSpamWordForm

def contact(request):
    template = "contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)
        # print(form)

        if form.is_valid():
            form.save()
    else :
        form = ContactForm()

    context = {
        'form' : form,
    }
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')

def contact_upload(request):
    template = "contact_upload.html"
    prompt = {
        'order': 'Order of the CSV should be sno, country, description, designaion, points, price, province, region_1, region_2, variety, winery'
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith(".csv"):
        messages.error(request, "This is not a csv file")
    data_set = csv_file.read().decode("UTF-8")
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter = ',', quotechar = "|" ):
        p1, p2 = "0", "0"
        if(re.match(r"^[0-9]+\.?[0-9]*$", column[4])):
            p1 = column[4]
        else:
            p1 =  "0"
        if(re.match(r"^[0-9]+\.?[0-9]*$", column[5])):
            p2 = column[5]
        else:
            p2 =  "0"

        _, cated = Contact.objects.update_or_create(
            sno = column[0],
            country = column[1],
            description = column[2],
            designaion = column[3],
            points = p1,
            price = p2,
            province = column[6],
            region_1 = column[7],
            region_2 = column[8],
            variety = column[9],
            winery = column[10]
        )
    context = {}
    return render(request, template, context)
