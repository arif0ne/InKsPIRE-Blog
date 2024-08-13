
from multiprocessing import context

from urllib.request import Request
from django.core import paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.urls import is_valid_path
from .models import PostModel, Category,Comment
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth.decorators import login_required
#signup
from .forms import PostModelForm,SignUpForm,UserUpdateForm,ProfileUpdateForm,PostUpdateForm,CommentForm
from django.contrib.auth import authenticate, login,logout


from django.core.paginator import Paginator






def home(request):
    posts = PostModel.objects.all()
    counts = posts.count()
    category = Category.objects.all()
    paginator = Paginator(posts, 15)  # Corrected variable name
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    if request.htmx:
        return render(request, 'store/index.html', {'posts': page_obj})
    return render(request, 'store/index.html', {'posts': page_obj,'counts':counts})






@login_required
#delete post
def post_delete(request,pd):
    post = PostModel.objects.get(id=pd)
    if request.method == "POST":
         post.delete()
         messages.success(request, "Post Delete successfully!")
         return redirect('home')
    
    context={
         }
    return render(request, 'store/post_delete.html',context)

@login_required
#post_update
def post_edit(request,pe):
    post = PostModel.objects.get(id=pe)
    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post) # " instance=post " = for show the values
        if form.is_valid():
            form.save()
            messages.success(request, "Post update successfully!")
            return redirect('product' , pk=post.id)   #there 'pk' is main product view id
             
    else:
        form = PostUpdateForm(instance=post) 
    context = {
         "post" : post,
         "form" : form,
         
     }
    return render(request,'store/post_edit.html',context) 



@login_required
#updateinfo
def update_info(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None,instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your personal info update successfully!")
            return redirect('profile')
            

    else:
        u_form =  UserUpdateForm( instance=request.user)
        p_form = ProfileUpdateForm( instance=request.user.profilemodel)


    context = {
        'u_form':u_form,
        'p_form':p_form,
        
    }
    return render(request,'users/Editinfo.html',context) 


@login_required
def profile(request):
    posts = PostModel.objects.filter(author=request.user)
    
    return render(request,'users/profile.html',{'posts':posts}) 





def sign_in(request):
	return render(request,'users/signin.html')


#signup
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registered successfully!")
            return redirect('editinfo')
        else:
            messages.success(request,"whoops ! show  problem! check password 8 character true!")
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = SignUpForm()  # Initialize the form object
        return render(request, 'users/signup.html', {'form': form})
    

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')





def search(request):
    if request.method == 'POST':  # Corrected the case of 'POST'
        searched = request.POST.get('searched')  # Corrected retrieving data from request
        prods = PostModel.objects.filter(
            Q(title__icontains=searched) |
            Q(description__icontains=searched) |
            Q(category__name__icontains=searched) |  # Added missing comma
            Q(author__username__icontains=searched)  # Changed to username, adapt as needed
        )
        
        if not prods:
            messages.success(request, "Hmm, Your Searched Item Isn't in Our Blog. Keep Scrolling for More!")  # Corrected error message
            return redirect('blog')
        else:
            return render(request, 'store/search.html', {'searched': searched, 'prods': prods})
    else:
        return render(request, 'store/search.html')



@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if request.user.is_authenticated:  # Debug statement
                instance.author = request.user
                instance.save()
                messages.success(request, 'Post added successfully')
                return redirect('home')
            else:
                return redirect('signin')  # Debug statement
    else:
        form = PostModelForm()

    return render(request, 'store/add-post.html', {'form': form})





def about(request):
	return render(request,'store/about.html')

def blog(request):
	posts = PostModel.objects.all()
	return render(request,'store/blog.html',{'posts':posts})




def category(request,foo):
    # postt = PostModel.objects.all()
    # Replace hypens with space
    # foo = foo.replace('-',' ')
    
    try:
        category = Category.objects.get(name=foo)
        posts = PostModel.objects.filter(category=category)
        
        return render(request,'store/category-posts.html',{'posts': posts,'category':category})
        
        
    except:
        messages.success(request,("that category does't work"))
        return redirect('home')





def contact(request):
	return render(request,'store/contact.html')





def service(request):
	return render(request,'store/services.html')






def product(request,pk):
    prodviews = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.post = prodviews
            instance.save()
            messages.success(request,"comment added on the post..... thanku")
            return redirect('product' , pk=prodviews.id)
            
    else:
        c_form = CommentForm() 
    return render(request,'store/productview.html',{'post':prodviews,'form':c_form})
