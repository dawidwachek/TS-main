from settings.models import Translation as Language

def Translation(request):
    translation = Language.objects.all()
    pl = []
    for t in translation:
        pl = "{{translation." + str(t.tag)+"}}"
        print('translation', str(pl))
    print('pl: ', str(pl))
    return(pl)