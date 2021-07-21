from django.http import HttpResponseRedirect
from django.urls import reverse

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test

from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView

class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'
    paginate_by = 3

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        context['title'] = 'админка/пользователи'
        return context

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', context)

class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    context_object_name = 'user_form'
    template_name = 'adminapp/user_create.html'
    success_url = '/admin_staff/users/read'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context['title'] = 'пользователи/создать'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     title = 'пользователи/создать'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'user_form': user_form,
#     }
#     return render(request, 'adminapp/user_create.html', context)

class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    context_object_name = 'user_form'
    template_name = 'adminapp/user_update.html'
    success_url = '/admin_staff/users/read'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data()
        context['title'] = 'пользователи/редактировать'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     title = 'пользователи/редактировать'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin_staff:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#
#     context = {
#         'title': title,
#         'user_form': edit_form,
#     }
#     return render(request, 'adminapp/user_update.html', context)

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    context_object_name = 'user_to_delete'
    success_url = '/admin_staff/users/read'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data()
        context['title'] = 'пользователи/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_delete = True
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.is_deleted = True
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin_staff:users'))
#
#     context = {
#         'title': title,
#         'user_to_delete': user,
#     }
#
#     return render(request, 'adminapp/user_delete.html', context)

class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    context_object_name = 'objects'
    paginate_by = 4

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['title'] = 'админка/категории'
        return context

    def get_queryset(self):
        return ProductCategory.objects.all()

# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     context = {
#         'title': title,
#         'objects': categories_list,
#     }
#
#     return render(request, 'adminapp/categories.html', context)



class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    form_class = ProductCategoryEditForm
    success_url = '/admin_staff/categories/read'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        context['title'] = 'категории/создать'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = 'категории/создать'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#
#         if category_form.is_valid():
#             category_form.save()
#
#             return HttpResponseRedirect(reverse('admin_staff:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#
#     context = {
#         'title': title,
#         'category_form': category_form,
#     }
#     return render(request, 'adminapp/category_create.html', context)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    form_class = ProductCategoryEditForm
    success_url = '/admin_staff/categories/read'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data()
        context['title'] = 'категории/редактировать'
        return context

# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = 'категории/редактировать'
#
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#
#         if edit_form.is_valid():
#             edit_form.save()
#
#             return HttpResponseRedirect(reverse('admin_staff:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = ProductCategoryEditForm(instance=edit_category)
#
#     context = {
#         'title': title,
#         'category_form': edit_form,
#     }
#     return render(request, 'adminapp/category_update.html', context)

class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    context_object_name = 'category_to_delete'
    success_url = '/admin_staff/categories/read'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data()
        context['title'] = 'категории/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_delete = True
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = 'категории/удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.is_deleted = True
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('admin_staff:categories'))
#
#     context = {
#         'title': title,
#         'category_to_delete': category,
#     }
#
#     return render(request, 'adminapp/category_delete.html', context)

class ProductsListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'
    context_object_name = 'objects'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        category = get_object_or_404(ProductCategory, pk=self.kwargs.get('pk'))
        context.update({'category': category})
        return context

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs.get('pk'))

# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     title = 'админка/товар'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     context = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'adminapp/products.html', context)

# class ProductCreateView(CreateView):
#     model = Product
#     template_name = 'adminapp/product_create.html'
#     form_class = ProductEditForm
#     success_url = '/'
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ProductCreateView, self).get_context_data()
#         context['title'] = 'товары/создать'
#         return context

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'товары/создать'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin_staff:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    context = {
        'title': title,
        'update_form': product_form,
        'category': category,
    }
    return render(request, 'adminapp/product_create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    title = 'товары/подробнее'

    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': title,
        'product': product,
    }

    return render(request, 'adminapp/product_read.html', context)

# class ProductUpdateView(UpdateView):
#     model = Product
#     template_name = 'adminapp/product_update.html'
#     form_class = ProductEditForm
#     success_url = '/'
#
#     @method_decorator(user_passes_test(lambda u: u.is_superuser))
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ProductUpdateView, self).get_context_data()
#         context['title'] = 'товары/редактировать'
#         return context

@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    title = 'товары/редактировать'

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_staff:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    context = {
        'title': title,
        'update_form': edit_form,
        'category': edit_product.category,
        'product': edit_product,
    }
    return render(request, 'adminapp/product_update.html', context)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    context_object_name = 'product_to_delete'
    success_url = '/admin_staff/categories/read'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data()
        context['title'] = 'товары/удаление'
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_delete = True
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def product_delete(request, pk):
#     title = 'товары/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_deleted = True
#         product.save()
#         return HttpResponseRedirect(reverse('admin_staff:products', args=[product.category.pk]))
#
#     context = {
#         'title': title,
#         'product_to_delete': product
#     }
#
#     return render(request, 'adminapp/product_delete.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'
