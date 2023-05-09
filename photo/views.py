from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost
from django.db.models import Q


class IndexView(ListView):
    template_name = 'index.html'
    # 投稿日時の降順に並べる
    queryset = PhotoPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 12

    def get_queryset(self, **kwargs): # 検索機能
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET

        if q := query.get('q'):
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(comment__icontains=q)
            )

        return queryset.order_by('-posted_at')


# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsetting.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    # forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    # レンダリングするテンプレート
    template_name = "post_photo.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(httpResponseRedirect)
        return super().form_valid(form)
    

class PostSuccessView(TemplateView):
    # index.htmlをレンダリングする
    template_name = 'post_success.html'


class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 12

    def get_queryset(self):
        # self.kwargsでキーワードの辞書を取得し、categoryキーの値を取得
        category_id = self.kwargs['category']
        # filterで絞り込み
        categories = PhotoPost.objects.filter(category=category_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return categories


class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 12
    
    def get_queryset(self):
        # self.kwargsでキーワードの辞書を取得し、userキーの値を取得
        user_id = self.kwargs['user']
        # filterで絞込
        user_list = PhotoPost.objects.filter(user=user_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return user_list
    

class DetailView(DetailView):
    template_name = 'detail.html'
    model = PhotoPost


class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 12

    def get_queryset(self):
        #現在ログインしているユーザー名はHttpRequest.userに格納されている．filterで絞り込む
        queryset = PhotoPost.objects.filter(user=self.request.user).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return queryset
    

class PhotoDeleteView(DeleteView):
    #操作対象はPhotoPostモデル
    model = PhotoPost
    # photo_delete.htmlをレンダリングする
    template_name = 'photo_delete.html'
    # 処理完了後にマイページにリダイレクトする
    success_url = reverse_lazy('photo:mypage')

    def delete(self, request, *args, **kwargs):
        #スーパークラスのdelete()を実行
        return super().delete(request, *args, **kwargs)
    

class PhotoUpdateView(UpdateView):
    model = PhotoPost
    # forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    # レンダリングするテンプレート
    template_name = "post_photo.html"
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(httpResponseRedirect)
        return super().form_valid(form)