from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns[
    url(r'^$', home, name='home'),
    url(r'^Article/$', views.ArticleView),
    url(r'^WordList/$', views.WordListView(selected = req.session.get('selected'))),
    url(r'^WordBank/$',WordBankView.as_view(wordbank = req.session.get('wordbank')))

    # Examples:
    # url(r'^$', 'corpus_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
