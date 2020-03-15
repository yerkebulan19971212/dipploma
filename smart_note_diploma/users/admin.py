from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

# from smart_note_diploma.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    # form = UserChangeForm
    # add_form = UserCreationForm
    # fieldsets = (("User", {"fields": ("email",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["email", "is_superuser"]
    search_fields = ["email"]
