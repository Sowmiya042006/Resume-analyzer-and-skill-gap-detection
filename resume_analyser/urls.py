from django.contrib import admin
from django.urls import path
from core.views import home, signup_view, login_view, logout_view, dashboard
from analyzer.views import upload_resume, results
from assessment.views import take_test
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('upload/', upload_resume, name='upload_resume'),
    path('test/<int:resume_id>/', take_test, name='take_test'),
    path('results/<int:resume_id>/<int:test_score>/', results, name='results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
