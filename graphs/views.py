from django.shortcuts import render
from django.http import HttpResponse
from graphs.models import posters, papers
import numpy as np
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# Create your views here.

def posterimage(request):
    poster = posters.objects.all()

    venue,poster_year2017,poster_year2018,poster_year2019,poster_year2020 =[],[],[],[],[]

    for a in poster:
        venue = venue +[a.Venue]
        poster_year2017 = poster_year2017 + [a.YEAR2017]
        poster_year2018 = poster_year2018 + [a.YEAR2018]
        poster_year2019 = poster_year2019 + [a.YEAR2019]
        poster_year2020 = poster_year2020 + [a.YEAR2020]

    
    barwidth = 3.0/(len(venue) + 2)

    r1 = np.arange(len(poster_year2017))
    r2 =[x + barwidth for x in r1]
    r3 = [ y + barwidth for y in r2]
    r4 = [z + barwidth for z in r3]

    plt.bar(r1,poster_year2017, width = barwidth, color = 'blue', label="2017")
    plt.bar(r2,poster_year2018, width = barwidth, color = 'green',label="2018")
    plt.bar(r3,poster_year2019, width = barwidth, color = 'yellow',label="2019")
    plt.bar(r4,poster_year2020, width = barwidth, color = 'red', label="2020")
    
    plt.xticks([r + (barwidth*2.5) for r in range(len(poster_year2017))],venue)
    plt.ylabel("No Of Posters")

    colors = ['blue','green','yellow','red']
    lines = [Line2D([0], [0], color=c, linewidth=4) for c in colors]
    labels = ['2017','2018','2019','2020']
    plt.legend(lines,labels)

    plt.xticks(rotation=90)
    plt.tight_layout()

    response = HttpResponse(content_type ="image/jpg")
    plt.savefig(response,format="jpg")

    return response

def paperimage(request):
    paper = papers.objects.all()

    venue,paper_year2017,paper_year2018,paper_year2019,paper_year2020 =[],[],[],[],[]

    for a in paper:
        venue = venue +[a.Venue]
        paper_year2017 = paper_year2017 + [a.YEAR2017]
        paper_year2018 = paper_year2018 + [a.YEAR2018]
        paper_year2019 = paper_year2019 + [a.YEAR2019]
        paper_year2020 = paper_year2020 + [a.YEAR2020]

    
    barwidth = 3.0/(len(venue) + 2)

    r1 = np.arange(len(paper_year2017))
    r2 =[x + barwidth for x in r1]
    r3 = [ y + barwidth for y in r2]
    r4 = [z + barwidth for z in r3]

    plt.bar(r1,paper_year2017, width = barwidth, color = 'blue', label="2017")
    plt.bar(r2,paper_year2018, width = barwidth, color = 'green',label="2018")
    plt.bar(r3,paper_year2019, width = barwidth, color = 'yellow',label="2019")
    plt.bar(r4,paper_year2020, width = barwidth, color = 'red', label="2020")
    
    plt.xticks([r + (barwidth*2.5) for r in range(len(paper_year2017))],venue)
    plt.ylabel("No Of Papers")

    colors = ['blue','green','yellow','red']
    lines = [Line2D([0], [0], color=c, linewidth=4) for c in colors]
    labels = ['2017','2018','2019','2020']
    plt.legend(lines,labels)

    plt.xticks(rotation=90)
    plt.tight_layout()

    response = HttpResponse(content_type ="image/jpg")
    plt.savefig(response,format="jpg")

    return response