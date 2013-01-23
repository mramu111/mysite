from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),        
    url(r'^polls/home/$', 'polls.views.loginpage'),   
    url(r'^polls/login/$', 'polls.views.login'), 
    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^polls/(?P<poll_id>\d+)/detail/$', 'polls.views.detail'),    
    url(r'^polls/questioninsertpage/$', 'polls.views.insertquestionpage'),    
    url(r'^polls/addquestion/$', 'polls.views.createquestion'),   
    url(r'^polls/(?P<poll_id>\d+)/choiceinsertpage/$', 'polls.views.inserchoicepage'),   
    url(r'^polls/(?P<poll_id>\d+)/addchoice/$', 'polls.views.createchoice'),   
    
    #url(r'^admin/', include(admin.site.urls)),  
     
)