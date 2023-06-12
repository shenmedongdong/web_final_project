from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect


# Create your views here.

def home(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'mymembers' : mymembers,
  }
  return HttpResponse(template.render(context, request))

# def search(request):
#   query = request.GET.get('query')

#   if query:
#     results = Post.objects.filter(title__contains=query)  # 검색어로 필터링된 결과 가져오기
#   else:
#     results = Post.objects.all()  # 검색어가 없을 경우 모든 결과 가져오기

#     context = {
#       'results': results,
#       'query': query,
#     }

#     return render(request, 'search.html', context)


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')  # 검색어를 가져옴

        # 외부 웹 사이트의 검색 페이지 URL로 리다이렉트
        search_url = f'https://www.pixnet.net/searcharticle?keyword={query}'
        return redirect(search_url)