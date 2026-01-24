"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from relationship_app import views
from relationship_app.views import LibraryDetailView



urlpatterns = [
    path("", include("relationship_app.urls")),
    path('admin/', admin.site.urls),
    path("books/", views.list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("admin-role/", views.admin_view, name="admin-view"),
    path("librarian-role/", views.librarian_view, name="librarian-view"),
    path("member-role/", views.member_view, name="member-view"),
    path("books/add_book/", views.add_book, name="add-book"),
    path("books/<int:pk>/edit_book/", views.edit_book, name="edit-book"),
    path("books/<int:pk>/delete_book/", views.delete_book, name="delete-book"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
