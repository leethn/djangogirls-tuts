from django.http import HttpResponse
'''
Detail view를 만들어봅니다
    1. view에 post_detail함수 추가
        post_detail은 인자로post_id를 받는다
    2. urls.py에 해당 view와 연결하는 url을 추가
        정규표현식으로 패턴네임 post_id이름을 갖는 숫자1개이상의 패턴을 등록
    3. post_detail뷰가 원하는 url에서 잘 출력되는지 확인후 (stub 메서드 사용)
        get 쿼리셋을 사용해서 (Post.objects.get(...))
        id값이 인자로 전달된 post_id와 같은 Post객체 context에 담아
        post-detail.html을 render한 결과를 리턴
    4. 템플릿에 post-detail.html을 만들고,
        인자로 전달된 Post객체의 title, content, created_date, published date를 출력
'''

from django.shortcuts import render , get_object_or_404
from django.utils import timezone

from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    # try:
    # ORM을 이용해서 id가 전달받은 post_id와 일치하는 Post객체를  post변수에 할당
    post = get_object_or_404(Post, id=post_id)

    except Post.DoesNotExits as e:
        # De


    context = {
            'post': post,
        }
    return render(request, 'blog/post-detail.html', context)
