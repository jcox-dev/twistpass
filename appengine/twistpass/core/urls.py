from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'twistpass.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^generator/$', 'generator', name='generator'),
    url(r'^how-it-works/$', 'how_it_works', name='how_it_works'),

    url(r'^feedback/$', 'feedback', name='feedback'),
    url(r'^send-love/$', 'send_love', name='send_love'),
    url(r'^tips/$', 'tips', name='tips'),
    # url(r'^learn/$', 'learn', name='learn'),

    url(r'^keep-alive/$', 'keep_alive', name='keep_alive'),
)
