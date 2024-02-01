from django.db import models
import random
import datetime
from django.db.models import Q
# Create your models here.
class Profile(models.Model):
    slug = models.SlugField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
        
    def get_author_name_profile(self):
        profiles = Profile.objects.all()
        result = []
        for i in profiles:
            result.append({
                'name': i.a_profile.name,
                'profile_detail': {
                    'slug': i.slug,
                    'username': i.username,
                    'email': i.email,
                    'phone': i.phone,
                    'address': i.address,
                }
            })
        return result

    def random_data(self):
        profiles = []
        for i in range(50000):
            slug = 'p' + str(i)
            username = 'user'+ str(i)
            email = username+'@gmail.com'
            phone = str(i)
            address = 'address'+ str(i)
            profile = Profile(slug=slug, username=username, email=email, phone=phone, address=address)
            profiles.append(profile)
            print(i)
        Profile.objects.bulk_create(profiles)
        
    
            
    def __str__(self):
        return self.username


class Author(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='a_profile')


    def num_books(self):
        authors = Author.objects.all()
        return {i:i.book_author.all().count() for i in authors}


    def find_author_input(self):
        a_name = (input("Author name: ")).lower()
        author = Author.objects.get(name=a_name)
        profile_details = {'profile_details':{'username':author.profile.username,
                           'email':author.profile.email,
                           'phone':author.profile.phone,
                           'address':author.profile.address}
                           }
        return profile_details
    
    def get_author_2_books(self):
        authors = Author.objects.all()
        lst = [i for i in authors if len(i.book_author.all()) > 2]
        return lst
    
    def get_name(self):
        authors = Author.objects.all()
        return [i.name for i in authors]
    
    def random_data(self):
        authors = []
        profiles = list(Profile.objects.all())
        for i in range(50000):
            slug = 'a' + str(i)
            name = 'author' + str(i)
            profile = profiles[i]
            author = Author(slug=slug, name=name, profile=profile)
            authors.append(author)
            print(i)
        Author.objects.bulk_create(authors)

        print('Done')

    def __str__(self):
        return self.name


class Publisher(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    website = models.URLField()
    email = models.EmailField()
    address = models.TextField()

    def random_data(self):
        publishers = []
        for i in range(50000):
            slug = 'pub' + str(i)
            name = 'publisher' + str(i)
            website = f'www.{name}.com'
            email = name+'@gmail.com'
            address = 'Pub_address'+ str(i)
            publisher = Publisher(slug=slug, name=name, website=website, email=email, address=address)
            publishers.append(publisher)
            print(i)
        Publisher.objects.bulk_create(publishers)
        print('Done')

    def __str__(self):
        return self.name

class Book(models.Model):
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='book_publisher')
    date_of_pub = models.DateField()
    is_deleted = models.BooleanField(default = False)
    
    #Return the list of books published by given publishers (input will be list of publisher names).
    def get_book_by_publishers(self, pubs):
        lst = []
        for i in pubs:
            pub = Publisher.objects.get(name=i)
            books = pub.book_publisher.all()
            for j in books:
                lst.append(j)
        return lst


    def get_starts_a_book(self):
        authors = Author.objects.filter(name__startswith='a')
        lst = []
        for i in authors:
            books = i.book_author.all()
            for j in books:
                lst.append(j.title)
        return lst
    
    def get_ends_a_book(self):
        authors = Author.objects.filter(name__endswith='1')
        lst = []
        for i in authors:
            books = i.book_author.all()
            for j in books:
                lst.append(j.title)
        return lst
    
    def get_book_by_authorA_B(self, authorA, authorB):
        query = Q(author=authorA)|Q(author=authorB)
        books = Book.objects.filter(query)
        return list(books)
    
    def get_book_exclude(self, a):
        query = ~Q(author=a)
        books = Book.objects.filter(query)
        return list(books)
    
    def delete_book(self, book_title):
        book = Book.objects.filter(title = book_title)
        if book.exists():
            book.delete()
            return "Book deleted"
        return "Book does not exist"
    
    def soft_delete_book(self, book_title):
        book = Book.objects.filter(title = book_title, is_deleted=False)
        if book.exists():
            book[0].is_deleted = True
            book[0].save()
            return "Book soft deleted"
        return "Book already soft deleted"
    
    def get_book_by_author(self, author_name):
        author = Author.objects.get(name=author_name)
        books = author.book_author.all()
        return [i.title for i in books]
    
    def get_book_by_publisher(self, pub_name):
        pub = Publisher.objects.get(name=pub_name)
        books = pub.book_publisher.all()
        return [i.title for i in books]
    
    def get_book_by_author_pub(self, author_name, pub_name):
        aut = Author.objects.get(name=author_name)
        pub = Publisher.objects.get(name=pub_name)
        books = Book.objects.filter(publisher=pub,author = aut)
        return [i for i in books]
    
    def get_book_by_website(self, web):
        pub = Publisher.objects.get(website=web)
        books = pub.book_publisher.all()
        return [i.title for i in books]
            
    def random_data(self):
        books = []
        authors = list(Author.objects.all())
        publishers = list(Publisher.objects.all())
        for i in range(50000):
            slug = 'B' + str(i)
            author = authors[i]
            title = 'Book'+ str(i)
            publisher = publishers[i]
            year = random.choice(range(1600,2025))
            month = random.choice(range(1,13))
            day = random.choice(range(1, 28))
            date_of_pub = datetime.date(year, month, day)
            book = Book(slug=slug, author=author,title=title, publisher=publisher, date_of_pub=date_of_pub)
            books.append(book)
            print(i)
        Book.objects.bulk_create(books)
        print('Done')

    def __str__(self):
        return self.title


class Collection(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def random_data(self):
        collections = []
        bk = list(Book.objects.all())
        for i in range(10):
            slug = 'C' + str(i)
            name = 'Collection'+str(i)
            
            collection = Collection(slug = slug, name = name)
            collection.save()
            for j in range(random.choice(range(1,10))):
                books = random.choice(bk) 
                collection.books.add(books)
            print('Collection',i)
        print('Done')

    def __str__(self):
        return self.books
    
def create_random_data():
    profile = Profile()
    author =Author()
    pub = Publisher()
    book = Book()
    col = Collection()
    profile.random_data()
    author.random_data()
    pub.random_data()
    book.random_data()
    col.random_data()