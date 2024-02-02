from django.views import generic

from .models import Post

class Home(generic.TemplateView):
	template_name = 'api/index.html'

class PostList(generic.ListView):
	template_name = 'api/army_list.html'
	thread = 0

	def get_queryset(self):
		if(self.request.user.groups.filter(name='Editor').exists()):
			return Post.objects.filter(thread=self.thread).order_by('-created_on')

		return Post.objects.filter(status=1, thread=self.thread).order_by('-created_on')

class PostDetail(generic.DetailView):
	template_name = 'api/post.html'

	def get_queryset(self):
		if(self.request.user.groups.filter(name='Editor').exists()):
			return Post.objects.all()

		return Post.objects.filter(status=1)

class AboutView(generic.TemplateView):
	template_name = 'api/about.html'
