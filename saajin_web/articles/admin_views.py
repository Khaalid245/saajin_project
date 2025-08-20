from django.shortcuts import render

def admin_login(request):
    return render(request, 'saajin-admin/login.html')

def admin_dashboard(request):
    return render(request, 'saajin-admin/dashboard.html')

def admin_articles(request):
    return render(request, 'saajin-admin/articles.html')

def admin_categories(request):
    return render(request, 'saajin-admin/categories.html')

def admin_comments(request):
    return render(request, 'saajin-admin/comments.html')

def home_page(request):
    return render(request, 'public/index.html')

def article_detail(request, id):
    """
    Public view for showing a single article detail page.
    It simply returns the HTML template which will fetch data from the API.
    """
    return render(request, 'public/article.html')

def about(request):
    return render(request, 'public/about.html')

def contact(request):
    return render(request, 'public/contact.html')

def all_articles(request):
    return render(request, 'public/articles_list.html')



