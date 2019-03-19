from django.shortcuts import render
import pandas as pd


def index(request):
    return render(request, "index.html")


def about_pr(request):
    return render(request, "about_pr.html")


def feedback(request):
    return render(request,"feedback.html")


def katalog_oil(request):
    df = pd.read_csv("results-oil.csv")
    df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
    df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
    choice = ""
    marks = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(lambda x: x.split(",")[choice.count(",")]))))
    spisok = []
    for mark in marks:
        d = {}
        d['name'] = mark
        mark = '_'.join(mark.split(' '))
        d['url'] = '/oil_' + mark
        spisok.append(d)
    return render(request, "katalog_oil.html", context={"spisok": spisok})


def katalog_dv(request):
    df = pd.read_csv("results-dv.csv")
    df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
    df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
    choice = ""
    marks = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(lambda x: x.split(",")[choice.count(",")]))))
    spisok = []
    for mark in marks:
        d = {}
        d['name'] = mark
        mark = '_'.join(mark.split(' '))
        d['url'] = '/dvorniki_' + mark
        spisok.append(d)
    return render(request, "katalog_dv.html", context={"spisok": spisok})


def katalog_fif(request):
    df = pd.read_csv("results-fif.csv")
    df["Path"] = df["Path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
    df["Path"] = df["Path"].apply(lambda x: ";".join(i for i in x.split("/")))
    choice = ""
    marks = sorted(list(set(df[df["Path"].apply(lambda x: x[:len(choice)] == choice)]["Path"].apply(lambda x: x.split(",")[choice.count(",")]))))
    spisok = []
    for mark in marks:
        d = {}
        d['name'] = mark
        mark = '_'.join(mark.split(' '))
        d['url'] = '/filters_' + mark
        spisok.append(d)
    return render(request, "katalog_fif.html", context={"spisok": spisok})


def ourmodels(request, path):

    if 'oil' in path:
        print('this is the first path', path)
        print(request.path)
        df = pd.read_csv("results-oil.csv")
        df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
        df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
        choice = str(path).split('_')
        choice.remove(choice[0])
        choice = ' '.join(choice)
        choice_oil = ','.join(choice.split('/'))
        choice = ','.join(choice.split('/')) + ','
        marks = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(lambda x: x.split(",")[choice.count(",")]))))
        marks_url = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["path"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1])))))
        spisok = []
        for i in range(len(marks)):
                d = {}
                d['name'] = marks[i]
                mark = '_'.join(marks_url[i].split(' '))
                print('this is our mark', marks[i])
                print(path,marks[i])
                d['url'] = '/oil_' + mark
                print(d['url'])
                spisok.append(d)
        print(spisok)
        print("This is our choice", choice)
        if spisok == []:
            choice = choice_oil
            para = (choice, *sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["oil"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1]))))))
            spisok.append(para)
        print(spisok)
        return render(request, "ourmodels_oil.html", context={'spisok': spisok})

    elif 'dvornik' in path:
        print('this is the first path', path)
        print(request.path)
        df = pd.read_csv("results-dv.csv")
        df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
        df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
        choice = str(path).split('_')
        choice.remove(choice[0])
        choice = ' '.join(choice)
        choice_dv = ','.join(choice.split('/'))
        choice = ','.join(choice.split('/')) + ','
        marks = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(
            lambda x: x.split(",")[choice.count(",")]))))
        marks_url = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(
            lambda x: ",".join(x.split(",")[0:choice.count(",") + 1])))))
        spisok = []
        for i in range(len(marks)):
            d = {}
            d['name'] = marks[i]
            mark = '_'.join(marks_url[i].split(' '))
            print('this is our mark', marks[i])
            print(path, marks[i])
            d['url'] = '/dvorniki_' + mark
            print(d['url'])
            spisok.append(d)
        print(spisok)
        print("This is our choice", choice)
        if spisok == []:
            choice = choice_dv
            dvorniki_list =  sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["dvornik"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",") + 1])))))[0]
            dvorniki_list = dvorniki_list.split(',')
            dvorniki_list[0] = choice
            spisok = dvorniki_list
        print(spisok)
        return render(request, "ourmodels_dv.html", context={'spisok': spisok})

    elif 'filters' in path:
        print('this is the first path', path)
        print(request.path)
        df = pd.read_csv("results-fif.csv")
        df["Path"] = df["Path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
        df["Path"] = df["Path"].apply(lambda x: ".".join(i for i in x.split("/")))
        choice = str(path).split('_')
        choice.remove(choice[0])
        choice = ' '.join(choice)
        choice_fif = ','.join(choice.split('/'))
        choice = ','.join(choice.split('/')) + ','
        marks = sorted(list(set(df[df["Path"].apply(lambda x: x[:len(choice)] == choice)]["Path"].apply(
            lambda x: x.split(",")[choice.count(",")]))))
        marks_url = sorted(list(set(df[df["Path"].apply(lambda x: x[:len(choice)] == choice)]["Path"].apply(
            lambda x: ",".join(x.split(",")[0:choice.count(",") + 1])))))
        spisok = []
        for i in range(len(marks)):
            d = {}
            d['name'] = marks[i]
            mark = '_'.join(marks_url[i].split(' '))
            print('this is our mark', marks[i])
            print(path, marks[i])
            d['url'] = '/filters_' + mark
            print(d['url'])
            spisok.append(d)
        print(spisok)
        print("This is our choice", choice)
        if spisok == []:
            new_d = {}
            choice = choice_fif
            new_d['name'] = choice
            new_d['oil'] = sorted(list(set(df[df["Path"].apply(lambda x: x[:len(choice)] == choice)]["OIL"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",") + 1])))))[0]
            new_d['air'] = sorted(list(set(df[df["Path"].apply(lambda x: x[:len(choice)] == choice)]["AIR"].apply(
                lambda x: ",".join(x.split(",")[0:choice.count(",") + 1])))))[0]
            new_d['fuel'] = sorted(list(set(df[df["Path"].apply(lambda x: x[:len(choice)] == choice)]["FUEL"].apply(
                lambda x: ",".join(x.split(",")[0:choice.count(",") + 1])))))[0]
            new_d['cabin'] = sorted(list(set(df[df["Path"].apply(lambda x: x[:len(choice)] == choice)]["CABIN"].apply(
                lambda x: ",".join(x.split(",")[0:choice.count(",") + 1])))))[0]
            spisok.append(new_d)
        print(spisok)
        return render(request, "ourmodels_fif.html", context={'spisok': spisok})