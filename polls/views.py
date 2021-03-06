# Create your views here.
from django.http import HttpResponse

from django.template import Context, loader
from polls.models import Poll
#from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from polls.models import Choice, Poll,User
from django.utils import timezone


#def index(request):
    #return HttpResponse("Hello, world. You're at the poll index.")

#def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]    
    t = loader.get_template('index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(t.render(c))


#def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})


#def detail(request, poll_id):
    #return HttpResponse("You're looking at poll %s." % poll_id)
    
    
#def detail(request, poll_id):
    #try:
        #p = Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist:
        #raise Http404
    #return render_to_response('polls/detail.html', {'poll': p})
    
    
    
    

#def detail(request, poll_id):
    #p = get_object_or_404(Poll, pk=poll_id)
    #return render_to_response('details.html', {'poll': p})
    
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    #import pdb;pdb.set_trace()
    return render_to_response('detail.html', {'poll': p},
                               context_instance=RequestContext(request))    


#def results(request, poll_id):
#    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('results.html', {'poll': p})

#def vote(request, poll_id):
    #return HttpResponse("You're voting on poll %s." % poll_id)



def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
    
    
def choice(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
    
def insertquestionpage(request):    
    return render_to_response('insertquestion.html')

def inserchoicepage(request,poll_id):   
    p=poll_id
    return render_to_response('insertchoice.html',
                              {'poll': p},
                              context_instance=RequestContext(request)                          
                                                      )

def loginpage(requset):
    return render_to_response('loginpage.html')
    

def createquestion(request):    
    p=Poll()
    p.question=request.GET['question']
    #p.pub_date=request.getparameter('pub_date')
    p.pub_date=timezone.now()
    p.save()
    return index(request)

def createchoice(request,poll_id):   
    p = get_object_or_404(Poll, pk=poll_id)        
    p.choice_set.create(choice=request.POST['choice'],votes=request.POST['votes'])
    p.save()
    return index(request)

def login(request):
    user=None
    import pdb;pdb.set_trace()
    username=request.GET['username']
    password=request.GET['password']
    
    user=User.objects.filter(username=username,password=password)
    if user:        
        return index(request)
    else:
        return render_to_response('loginpage.html')
    


