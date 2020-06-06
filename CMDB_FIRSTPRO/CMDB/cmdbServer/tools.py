from django.forms.models import model_to_dict

def modelToDict(instance, fields=None, exclude=None, data= None):
    dict = model_to_dict(instance,fields=fields,exclude=exclude)
    if data != None :
        for key in data.keys():
            dict[key]=data[key]
    return dict