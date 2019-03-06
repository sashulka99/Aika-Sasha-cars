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


# def ourmodels_oil(request, path):
#     print('this is the first path', path)
#     print(request.path)
#     df = pd.read_csv("results-oil.csv")
#     df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
#     df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
#     choice = ' '.join(str(path).split('_'))
#     choice_oil = ','.join(choice.split('/'))
#     choice = ','.join(choice.split('/')) + ','
#     marks = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(lambda x: x.split(",")[choice.count(",")]))))
#     marks_url = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["path"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1])))))
#     spisok = []
#     for i in range(len(marks)):
#             d = {}
#             d['name'] = marks[i]
#             mark = '_'.join(marks_url[i].split(' '))
#             #mark = '/'.join(mark.split(','))
#             print('this is our mark', marks[i])
#             print(path,marks[i])
#             d['url'] = '/oil_' + mark
#             print(d['url'])
#             spisok.append(d)
#     print(spisok)
#     print("This is our choice", choice)
#     if spisok == []:
#         choice = choice_oil
#         para = (choice, *sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["oil"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1]))))))
#         # spisok.append(*sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["oil"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1]))))))
#         spisok.append(para)
#     print(spisok)
#     return render(request, "ourmodels_oil.html", context={'spisok': spisok})


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

#
# def ourmodels_dv(request, path):
#     print('this is the first path', path)
#     print(request.path)
#     df = pd.read_csv("results-dv.csv")
#     df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
#     df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
#     choice = ' '.join(str(path).split('_'))
#     choice_dv = ','.join(choice.split('/'))
#     choice = ','.join(choice.split('/')) + ','
#     marks = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(lambda x: x.split(",")[choice.count(",")]))))
#     marks_url = sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["path"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1])))))
#     spisok = []
#     for i in range(len(marks)):
#             d = {}
#             d['name'] = marks[i]
#             mark = '_'.join(marks_url[i].split(' '))
#             print('this is our mark', marks[i])
#             print(path,marks[i])
#             d['url'] = '/dvorniki_' + mark
#             print(d['url'])
#             spisok.append(d)
#     print(spisok)
#     print("This is our choice", choice)
#     if spisok == []:
#         choice = choice_dv
#         para = (choice, *sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["dvornik"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1]))))))
#         spisok.append(para)
#     print(spisok)
#     return render(request, "ourmodels_dv.html", context={'spisok': spisok})


def ourmodels(request, path):
    print('VY DALBAYBY')
    if 'oil' in path:

        print('this is the first path', path)
        print(request.path)
        df = pd.read_csv("results-oil.csv")
        df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
        df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
        # choice = ' '.join(str(path).split('_'))
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
                #mark = '/'.join(mark.split(','))
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
            # spisok.append(*sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)]==choice)]["oil"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",")+1]))))))
            spisok.append(para)
        print(spisok)
        return render(request, "ourmodels_oil.html", context={'spisok': spisok})
    elif 'dvornik' in path:
        print('this is the first path', path)
        print(request.path)
        df = pd.read_csv("results-dv.csv")
        df["path"] = df["path"].apply(lambda x: ",".join(i.strip() for i in x.split(",")))
        df["path"] = df["path"].apply(lambda x: ";".join(i for i in x.split("/")))
        # choice = ' '.join(str(path).split('_'))
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
            # para = (choice, *sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["dvornik"].apply(
            #     lambda x: ",".join(x.split(",")[0:choice.count(",") + 1]))))))

            dvorniki_list =  sorted(list(set(df[df["path"].apply(lambda x: x[:len(choice)] == choice)]["dvornik"].apply(lambda x: ",".join(x.split(",")[0:choice.count(",") + 1])))))[0]
            dvorniki_list = dvorniki_list.split(',')
            dvorniki_list[0] = choice
            spisok = dvorniki_list
            # para = (choice, dvorniki_list)
            # spisok.append(para)
            # spisok.append(dvorniki_list)
        print(spisok)
        return render(request, "ourmodels_dv.html", context={'spisok': spisok})