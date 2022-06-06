from django import forms

from .models import BlogPost, Block


class BlogPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
        field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = BlogPost
        exclude = ("comm_content", "author", "blocked_user")


class BlockUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlockUserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
        field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Block
        exclude = ()
