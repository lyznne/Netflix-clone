from django.contrib import admin
from Netflix.models import Movie, Category, Tag
from django.utils.html import format_html 


# to show the preview and video 
class MovieAdmin(admin.ModelAdmin):

    def  preview(self, movie):
        """render  preview image as html image """
        return format_html(f'<img style="height: 20px" src="/media/{movie.preview_image} " />')

    def video(self, movie):
        """ render movie video as html image """
        return format_html(
            f"""
            <video width="320" height="240" controls>
            <source_src="/media/{movie.file}" type="video/mp4">
            your browser does not support the video tag.
            </video>"""
        )

    preview.short_description = 'Movie Image'
    video.short_descriprion = 'Movie Video'
    list_display = ["name", "preview", "video", "description"]

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
admin.site.register(Tag)