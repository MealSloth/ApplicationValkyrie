from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context

from Valkyrie.form.auth.form_auth_user_add import AuthUserAddForm
from Valkyrie.form.blog_post.form_blog_post_add import BlogPostAddForm


def tools(request):
    tools_view = ToolsView()
    response = render(request, 'page/tool/tools.html', Context({'sections': tools_view.get_elements()}))
    return HttpResponse(response)


class ToolsView:
    sections = []

    def __init__(self):
        auth_user_add_button = [
                'fragment/modal/form/form-modal.html',                      # Modal template
                'fragment/modal/form/add-form/auth-user-add-form.html',     # Form template
                AuthUserAddForm(),                                          # Form instance
                '',                                                         # ID parameter for action
                'valkyrie-page-single-listable__auth-user-add-modal',       # Modal ID
                'Add an Auth User',                                         # Modal title text
                'btn btn-primary',                                          # Button style
                'auth-user-add',                                            # Form action
                'Add an Auth User',                                         # Submit button text
                '',                                                         # Listable button style
                'valkyrie-fragment-form__section-form',                     # Form CSS class
                '',                                                         # Form enctype
        ]

        auth = ['Authentication',
                [
                    auth_user_add_button,
                ],
                ]

        self.sections = [auth, ]

    def get_elements(self):
        return self.sections
