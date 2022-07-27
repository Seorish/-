from django.shortcuts import render, redirect, get_object_or_404
from django.urls import is_valid_path
from .forms import PostForm, CommentForm
from .models import Post,Comment
# Create your views here.

def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts' : posts})


def postcreate(request):
    # request method 가 POST일 경우
    if request.method == 'POST' or request.method == "FILES":
        # form 변수에 입력값 담기
        form = PostForm(request.POST , request.FILES)
        # 유효한 값이 담겨있다면 (유효성 검사)
        if form.is_valid():
            # 저장해라
            form.save()
            # 저장 후 home으로 redirect
            return redirect('home')
    # request method 가 GET일 경우
    else:
        # form 입력 html 띄우기
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})


def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail' : post_detail},{'comment_form':comment_form})
 
# 댓글 작성하고 submit 할 때 이동하는 url 이므로
# 댓글 저장하는 기능을 함
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    # CommentForm에서 POST 요청 보낸 것을 filled_form이라는 변수에 넣어줌
    if filled_form.is_valid():
        filled_form.save(commit=False)
        # 어떤 게시물에 대한 댓글인지 정해지지 않았으므로 일단 저장하지 않고
        finished_form.post = get_object_or_404(Post, pk = post_id)
        # finished_form의 post에 get_object_or_404 -> 어떤 게시물에 대한 댓글인 지 확인 후
        finished_form.save()   
    return redirect('detail.html', post_id)
    # 내가 댓글을 단 detail.html로 이동한다.

    # 댓글 기능에서 중요한 점
    # 1. models.py 에서 ForeignKey
    # 2. 일단 저장하지 않고(commit=False) 마땅히 채워야 할 정보 저장한 후 save
