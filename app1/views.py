from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import bookdetails, borrow
from django.contrib import messages
from datetime import datetime, timedelta

def subtract_copies(copies_borrowed, book_name):
    try:
        book = get_object_or_404(bookdetails, name=book_name)
        copies_borrowed = int(copies_borrowed)
        if book.copies >= copies_borrowed:
             book.copies -= copies_borrowed
             book.save()
             return True
        else:
             return False
    except ValueError:
         return False

def c_admin(request):
    books = bookdetails.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bookentry(request):
    if not request.session.get('admin_logged_in', False):
        return redirect('admin')
    if request.method == 'POST':
        name = request.POST.get('bname')
        author = request.POST.get('author')
        copies = request.POST.get('copies')
        genre = request.POST.get('genre')
        shelf = request.POST.get('shelf')
        level = request.POST.get('level')
        column = request.POST.get('column')

        if name and author and copies:
            book = bookdetails(name=name, author=author, copies=copies, genre=genre, shelf=shelf, level=level, column=column)
            book.save()
            messages.success(request, "Book added successfully!")
        else:
            messages.error(request, "Please fill in all fields!")
    return render(request, 'bookentry.html')

def adm_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        if email == 'kingston@lib.com' and pass1 == 'admin':
          request.session['admin_logged_in'] = True  #Set the session variable
          return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!!!")
    return render(request, 'admin.html')

def adm_logout(request):
    try:
         del request.session['admin_logged_in']
    except KeyError:
         pass # If the key is not present just ignore
    return redirect('admin') # Redirect to admin page after logout

def borrow1(request):
    book_name = request.GET.get('book_name') #get book_name regardless of the method
    if request.method == 'POST':
        #book_name = request.GET.get('book_name') # Removed, already at the top
        name = request.POST.get('username')
        copies = request.POST.get('copies')

        if not (name and copies):
            messages.error(request, "Please fill in all fields!")
            return render(request, 'borrow.html', {'book_name': book_name}) #stay at borrow page

        try:
            copies = int(copies)  # Convert copies to integer
        except ValueError:
            messages.error(request, "Invalid number of copies.")
            return render(request, 'borrow.html', {'book_name': book_name})  #stay at borrow page

        try:
            book = get_object_or_404(bookdetails, name=book_name)

            if book.copies >= int(copies): #cast copies to an int

                #if subtract_copies(copies, book_name): #No need for function
                book.copies -= int(copies) #subtract copies here
                book.save()

                borrow_entry = borrow(name=name, book_name=book_name, copies=copies, date_borrowed=datetime.now())
                borrow_entry.save()

                messages.success(request, "Book borrowed successfully!")
                return redirect('books') #Redirect to books, we are done here

            else:
                messages.error(request, f"Not enough copies available for book: {book_name}")
                return render(request, 'borrow.html', {'book_name': book_name}) #stay at borrow page with book_name

        except bookdetails.DoesNotExist:
           messages.error(request, "Book could not be found")
           return redirect('books')  # Go back to the books page if the book is not found

    else:
        #This get request handles the first load
        #book_name = request.GET.get('book_name') #remove get request from here since it can be potentially dangerous to have a get request
        return render(request, 'borrow.html', {'book_name': book_name}) # render page with the book name
def return_book(request):
    if request.method == 'POST':
        borrow_id = request.POST.get('borrow_id')
        try:
             borrow_entry = get_object_or_404(borrow, id=borrow_id)
             book_name = borrow_entry.book_name # Obtains the book_name from the borrow entry.
             book = get_object_or_404(bookdetails, name = book_name) # gets book from bookdetails.
             book.copies += borrow_entry.copies # Adds the copies back to the book.
             book.save() # saves the book
             borrow_entry.delete() # deletes the borrow entry.
        except bookdetails.DoesNotExist:
           messages.error(request,"Book could not be found")
        except borrow.DoesNotExist:
            messages.error(request, "Borrow entry could not be found")
        return redirect('borrowed') # Redirect to the borrowed page

def borrowed(request):
    if not request.session.get('admin_logged_in', False):
        return redirect('admin')
    borrows = borrow.objects.all()
    for borrow_entry in borrows:
        days_borrowed = (datetime.now().date() - borrow_entry.date_borrowed).days
        borrow_entry.remaining_days = 30 - days_borrowed
        borrow_entry.fine = max(0, days_borrowed - 30) * 1  # Assuming fine is 1 unit per day after 30 days
    context = {'borrows': borrows}
    return render(request, 'borrowed.html', context)