import math
from corpus.models import *
from numpy import power,arctan
import numpy

def gauss(x, *p):
    A, mu, sigma = p
    return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))

def update_difficulty_all():
 easybase=6e-4
 diffbase=1e-7
 factor=10/math.log(diffbase/easybase,10)
 coeff=[460.62127153, 5.56339237, 2.51568407]

 diff=[]
 calc_diff=[]
 for word in Word.objects.all():
    if float(word.ngramsfreq) > easybase:
        word.difficulty=0
        word.calc_diff=0
    else:
        word.difficulty=math.log(float(word.ngramsfreq)/easybase,10)*factor
        x=word.difficulty
#        word.calc_diff=x/float(word.ngramsfreq)/gauss(x,*coeff)
        word.calc_diff=x*(arctan(x-8)+1.447)
        #word.calc_diff=word.difficulty*(((x-5)/abs(x-8))*power(abs(x-5),1.0/5.5)+1.38)*2
   # if(word.difficulty<5):
#        print word.difficulty, word.calc_diff
    word.save()
    diff.append(word.difficulty)
    calc_diff.append(word.calc_diff)
    print word
    

    
    
#hist, bin_edges = numpy.histogram(data, density=True)
#bin_centres = (bin_edges[:-1] + bin_edges[1:])/2

# Define model function to be used to fit to the data above:
#def gauss(x, *p):
#    A, mu, sigma = p
#    return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))

# p0 is the initial guess for the fitting coefficients (A, mu and sigma above)
#p0 = [1., 0., 1.]

#coeff, var_matrix = curve_fit(gauss, bin_centres, hist, p0=p0)

# Get the fitted curve
#hist_fit = gauss(bin_centres, *coeff)
