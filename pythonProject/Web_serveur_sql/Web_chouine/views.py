from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
import matplotlib.pyplot as plt





def affichecapteur(request, id):
    capteur = models.Capteur.objects.get(pk=id)
    temp  = models.Temperature.objects.all()
    t_date, t_temp = [], []

    return render(request, "Web_chouine/capteur/affichecapteur.html", {"capteur" : capteur, 'temp':temp, 't_date':t_date, 't_temp':t_temp})

def updatecapteur(request, id):
    capteur = models.Capteur.objects.get(pk=id)
    temp  = models.Temperature.objects.all()
    return render(request, "Web_chouine/capteur/updatecapteur.html", {"capteur" : capteur, 'temp':temp})

def traitementupdatecapteur(request, id):
    lform = CapteurForm(request.POST)
    if lform.is_valid():
        capteur = lform.save(commit=False)
        capteur.id = id
        capteur.save()
        return HttpResponseRedirect("/Web_chouine/affichecapteur/")
    else:
        return render(request, "Web_chouine/capteur/updatejeu.html", {"form": lform, "id": id})


def graph(x, y):
    fig, ax = plt.subplots()
    capteur = models.Capteur.objects.all()
    temp = models.Temperature.objects.all()
    plt.plot(x, y, "o-", label="temperature_capteur")
    plt.title("Evolution de la vaccination dans le haut-rhin")
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('nombre de personnes')
    return plt.show()

def graph():
    fig, ax = plt.subplots()
    docL = pandas.read_csv('graphhh.csv', delimiter=';', low_memory=False, encoding="utf-8")
    x = (([k for k in docL['region_residence']]), ([k for k in docL["effectif_1_inj"]])) #, (k for k in docL['effectif_termine']), (k for k in docL['effectif_rappel'])
    axe_x, axe_2, axe_3 = [], [], []
    print(x)
    for i in range(len(x[0])):
        if x[0][i] == 1:
            axe_x.append(x[1][i])
            """axe_2.append(x[2])
            axe_3.append(x[3])"""
    date = docL['date'].tolist()
    #axe_y = [date[k] for k in range(len(axe_x))]
    axe_y = [f'date {k}' for k in range(len(axe_x))]
    axe_2 = [k*2000 for k in range(len(axe_x))]
    axe_3 = [k+200 for k in range(len(axe_x))]
    print(axe_y)
    plt.plot(axe_y, axe_x,"o-", label="1 dose")
    plt.plot(axe_y, axe_2,"o-",label='2 doses')
    plt.plot(axe_y, axe_3,"o-", label='3 doses')
    plt.title("Evolution de la vaccination dans le haut-rhin")
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('nombre de personnes')
    return plt.show()



#BROUILLON
"""
    for t in temp:
        if capteur==temp.capteur:
            t_temp+=t.temp
            t_date+=t.date"""