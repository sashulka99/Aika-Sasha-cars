from django.shortcuts import render
import pandas as pd

# Create your views here.

def index(request):
    return render(request, "index.html")

def katalog(request):
    df = pd.read_csv("results.csv")
    df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
    df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
    choice = ""
    marks = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(lambda x: x.split(",")[choice.count(",")]))))
    spisok = []
    for mark in marks:
        d = {}
        d['name'] = mark
        mark = '_'.join(mark.split(' '))
        d['url'] = '/' + mark
        spisok.append(d)
    #spisok = [{"url":"/BMW_X5", "name":'BMW'}, {"url":"/Mers/","name":"Mercedes"}]

    #print(path)
    return render(request, "katalog.html", context={"spisok": spisok})


def ourmodels(request, path):
    print('this is the first path', path)
    print(request.path)
    #print('AIKAAAAA')
    #choice = ' '.join(str(request.path).split('_'))
    #print('sasha', choice)
    #choice = choice.strip('/') + ','
    #print('aika', choice)
    #choice ="BMW,"
    df = pd.read_csv("results.csv")
    df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
    df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
    choice = ' '.join(str(path).split('_'))
    choice_oil = ','.join(choice.split('/'))
    choice = ','.join(choice.split('/')) + ','
    marks = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(lambda x: x.split(",")[choice.count(",")]))))
    marks_url = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["path"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1])))))
    spisok = []
    '''
    for mark in marks:
        d = {}
        d['name'] = mark
        mark = '_'.join(mark.split(' '))
        print('this is our mark', mark)
        print("this is our path for mark",path)
        d['url'] =  '/' + mark
        print( "this is our url for list",d['url'])
        spisok.append(d)
    print(spisok)
    '''
    for i in range(len(marks)):
            d = {}
            d['name'] = marks[i]
            mark = '_'.join(marks_url[i].split(' '))
            #mark = '/'.join(mark.split(','))
            print('this is our mark', marks[i])
            print(path,marks[i])
            d['url'] = '/' + mark
            print(d['url'])
            spisok.append(d)
    print(spisok)
    print("This is our choice", choice)
    if spisok == []:
        choice = choice_oil
        para = (choice, *sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["oil"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1]))))))
        # spisok.append(*sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["oil"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1]))))))
        spisok.append(para)
    print(spisok)
    return render(request, "ourmodels.html", context={'spisok': spisok})


def about_pr(request):
    return render(request, "about_pr.html")

def feedback(request):
    return render(request,"feedback.html")
