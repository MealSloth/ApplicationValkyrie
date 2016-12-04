from Chimera.models import Review, Post, Chef, Consumer, Blob, Album
from Valkyrie.view.abstract.view_single_listable import SingleListableView
from Chimera.settings import GCS_URL, PROTOCOL
from Valkyrie.form.review.form_review_edit import ReviewEditForm
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def review(request, review_id):
    review_view = ReviewView(review_id=review_id)
    response = render(request, 'page/abstract/single-listable.html', Context(review_view.get_elements()))
    return HttpResponse(response)


class ReviewView(SingleListableView):
    def __init__(self, review_id):
        current_review = Review.objects.filter(pk=review_id)
        if not current_review.values().count() > 0:
            return
        else:
            current_review = current_review[0]

        post = Post.objects.get(pk=current_review.post_id)
        blob_list = Blob.objects.filter(album=post.album)

        image = []

        if blob_list.count() > 0:
            blob = blob_list[0]
            gcs_id = blob.gcs_id
            image.append(PROTOCOL + GCS_URL + gcs_id)

        review_edit_button = [
                'fragment/modal/form/form-modal.html',                          # Modal template
                'fragment/modal/form/edit-form/review-edit-form.html',          # Form template
                ReviewEditForm({                                                # Form instance
                    'title': current_review.title,
                    'rating': current_review.rating,
                    'summary': current_review.summary,
                }),
                current_review.id,                                              # ID parameter for action
                'valkyrie-page-single-listable__review-edit-modal',             # Modal ID
                'Edit Review',                                                  # Modal title text
                'btn btn-primary',                                              # Button style
                'review-edit',                                                  # Form action
                'Save Edit',                                                    # Submit button text
                'glyphicon glyphicon-pencil',                                   # Listable button style
                'valkyrie-fragment-form__section-form',                         # Form CSS class
                '',                                                             # Form enctype
            ]

        associated_items = []

        review_delete_button = [
                'fragment/modal/delete-confirmation-modal.html',                            # Modal template
                '',                                                                         # Form template
                '',                                                                         # Form instance
                current_review.id,                                                          # ID parameter for action
                'valkyrie-page-single-listable__review-delete-modal',                       # Modal ID
                'Delete Review',                                                            # Modal title text
                'btn btn-danger',                                                           # Button style
                'review-delete',                                                            # Submit action
                'Delete Review',                                                            # Submit button text
                'glyphicon glyphicon-trash',                                                # Listable button style
                '',                                                                         # Form CSS class
                '',                                                                         # Form enctype
                '',                                                                         # Modal body header
                associated_items,                                                           # Modal body list
                'Are you sure you would like to delete this review?',                       # Modal body footer
            ]

        review_buttons = [review_edit_button, review_delete_button, ]

        id = [('Review', current_review.id, review_buttons), ]

        info = [
            ('Associated Post', post.name),
            ('Rating', current_review.rating),
            ('Title', current_review.title),
            ('Summary', current_review.summary),
            ('Time', current_review.time),
        ]

        widget = [('fragment/widget/single-listable/review-rating-widget.html', current_review.rating), ]

        id_pool = [
            ('Post ID', current_review.post.id, 'post'),
            ('Chef ID', post.chef.id, 'chef'),
        ]

        blobs = [PROTOCOL + GCS_URL, Blob.objects.filter(album_id=post.album.id)]

        kwargs = {
            'image': image,
            'id': id,
            'info': info,
            'widget': widget,
            'id_pool': id_pool,
            'blobs': blobs,
        }

        SingleListableView.__init__(
            self, **kwargs
        )
