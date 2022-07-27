from django.shortcuts import redirect, render
from django.contrib import auth

def login(request):
    # request == POST
    if request.method == "POST":
    # 로그인 시키기
        username = request.POST["username"]
        # POST 안에 있는 username을 변수 username안에 담아줌
        password = request.POST["password"]
        # POST 안에 있는 password를 변수 password안에 담아줌
        user = auth.authenticate(request, username=username, password=password)  
        # auth.authenticate 메소드로 로그인 실현
        # authenticate 메소드는 username과 password에 해당하는 회원이 있다면
        # 그 회원에 해당하는 user객체 반환
        # 그렇지 않다면 none반환
        if user is not None:
            #  user 가 있다면
            auth.login(request, user)
            # request를 보낸 user를 로그인 시켜줘라
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    # request == GET 
    else:
    # login html 띄우기
        return(request, 'login.html')

def logout(request):
    auth.logout(request)
    # 로그아웃은 검증할 게 없음
    return redirect('home')
