from django.db import models
import random
import datetime
# Create your models here.
class Profile(models.Model):
    slug = models.SlugField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

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
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def random_data(self):
        authors = []
        for i in range(50000):
            slug = 'a' + str(i)
            name = 'author' + str(i)
            profile = Profile.objects.get(username='user'+ str(i))
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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date_of_pub = models.DateField()

    def random_data(self):
        books = []
        for i in range(50000):
            slug = 'B' + str(i)
            author = Author.objects.get(name='author' + str(i))
            title = 'Book'+ str(i)
            publisher = Publisher.objects.get(name='publisher' + str(i))
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
        for i in range(50000):
            slug = 'C' + str(i)
            name = 'Collection'+str(i)
            bk = Book.objects.all()
            collection = Collection(slug = slug, name = name)
            collection.save()
            for j in range(random.choice(range(1,10))):
                books = random.choice(bk) 
                collection.books.add(books)
            collection.save()
            print('Collection',i)
        print('Done')

    def __str__(self):
        return self.name
    
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