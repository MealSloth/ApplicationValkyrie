from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns
import views


regex_uuid = "[0-9a-fA-F]{8}\-(?:[0-9a-fA-F]{4}\-){3}[0-9a-fA-F]{12}"


urlpatterns = patterns(
    '',


    # Home
    url(r'^$', views.home, name='home'),


    # Auth
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth-user-add/$', views.auth_user_add, name='auth-user-add'),
    url(r'^change-password/$', views.change_password, name='change-password'),


    # Multi listables
    url(r'^users/$', views.users, name='users'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^orders/$', views.orders, name='orders'),
    url(r'^user-logins/$', views.user_logins, name='user-logins'),
    url(r'^consumers/$', views.consumers, name='consumers'),
    url(r'^chefs/$', views.chefs, name='chefs'),
    url(r'^locations/$', views.locations, name='locations'),
    url(r'^billings/$', views.billings, name='billings'),
    url(r'^profile-photos/$', views.profile_photos, name='profile-photos'),
    url(r'^albums/$', views.albums, name='albums'),
    url(r'^blobs/$', views.blobs, name='blobs'),
    url(r'^blog-posts/$', views.blog_posts, name='blog-posts'),
    url(r'^reviews/$', views.reviews, name='reviews'),

    # Single listables
    url(r'^user/(%s)/$' % regex_uuid, views.user, name='user'),
    url(r'^post/(%s)/$' % regex_uuid, views.post, name='post'),
    url(r'^order/(%s)/$' % regex_uuid, views.order, name='order'),
    url(r'^user-login/(%s)/$' % regex_uuid, views.user_login, name='user-login'),
    url(r'^consumer/(%s)/$' % regex_uuid, views.consumer, name='consumer'),
    url(r'^chef/(%s)/$' % regex_uuid, views.chef, name='chef'),
    url(r'^location/(%s)/$' % regex_uuid, views.location, name='location'),
    url(r'^billing/(%s)/$' % regex_uuid, views.billing, name='billing'),
    url(r'^profile-photo/(%s)/$' % regex_uuid, views.profile_photo, name='profile-photo'),
    url(r'^album/(%s)/$' % regex_uuid, views.album, name='album'),
    url(r'^blog-post/(%s)/$' % regex_uuid, views.blog_post, name='blog-post'),
    url(r'^blob/(%s)/$' % regex_uuid, views.blob, name='blob'),
    url(r'^review/(%s)/$' % regex_uuid, views.review, name='review'),


    # Add Forms
    url(r'^user-add/$', views.user_add, name='user-add'),
    url(r'^post-add/(%s)/$' % regex_uuid, views.post_add, name='post-add'),
    url(r'^blob-add/(%s)/$' % regex_uuid, views.blob_add, name='blob-add'),
    url(r'^order-add/(%s)/$' % regex_uuid, views.order_add, name='order-add'),
    url(r'^blog-post-add/$', views.blog_post_add, name='blog-post-add'),
    url(r'^review-add/(%s)/$' % regex_uuid, views.review_add, name='review-add'),

    # Edit Forms
    url(r'^post-edit/(%s)/$' % regex_uuid, views.post_edit, name='post-edit'),
    url(r'^blog-post-edit/(%s)/$' % regex_uuid, views.blog_post_edit, name='blog-post-edit'),
    url(r'^user-login-password-change/(%s)/$' % regex_uuid, views.user_login_password_change, name='user-login-password-change'),
    url(r'^review-edit/(%s)/$' % regex_uuid, views.review_edit, name='review-edit'),

    # Delete Forms
    url(r'^user-delete/(%s)/$' % regex_uuid, views.user_delete, name='user-delete'),
    url(r'^post-delete/(%s)/$' % regex_uuid, views.post_delete, name='post-delete'),
    url(r'^blob-delete/(%s)/$' % regex_uuid, views.blob_delete, name='blob-delete'),
    url(r'^order-delete/(%s)/$' % regex_uuid, views.order_delete, name='order-delete'),
    url(r'^blog-post-delete/(%s)/$' % regex_uuid, views.blog_post_delete, name='blog-post-delete'),
    url(r'^review-delete/(%s)/$' % regex_uuid, views.review_delete, name='review-delete'),


    # Tools
    url(r'^tools/$', views.tools, name='tools'),

) + staticfiles_urlpatterns()
