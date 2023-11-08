from django.shortcuts import render
from .forms import MyForm
from django.contrib import messages
from base64 import b64encode
from .editing import trim_image_to_square
import pickle
pickled_model = pickle.load(open('knn_model_images.pkl', 'rb'))



def one_view(request):
    if request.method == 'POST':
        one_form = MyForm(request.POST, request.FILES)
        if one_form.is_valid():
            # name = one_form.cleaned_data
            image_file = one_form.cleaned_data.get('img')
            data = image_file.read()
            encoded = b64encode(data).decode()
            mime = 'image/jpeg;'
            edited_image_array = trim_image_to_square(image_file)
            edited_image_array = pickled_model.predict(edited_image_array.reshape(1, -1))
            # edited_image_array = edited_image_array.reshape(1, -1)
            
            """
            data = image_file.read()
            encoded = b64encode(data).decode()
            mime = 'image/jpeg;'
            context = {"image": f"data:{mime}base64,{encoded}",
                       'data': name.get('name'),
                       'one_form': MyForm()
                       }
            """
            context = {'image': edited_image_array, 'one_form': MyForm(), "image2": f"data:{mime}base64,{encoded}"}
            messages.success(request, "Data is in order")
            return render(request, 'myapp/home.html', context)
        else:
            messages.error(request, one_form.errors)
            return render(request, 'myapp/home.html', {'one_form': MyForm()})        
    else:
        return render(request, 'myapp/home.html', {'one_form': MyForm()})



def methodology(request):
    return render(request, 'myapp/methodology.html', {})