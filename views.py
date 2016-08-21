from django.contrib.auth.decorators import login_required

from view.user_login import view_user_login, view_user_logins, view_user_login_password_change
from view.album import view_album, view_albums
from view.blob import view_blob, view_blobs, view_blob_add, view_blob_delete
from view.auth import view_login, view_logout, view_auth_user_add, view_change_password
from view.billing import view_billing, view_billings
from view.blog_post import view_blog_post, view_blog_posts, view_blog_post_add, view_blog_post_edit,\
    view_blog_post_delete
from view.chef import view_chef, view_chefs
from view.consumer import view_consumer, view_consumers
from view.home import view_home
from view.location import view_location, view_locations
from view.order import view_order, view_orders, view_order_add, view_order_delete
from view.post import view_post, view_posts, view_post_add, view_post_delete, view_post_edit
from view.profile_photo import view_profile_photo, view_profile_photos
from view.review import view_review, view_reviews, view_review_add, view_review_edit, view_review_delete
from view.tool import view_tools
from view.user import view_user, view_users, view_user_add, view_user_delete


# home

@login_required
def home(request):
    return view_home.home(request)


# auth

def login(request):
    return view_login.login(request)


def logout(request):
    return view_logout.logout(request)


@login_required
def auth_user_add(request):
    return view_auth_user_add.auth_user_add(request)


@login_required
def change_password(request):
    return view_change_password.change_password(request)


# user

@login_required
def users(request):
    return view_users.users(request)


@login_required
def user(request, user_id):
    return view_user.user(request, user_id)


@login_required
def user_add(request):
    return view_user_add.user_add(request)


@login_required
def user_delete(request, user_id):
    return view_user_delete.user_delete(request, user_id)


# user_login

@login_required
def user_login(request, user_login_id):
    return view_user_login.user_login(request, user_login_id)


@login_required
def user_logins(request):
    return view_user_logins.user_logins(request)


@login_required
def user_login_password_change(request, user_login_id):
    return view_user_login_password_change.user_login_password_change(request, user_login_id)


# consumer

@login_required
def consumer(request, consumer_id):
    return view_consumer.consumer(request, consumer_id)


@login_required
def consumers(request):
    return view_consumers.consumers(request)


# chef

@login_required
def chef(request, chef_id):
    return view_chef.chef(request, chef_id)


@login_required
def chefs(request):
    return view_chefs.chefs(request)


# location

@login_required
def location(request, location_id):
    return view_location.location(request, location_id)


@login_required
def locations(request):
    return view_locations.locations(request)


# billing

@login_required
def billing(request, billing_id):
    return view_billing.billing(request, billing_id)


@login_required
def billings(request):
    return view_billings.billings(request)


# profile_photo

@login_required
def profile_photo(request, profile_photo_id):
    return view_profile_photo.profile_photo(request, profile_photo_id)


@login_required
def profile_photos(request):
    return view_profile_photos.profile_photos(request)


# post

@login_required
def posts(request):
    return view_posts.posts(request)


@login_required
def post(request, post_id):
    return view_post.post(request, post_id)


@login_required
def post_add(request, user_id):
    return view_post_add.post_add(request, user_id)


@login_required
def post_delete(request, post_id):
    return view_post_delete.post_delete(request, post_id)


@login_required
def post_edit(request, post_id):
    return view_post_edit.post_edit(request, post_id)


# order

@login_required
def orders(request):
    return view_orders.orders(request)


@login_required
def order(request, order_id):
    return view_order.order(request, order_id)


@login_required
def order_add(request, post_id):
    return view_order_add.order_add(request, post_id)


@login_required
def order_delete(request, order_id):
    return view_order_delete.order_delete(request, order_id)


# album

@login_required
def album(request, album_id):
    return view_album.album(request, album_id)


@login_required
def albums(request):
    return view_albums.albums(request)


# review

@login_required
def review(request, review_id):
    return view_review.review(request, review_id)


@login_required
def reviews(request):
    return view_reviews.reviews(request)


@login_required
def review_add(request, post_id):
    return view_review_add.review_add(request, post_id)


@login_required
def review_edit(request, review_id):
    return view_review_edit.review_edit(request, review_id)


@login_required
def review_delete(request, review_id):
    return view_review_delete.review_delete(request, review_id)


# blob

@login_required
def blob(request, blob_id):
    return view_blob.blob(request, blob_id)


@login_required
def blobs(request):
    return view_blobs.blobs(request)


@login_required
def blob_add(request, album_id):
    return view_blob_add.blob_add(request, album_id)


@login_required
def blob_delete(request, blob_id):
    return view_blob_delete.blob_delete(request, blob_id)


# blog

@login_required
def blog_post(request, blog_post_id):
    return view_blog_post.blog_post(request, blog_post_id)


@login_required
def blog_posts(request):
    return view_blog_posts.blog_posts(request)


@login_required
def blog_post_add(request):
    return view_blog_post_add.blog_post_add(request)


@login_required
def blog_post_edit(request, blog_post_id):
    return view_blog_post_edit.blog_post_edit(request, blog_post_id)


@login_required
def blog_post_delete(request, blog_post_id):
    return view_blog_post_delete.blog_post_delete(request, blog_post_id)


# tools

@login_required
def tools(request):
    return view_tools.tools(request)
