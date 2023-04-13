results = [
    {
        'id': 16, 'img_url': 
        'https://images.pexels.com/photos/15086545/pexels-photo-15086545.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load', 
        'comment': 'My First Comment !', 
        'created_at': [2023, 4, 11], 
        'updated_at': [2023, 4, 11],
        'user_id': 12, 
        'users.id': 12, 
        'first_name': 'bob', 
        'last_name': 'smith', 
        'email': 'bob@mail.com', 
        'password': '$2b$12$gg7sbJ.zX/wfc0DD0utEdOInmEwfbUjdmdUUH36b/iOfw.g9EfD3K', 
        'users.created_at': [2023, 4, 11], 
        'users.updated_at': [2023, 4, 11],
        'post_id': 16, 
        'likes.user_id': 13, 
        'liked_by.id': 13, 
        'liked_by.first_name': 'ryan', 
        'liked_by.last_name': 'smith', 
        'liked_by.email': 'ryan@mail.com', 
        'liked_by.password': '$2b$12$/pfY5cWEhUssxlBzbDIGx.lw9R5yXK91.fqYkihPYg6NyuUOhO1Hq', 
        'liked_by.created_at': [2023, 4, 11], 
        'liked_by.updated_at': [2023, 4, 11]
    }, 
    {
        'id': 16, 
        'img_url': 'https://images.pexels.com/photos/15086545/pexels-photo-15086545.jpeg?auto=compress&cs=tinysrgb&w=800&lazy=load',
        'comment': 'My First Comment !',
        'created_at': [2023, 4, 11],
        'updated_at': [2023, 4, 11],
        'user_id': 12, 
        'users.id': 12, 
        'first_name': 'bob', 
        'last_name': 'smith', 
        'email': 'bob@mail.com', 
        'password': '$2b$12$gg7sbJ.zX/wfc0DD0utEdOInmEwfbUjdmdUUH36b/iOfw.g9EfD3K', 
        'users.created_at': [2023, 4, 11], 
        'users.updated_at': [2023, 4, 11], 
        'post_id': 16, 
        'likes.user_id': 14, 
        'liked_by.id': 14, 
        'liked_by.first_name': 'godzilla', 
        'liked_by.last_name': 'rawr', 
        'liked_by.email': 'zilla@mail.com', 
        'liked_by.password': '$2b$12$eYrdABURfMJYx2TyzEgntex6LouLe.Ii/PZjGMGvAo.rFI7p/as8u', 
        'liked_by.created_at': [2023, 4, 11], 
        'liked_by.updated_at': [2023, 4, 11]
        }
    ]
    
class User:

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.posts=[]
        
class Post:

    def __init__(self,data):
        self.id = data['id']
        self.img_url = data['img_url']
        self.comment=data['comment']
        self.user_id = data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.owner=None
        self.likes=[]
    

this_post = Post(results[0])
data={
    'id':results[0]["users.id"],
    'first_name':results[0]["first_name"],
    'last_name':results[0]["last_name"],
    'email':results[0]["email"],
    'password':results[0]["password"],
    'created_at':results[0]["users.created_at"],
    'updated_at':results[0]["users.updated_at"],
    
    }

this_owner = User(data)
this_post.owner = this_owner
for row in results:
    if not row["likes.user_id"] == None:
        data={
            'id':row["liked_by.id"],
            'first_name':row["liked_by.first_name"],
            'last_name':row["liked_by.last_name"],
            'email':row["liked_by.email"],
            'password':row["liked_by.password"],
            'created_at':row["liked_by.created_at"],
            'updated_at':row["liked_by.updated_at"],
        }

        this_post.likes.append(User(data))

print(this_post.id)
print(this_post.comment)
print(len(this_post.likes))
for user in this_post.likes:
    print(user.first_name)
    
    

    