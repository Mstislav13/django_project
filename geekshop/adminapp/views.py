from django.http import HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создать'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:users'))
    else:
        user_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'user_form': user_form,
    }
    return render(request, 'adminapp/user_create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактировать'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
    else:
        user_form = ShopUserAdminEditForm(instance=edit_user)

    context = {
        'title': title,
        'user_form': user_form,
    }
    return render(request, 'adminapp/user_update.html', context)

@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_deleted = True
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin_staff:users'))

    context = {
        'title': title,
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'категории/создать'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)

        if category_form.is_valid():
            category_form.save()

            return HttpResponseRedirect(reverse('admin_staff:categories'))
    else:
        category_form = ProductCategoryEditForm()

    context = {
        'title': title,
        'category_form': category_form,
    }
    return render(request, 'adminapp/category_create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'категории/редактировать'

    edit_form = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_form)

        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(reverse('admin_staff:category_update', args=[edit_form.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_form)

    context = {
        'title': title,
        'category_form': edit_form,
    }
    return render(request, 'adminapp/category_update.html', context)

@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        category.is_deleted = True
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin_staff:categories', args=[category.pk]))

    context = {
        'title': title,
        'category_to_delete': category,
    }

    return render(request, 'adminapp/category_delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/товар'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    pass

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    pass
