from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser



class accountManager(BaseUserManager):
    def create_user(self,email,fname,lname,phone,password = None):
        if not email:
            raise ValueError('user must have an email')

        if not fname:
            raise ValueError('Unvalid Null Value')
        
        if not lname:
            raise ValueError('Unvalid Null Value')
        
        if not phone:
            raise ValueError('Unvalid Null Value')
        
        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
            fname = fname,
            lname = lname
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self,email,fname,lname,phone,password):
        user = self.create_user(
            email = self.normalize_email(email),
            phone = phone,
            fname = fname,
            lname = lname,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user 







def imagesave(instance,filename):
    imagename , extension = filename.split(".")
    return "users/%s/%s/"%(instance.id,"images")

def cap(string):
    new=string[0].upper()
    for i in range(1,len(string),1):
        if string[i-1] == '-':
            new += string[i].upper()
        else:
            new +=string[i]
    return new

class users(AbstractBaseUser):

    choose = (
        ("Doctor","Doctor"),
        ("Patient" ,"Patient")
    )

    fname         = models.CharField(max_length=20,verbose_name="First Name",unique=False)
    lname         = models.CharField(max_length=20,verbose_name="Last Name",unique=False)
    phone         = models.CharField(max_length=12, verbose_name="Phone",unique=True)
    email         = models.EmailField(unique = True, max_length=254,verbose_name="Email")
    password      = models.CharField(max_length=150)
    image         = models.ImageField(default="users/logo.png",upload_to=imagesave, height_field=None, width_field=None)
    joined_at     = models.DateField(auto_now_add=True,verbose_name="joined at")
    slug          = models.SlugField(blank=True,null=True)
    is_active     = models.BooleanField(default=True)
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    user_type     = models.CharField(max_length=30,choices=choose)
    #addresse

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['fname','lname','phone']

    objects = accountManager()



    def save(self,*args, **kwargs):
        self.slug = slugify(self.fname+" "+self.lname)
        self.slug = cap(self.slug)
        super(users,self).save(*args,**kwargs)


    
    def __str__(self):
        return self.email


    def has_perm(self , perm , obj = None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True


class Category(models.Model):
    name = models.CharField(max_length=60)
 
    def __str__(self):
        return self.name


class doctor(models.Model):
    user     = models.OneToOneField(users,on_delete=models.CASCADE)
    age      = models.IntegerField()
    bio      = models.CharField(max_length = 150)
    quali    = models.TextField(max_length = 400)
    bill     = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start    = models.DateTimeField(auto_now=False, auto_now_add=False)
    end      = models.DateTimeField(auto_now=False, auto_now_add=False)


    
    
    
    
    
    def __str__(self):
        return self.bio





class patient(models.Model):
    user            = models.OneToOneField(users,on_delete=models.CASCADE)
    age             = models.IntegerField()
    

    

    def __str__(self):
        return self.age

    



class Disease(models.Model):

    patient        = models.ForeignKey(patient, on_delete=models.CASCADE)
    disease_name   = models.CharField( max_length=50,verbose_name="disease name")
    when_come      = models.DateTimeField(auto_now=False, auto_now_add=False,verbose_name="when you get this disease")
    is_gone        = models.BooleanField()
    side_effects   = models.TextField(max_length=1000 , verbose_name="Side Effects")

    def __str__(self):
        return self.disease_name


class FamilyDisease(models.Model):
    
    relatives= (
        ("father"       ,   "Father"),
        ("mother"       ,   "Mother"),
        ("sister"       ,   "Sister"),
        ("brother"      ,   "Brother"),
        ("grand father" ,   "Grand father"),
        ("grand mother" ,   "Grand mother"),
    )
    family_patient  = models.ForeignKey(patient, on_delete=models.CASCADE)
    relative_name   = models.CharField(max_length=50, choices=relatives,verbose_name="Relative Position")
    disease_name    = models.CharField( max_length=50,verbose_name="disease name")
    when_come       = models.DateTimeField(auto_now=False, auto_now_add=False,verbose_name="when you get this disease")
    is_gone         = models.BooleanField()
    side_effects    = models.TextField(max_length=1000 , verbose_name="Side Effects")
    
    def __str__(self):
        return self.relative_name



