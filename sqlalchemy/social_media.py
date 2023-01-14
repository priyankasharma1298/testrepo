# socialmedia database ==> tables=> users | posts  | likes

# relationship between the tables
# user to post => 1 to many [one user can have many diff post but one post can only belong to one user]
# post to like  => 1 to many [one post can have many likes]
# user to like =>  1 to many [one user can like many posts]


from sqlalchemy import create_engine,ForeignKey,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# creating engine  
my_engine = create_engine("mysql+pymysql://root:priyAnka%401298@localhost:3306/socialmedia",echo=False)


# create session
my_session = sessionmaker(bind=my_engine)
session = my_session()  # object of my_session


# create table
base = declarative_base()

class Users(base):
    __tablename__ = "users"

    UserId = Column("UserId",Integer , primary_key=True)
    firstName = Column("firstName",String(50))
    lastName = Column("lastName",String(50))
    profileName = Column("profileName",String(50))
    email = Column("email",String(50))

    def __init__(self , firstName,lastName,profileName,email):
        self.firstName = firstName
        self.lastName = lastName
        self.profileName = profileName
        self.email = email


class Posts(base):
    __tablename__ = "posts"

    postId = Column("postId", Integer , primary_key = True)
    postContent = Column("postContent",String(200))
    userId = Column("userId", Integer , ForeignKey("users.UserId")) # foreignkey(table.cloumnname)

    def __init__(self,userId,postContent):
        self.userId = userId
        self.postContent = postContent




class Likes(base):
    __tablename__ = "likes"

    likeId = Column("likeId",Integer,primary_key=True)
    userId = Column("userId",Integer, ForeignKey("users.UserId"))
    postId = Column("postId", Integer , ForeignKey("posts.postId"))
    

    def __init__(self,userId , postId):
        self.userId = userId
        self.postId = postId



# function to add users
def addUser(session ,firstName,lastName,profileName,email ):
    # checking duplicate entry on basis of email
    exists = session.query(Users).filter(Users.email==email).all()
    if len(exists)>0:
        print("email already exits")
    else:
        # creating a user
        user = Users(firstName,lastName,profileName,email)
        session.add(user)
        session.commit()
        print("user added to db")

# function to add post
def addPost(session , userId,postContent):
    # creating new post
    newPost = Posts(userId, postContent) # object of Posts class
    session.add(newPost)
    session.commit()


# function to like a post
def addLike(session , userId , postId):
    like = Likes(userId , postId)
    session.add(like)
    session.commit()
    print("like was added")



base.metadata.create_all(my_engine)  # migrate so as to make table in db 


# function call of addUser()
firstName = "echoFalse"
lastName = "example2"
profileName = "ecoF993"
email = "echoF@gamil.com"
addUser(session,firstName,lastName,profileName,email)


# function call of addPost()
userId = 1
postContent = "this is a post by user id 3"
addPost(session,userId,postContent)


# to fetch all posts of a particular userid

fetchPost = session.query(Posts).filter(Posts.userId==userId).all()
postsFilterByUser=[i.postContent for i in fetchPost]
print(postsFilterByUser)


# function call of addLike()
userId = 1
postId =2
addLike(session , userId,postId)

# join between two table users and likes to find which user liked a particular post
usersLikedPost = session.query(Users,Likes).filter(Likes.postId == postId).filter(Likes.userId==Users.UserId)
for i in usersLikedPost:
    print(i["Users"].firstName)



    









# creating a user

#firstName = "edward"
#lastName = "clark"
#profileName = "Ed123"
#email = "eddy@gamil.com"

#user = Users(firstName,lastName,profileName,email)
#session.add(user)
#session.commit()

# creating a post

#userId = 1
#postContent = "this is 2nd post by user id 1"
#newPost = Posts(userId, postContent) # object of Posts class

#session.add(newPost)
#session.commit()









