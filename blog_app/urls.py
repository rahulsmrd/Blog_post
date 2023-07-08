from django.urls import path
from blog_app import views

urlpatterns = [
    path("about/",views.aboutview.as_view(),name='about'),
    path('',views.postlistview.as_view(),name='post_list'),
    path('post/<pk>',views.postdetailview.as_view(),name="post_detail"),
    path('post/new/',views.postcreatview.as_view(),name="post_new"),
    path("post/update/<pk>", views.postupdateview.as_view(),name='post_update'),
    path('post/delete/<pk>', views.postdeleteview.as_view(),name='post_delete'),
    path('drafts/', views.draftlistview.as_view(),name='post_draft_list'),
    path('post/comment/<pk>', views.add_comment_to_post,name="add_comment_to_post"),
    path('comment/approve/<pk>', views.comment_approval, name="comment_approval"),
    path('comment/remove/<pk>', views.comment_remove, name="comment_remove"),
    path('post/publish/<pk>', views.post_publish, name='post_publish'),
]