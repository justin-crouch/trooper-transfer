from django.views import generic
from .models import Post

class Home(generic.TemplateView):
	""" Path view for landing page """
	template_name = 'api/index.html'

class PostList(generic.ListView):
	""" Path view for loading a list of posts, depending on thread """
	template_name = 'api/army_list.html'
	thread = 0

	def get_queryset(self):
		""" 
			Returns all posts if user profile is in the Editor group,
			otherwise load only published posts
		"""
		if(self.request.user.groups.filter(name='Editor').exists()):
			return Post.objects.filter(thread=self.thread).order_by('-created_on')

		return Post.objects.filter(status=1, thread=self.thread).order_by('-created_on')

class PostDetail(generic.DetailView):
	""" Path view for loading a single post """
	template_name = 'api/post.html'

	def get_queryset(self):
		""" 
			Allows access to post if user profile is in the Editor group,
			otherwise allow viewing if post is published
		"""
		if(self.request.user.groups.filter(name='Editor').exists()):
			return Post.objects.all()

		return Post.objects.filter(status=1)

class AboutView(generic.TemplateView):
	""" Path view for about page """
	template_name = 'api/about.html'

class ContactView(generic.TemplateView):
	""" Path view for contact page """
	template_name = 'api/contact.html'