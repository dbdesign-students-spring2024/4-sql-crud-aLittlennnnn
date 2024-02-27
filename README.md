# SQL CRUD

## links to csv files
[restaurants.csv](./data/restaurants.csv)
[users.csv](./data/users.csv)
[messages.csv](./data/messages.csv)
[stories.csv](./data/stories.csv)
[posts.csv](./data/posts.csv)


## Part 1: Restaurant Finder
To get started, I typed in the following command to create a new database called `part1.db` for the part 1 of this assignment:
~~~sql
sqlite3 part1.db
~~~
### table structures
#### restaurants
Below are the first 20 rows of the [restaurants.csv](./data/restaurants.csv) file.
~~~sql
Restaurant_id,Restaurant,Category,Price,Neighbourhood,Open_time,Close_time,Average_rating,Good_for_kids
1,The Caramel Star,Pizza,cheap,Manhattan,11:27,23:41,5,true
2,The Caramel Star,Danish,expensive,Bronx,5:14,18:37,3,true
3,The Ruby Spices,Asian,cheap,Brooklyn,4:41,16:55,4,false
4,The Mountainview Bistro,French,expensive,Queens,0:32,20:13,5,true
5,The Ruby Spices,Sushi,expensive,Staten Island,2:46,12:16,2,false
6,The Boiling Dairy,Vegetarian,medium,Brooklyn,6:27,21:45,2,true
7,The Thai Devil,Seafood,expensive,Queens,4:11,15:51,1,true
8,The Caramel Star,French,cheap,Queens,3:12,16:57,5,false
9,The Painted Stranger,Indian,expensive,Bronx,4:42,15:13,5,true
10,The Ruby Spices,African,medium,Staten Island,6:40,16:21,4,true
11,The Pearl,African,cheap,Queens,0:05,16:09,3,true
12,The Garden,Pizza,expensive,Queens,9:40,23:32,4,false
13,The Crown,Seafood,expensive,Bronx,9:46,16:16,2,false
14,The Boiling Dairy,Asian,medium,Staten Island,6:45,23:03,4,false
15,The Pearl,Asian,cheap,Bronx,11:28,19:31,4,true
16,Modesty,Pizza,medium,Manhattan,10:16,14:55,2,false
17,The Pearl,Cuban,cheap,Manhattan,3:03,14:02,5,true
18,The Pearl,Sushi,cheap,Manhattan,8:35,23:41,1,true
19,The Thai Devil,Spanish,medium,Manhattan,7:41,14:10,2,true
~~~

In order to import the csv file into an SQLite table, I first initiated an sqlite table with the following fields:
~~~sql
CREATE TABLE restaurants (
   ...> Restaurant_id INTEGER PRIMARY KEY,
   ...> Restaurant TEXT,
   ...> Category TEXT,
   ...> Price TEXT,
   ...> Neighboorhood TEXT,
   ...> Open_time TEXT,
   ...> Close_time TEXT,
   ...> Average_rating INTEGER,
   ...> Good_for_kids INTEGER);
~~~

Then I turned on csv mode and import the _restaurants.csv_ into the sqlite table `restaurants` I have just  created:
~~~sql
.mode csv
.headers on
.import restaurants.csv restaurants --skip 1
~~~

Among all the fields, the field of **Restaurant_ID** will be used as both **primary key** for the `restaurants` table and the **foreign key** to the `reviews` table.

#### reviews
Create the `reviews` table with the following command:
~~~sql
CREATE TABLE reviews(
...> Review_ID INTEGER PRIMARY KEY,
...> Restaurant_id INTEGER,
...> Customer_name TEXT,
...> Comment TEXT,
...> Rating INTEGER,
...> FOREIGN KEY (Restaurant_id) REFERENCES restaurants(Restaurant_id)
...> );
~~~
Among all the fields, the field of **Review_ID** will be used as **primary key** of the `reviews` table, and the field of **Restaurant_ID** will be used as **foreign key** to the `restaurants` table.

### SQL queries

1. Find all cheap restaurants in a particular neighborhood (pick any neighborhood as an example).<br>
I found all cheap restaurants in Manhattan.
Corresponding query:
~~~sql
SELECT Restaurant from restaurants WHERE Price = "cheap" AND Neighboorhood = "Manhattan";
~~~
And we can get the results:

~~~sql
Restaurant
"The Caramel Star"
"The Pearl"
"The Pearl"
"The Painted Stranger"
"The Mountainview Bistro"
Babylon
"The Imperial Ship"
"The Mountainview Bistro"
"The Ruby Spices"
"The Boiling Dairy"
"The Caramel Star"
"The Painted Stranger"
"The Imperial Ship"
Babylon
"The Boiling Dairy"
Modesty
"The Ruby Spices"
Modesty
"The Noodle Oak"
"The Boiling Dairy"
"The Imperial Ship"
"The Greek Tiger"
"The Ruby Spices"
"The Boiling Dairy"
Modesty
"The Thai Devil"
"The Crown"
"The Garden"
"The Noodle Oak"
"The Caramel Star"
"The Painted Stranger"
Babylon
"The Garden"
"The Caramel Star"
"The Imperial Ship"
"The Garden"
"The Mountainview Bistro"
"The Garden"
"The Crown"
"The Caramel Star"
"The Imperial Ship"
"The Noodle Oak"
"The Pearl"
Babylon
"The Crown"
"The Caramel Star"
"The Caramel Star"
"The Mountainview Bistro"
"The Ruby Spices"
"The Caramel Star"
"The Pearl"
"The Noodle Oak"
Babylon
"The Private Fiddler"
"The Private Fiddler"
"The Private Fiddler"
Babylon
"The Boiling Dairy"
"The Mountainview Bistro"
"The Ruby Spices"
"The Thai Devil"
"The Boiling Dairy"
"The Boiling Dairy"
Babylon
"The Private Fiddler"
"The Greek Tiger"
"The Noodle Oak"
"The Painted Stranger"
Babylon
"The Pearl"
"The Private Fiddler"
"The Caramel Star"
"The Mountainview Bistro"
"The Noodle Oak"
~~~

2. Find all restaurants in a particular genre (pick any genre as an example) with 3 stars or more, ordered by the number of stars in descending order.<br>
I found all Spanish restaurants with 3 or more starts ordered by the number of starts in descending order.
Corresponding query:
~~~sql
SELECT Restaurant from restaurants WHERE Category = "Spanish" AND Average_rating >=3 ORDER BY Average_rating DESC;
~~~
And we can get the results:
~~~sql
Restaurant
"The Imperial Ship"
"The Boiling Dairy"
"The Caramel Star"
"The Mountainview Bistro"
"The Crown"
"The Thai Devil"
"The Imperial Ship"
"The Crown"
"The Boiling Dairy"
"The Greek Tiger"
"The Thai Devil"
"The Garden"
"The Private Fiddler"
"The Ruby Spices"
"The Noodle Oak"
"The Painted Stranger"
"The Ruby Spices"
"The Thai Devil"
"The Noodle Oak"
"The Private Fiddler"
"The Thai Devil"
"The Private Fiddler"
Modesty
"The Boiling Dairy"
"The Painted Stranger"
"The Pearl"
Modesty
Babylon
"The Boiling Dairy"
"The Caramel Star"
"The Caramel Star"
"The Painted Stranger"
"The Crown"
Modesty
"The Caramel Star"
"The Imperial Ship"
"The Mountainview Bistro"
"The Private Fiddler"
"The Noodle Oak"
"The Mountainview Bistro"
"The Boiling Dairy"
"The Noodle Oak"
"The Garden"
"The Garden"
Babylon
"The Crown"
"The Greek Tiger"
"The Caramel Star"
"The Private Fiddler"
Modesty
"The Pearl"
Modesty
Modesty
"The Garden"
~~~

3. Find all restaurants that are open now (see hint below).<br>
Corresponding query:
~~~sql
SELECT Restaurant from restaurants WHERE Open_time<=strftime('%H:%M', 'now') AND strftime('%H:%M', 'now')<= Close_time;
~~~

The current time is 12:22 PM, and I get the results:
~~~sql
Restaurant
"The Caramel Star"
"The Mountainview Bistro"
"The Pearl"
Modesty
"The Pearl"
"The Painted Stranger"
"The Imperial Ship"
"The Garden"
"The Greek Tiger"
"The Noodle Oak"
"The Mountainview Bistro"
Babylon
"The Ruby Spices"
Babylon
"The Ruby Spices"
"The Noodle Oak"
"The Boiling Dairy"
"The Garden"
"The Private Fiddler"
"The Painted Stranger"
"The Boiling Dairy"
"The Ruby Spices"
"The Caramel Star"
"The Noodle Oak"
Modesty
"The Thai Devil"
"The Painted Stranger"
"The Boiling Dairy"
"The Ruby Spices"
"The Boiling Dairy"
Modesty
"The Boiling Dairy"
"The Noodle Oak"
Babylon
"The Garden"
"The Thai Devil"
"The Boiling Dairy"
"The Boiling Dairy"
"The Boiling Dairy"
"The Pearl"
"The Ruby Spices"
"The Imperial Ship"
"The Thai Devil"
Modesty
"The Greek Tiger"
"The Private Fiddler"
"The Painted Stranger"
"The Painted Stranger"
"The Ruby Spices"
"The Crown"
"The Boiling Dairy"
"The Boiling Dairy"
Modesty
"The Imperial Ship"
"The Greek Tiger"
"The Greek Tiger"
"The Noodle Oak"
"The Private Fiddler"
"The Garden"
"The Caramel Star"
Modesty
"The Noodle Oak"
"The Private Fiddler"
"The Pearl"
"The Mountainview Bistro"
"The Greek Tiger"
"The Greek Tiger"
"The Noodle Oak"
"The Ruby Spices"
"The Mountainview Bistro"
"The Thai Devil"
"The Greek Tiger"
"The Thai Devil"
"The Boiling Dairy"
"The Greek Tiger"
"The Mountainview Bistro"
"The Private Fiddler"
"The Ruby Spices"
"The Garden"
"The Ruby Spices"
Babylon
"The Caramel Star"
"The Imperial Ship"
"The Thai Devil"
"The Pearl"
"The Boiling Dairy"
"The Thai Devil"
"The Private Fiddler"
"The Painted Stranger"
"The Painted Stranger"
"The Pearl"
"The Boiling Dairy"
"The Garden"
"The Boiling Dairy"
Modesty
"The Caramel Star"
"The Mountainview Bistro"
"The Crown"
"The Greek Tiger"
"The Noodle Oak"
"The Mountainview Bistro"
"The Garden"
"The Crown"
"The Painted Stranger"
"The Crown"
Babylon
"The Crown"
"The Garden"
"The Pearl"
"The Boiling Dairy"
"The Ruby Spices"
"The Boiling Dairy"
"The Mountainview Bistro"
"The Painted Stranger"
"The Crown"
"The Noodle Oak"
"The Mountainview Bistro"
"The Noodle Oak"
"The Caramel Star"
"The Caramel Star"
Babylon
"The Private Fiddler"
"The Ruby Spices"
"The Crown"
"The Caramel Star"
"The Thai Devil"
"The Crown"
"The Thai Devil"
"The Greek Tiger"
"The Imperial Ship"
"The Noodle Oak"
"The Painted Stranger"
"The Imperial Ship"
Babylon
"The Painted Stranger"
"The Noodle Oak"
"The Crown"
Babylon
"The Boiling Dairy"
~~~

4. Leave a review for a restaurant (pick any restaurant as an example).
~~~sql
INSERT INTO reviews (Review_ID, Restaurant_id, Customer_name, Comment, Rating) VALUES (1,1,"Yi","Good service!",5);
~~~

5. Delete all restaurants that are not good for kids.

~~~sql
DELETE FROM restaurants WHERE Good_for_kids = "false";
~~~

6. Find the number of restaurants in each NYC neighborhood.

~~~sql
SELECT Neighboorhood,count(Restaurant) from restaurants GROUP BY Neighboorhood;
~~~

And I get the results:

~~~sql
Neighboorhood,count(Restaurant)
Bronx,114
Brooklyn,99
Manhattan,102
Queens,86
"Staten Island",108
~~~


## Part 2: Social Media APP
To get started, I created a `part2.db` database for the Part2 of this assignment:

~~~sql
sqlite3 part2.db
~~~

### Tables Structure
#### users
I generated [users.csv](./data/users.csv) with fields of User_id, Username, Email,and Password:

I write the following command to import the csv file into sqlite:
~~~sql
CREATE TABLE users(
   ...> User_id INTEGER PRIMARY KEY,
   ...> Username TEXT,
   ...> Email TEXT,
   ...> Password TEXT);
~~~
~~~sql
.mode csv
.headers on
.import users.csv users --skip 1
~~~

Both user_id and username are supposed to be unique.

The **User_id** is the **primary key** of `users` table and the **Username** will be the **foreign key** to the `posts` table.


#### posts
I created the [posts.csv](./data/posts.csv) by combining [messages.csv](./data/messages.csv) and [stories.csv](./data/stories.csv)using [combine.py](./combine.py), which all have the fields of post_id,type,created_time,status,message_from,message_to,author,content.

To get more visible information, I set the weight for visible messages 3 times to the invisible ones.

Now we import the csv file into sqlite table `posts` with the following commands:

Post_id,Type,Status,Sender,Receiver,Content,Created

~~~sql
CREATE TABLE posts(
   ...> Post_id INTEGER PRIMARY KEY,
   ...> Type TEXT,
   ...> Status TEXT,
   ...> Sender TEXT,
   ...> Receiver TEXT,
   ...> Content TEXT,
   ...> Created DATETIME DEFAULT CURRENT_TIMESTAMP,
   ...> FOREIGN KEY (Sender) REFERENCES users(Username),
   ...> FOREIGN KEY (Receiver) REFERENCES users(Username)
   ...> );
~~~
~~~sql
.import posts.csv posts --skip 1
~~~

The **post_id** is the **primary key** of the `posts` table, and the **Sender**, **Receiver**, columns are all **foreign keys** to the `users` table, referencing **Username**

### SQL queries

1. Register a new User.
~~~sql
INSERT INTO users (User_id,Username,Email,Password) VALUES (1001,"YiWang","abcde@some.com","hahahahahaha");
~~~

2. Create a new Message sent by a particular User to a particular User (pick any two Users for example).
~~~sql
INSERT INTO posts (Post_id, Type, Status, Sender, Receiver, Content) VALUES (2001,"visible","message","YiWang","bduggon0","hello");
~~~

3. Create a new Story by a particular User (pick any User for example).
~~~sql
INSERT INTO posts (Post_id, Type, Status, Sender, Content) VALUES (2002,"visible","story","YiWang","hello world!!");
~~~

4. Show the 10 most recent visible Messages and Stories, in order of recency.
~~~sql
SELECT * FROM posts WHERE Type = "visible" ORDER BY Created DESC LIMIT 10;
~~~

And I get the result:
~~~sql
Post_id,Type,Status,Sender,Receiver,Content,Created
2002,visible,story,YiWang,,"hello world!!","2024-02-27 18:46:35"
2001,visible,message,YiWang,bduggon0,hello,"2024-02-27 18:46:30"
1128,visible,story,aportrisso2,"","Morbi a ipsum.","2024-02-25 23:05:54"
632,visible,message,amongetns,kmosdell7o,"Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum.","2024-02-25 10:39:18"
808,visible,message,ptitchard14,dboicekq,"Morbi vel lectus in quam fringilla rhoncus. Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.","2024-02-25 06:26:25"
1485,visible,story,hledbury4w,"","Nunc purus. Phasellus in felis. Donec semper sapien a libero. Nam dui.","2024-02-25 06:17:57"
1560,visible,story,oivashechkin5y,"","Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.","2024-02-25 05:45:24"
1507,visible,story,ksimonato3h,"","In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy.","2024-02-25 05:18:44"
1908,visible,story,bbrent5l,"","Nulla tellus.","2024-02-25 03:36:31"
53,visible,message,rdukesburyd6,hgilbride21,"Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus.","2024-02-24 21:45:22"
~~~


5. Show the 10 most recent visible Messages sent by a particular User to a particular User (pick any two Users for example), in order of recency.

~~~sql
SELECT * FROM posts WHERE Type = "visible" AND Sender = "YiWang" AND Receiver = "bduggon0" ORDER BY created DESC LIMIT 10;
~~~
And I get the result:
~~~sql
Post_id,Type,Status,Sender,Receiver,Content,Created
2001,visible,message,YiWang,bduggon0,hello,"2024-02-27 18:46:30"
~~~

6. Make all Stories that are more than 24 hours old invisible.
~~~sql
UPDATE posts SET Type = "invisible" WHERE Status = "story" AND Created <= datetime('now','-1 day');
~~~

7. Show all invisible Messages and Stories, in order of recency.
~~~sql
SELECT * FROM posts WHERE Type = "invisible" ORDER BY Created DESC;
~~~

here only the first 10 rows are shown, there are too many invisible posts:
~~~sql
Post_id,Type,Status,Sender,Receiver,Content,Created
1128,invisible,story,aportrisso2,"","Morbi a ipsum.","2024-02-25 23:05:54"
1485,invisible,story,hledbury4w,"","Nunc purus. Phasellus in felis. Donec semper sapien a libero. Nam dui.","2024-02-25 06:17:57"
1560,invisible,story,oivashechkin5y,"","Integer non velit. Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.","2024-02-25 05:45:24"
1507,invisible,story,ksimonato3h,"","In tempor, turpis nec euismod scelerisque, quam turpis adipiscing lorem, vitae mattis nibh ligula nec sem. Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy.","2024-02-25 05:18:44"
1908,invisible,story,bbrent5l,"","Nulla tellus.","2024-02-25 03:36:31"
530,invisible,message,dbaynham51,cyockleya5,"Vivamus vestibulum sagittis sapien.","2024-02-25 02:48:42"
1728,invisible,story,bburridgeaw,"","Proin interdum mauris non ligula pellentesque ultrices.","2024-02-24 14:46:50"
1363,invisible,story,mmcmackin4b,"","In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.","2024-02-24 06:21:06"
1518,invisible,story,scheers4o,"","Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla.","2024-02-24 03:50:57"
354,invisible,message,mfearnsidesq6,ikendal55,"Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus.","2024-02-24 02:16:38"
~~~

8. Show the number of posts by each User.
~~~sql
SELECT Sender,count(Post_id) from posts GROUP BY Sender;
~~~

results, only the first 10 are shown since there's too many:

~~~sql
Sender,count(Post_id)
YiWang,2
aadamovsky4a,1
aapplefordqy,2
abaldungbw,2
abalharryea,1
abaylisgq,2
abeastonjg,1
abenzipz,3
aberreyhn,2
abrockieab,2
~~~

10. Show the email addresses of all Users who have not posted anything yet.
~~~sql
SELECT users.Email FROM users LEFT JOIN posts ON users.Username = posts.Sender WHERE users.Username NOT IN (SELECT Sender FROM posts);
~~~

and the results:
~~~sql
Email
logilvy5@drupal.org
hcristofolini6@github.com
ibarbosa9@ebay.co.uk
wtythacottf@webmd.com
ccoopmanh@nhs.uk
aberes@weather.com
pgainsefordu@fc2.com
aguilloton11@pagesperso-orange.fr
vkelsall16@hugedomains.com
rwilmington1f@g.co
dmarns1t@wikipedia.org
ceglese20@moonfruit.com
pbeddoe2c@nps.gov
gknightsbridge2k@sfgate.com
cyakovlev2o@earthlink.net
edelamaine2s@google.fr
mjachimak2w@cnbc.com
mentwhistle33@slashdot.org
jlatore3i@webnode.com
ahearle47@usa.gov
bbannon49@ezinearticles.com
bemtage4s@sakura.ne.jp
vdibiaggi4t@harvard.edu
pgeelan53@oracle.com
vleyband59@google.nl
ehoult5j@usa.gov
dmacdearmont5k@wikispaces.com
cdellenbroker5m@psu.edu
cvanyashin5p@behance.net
haberkirder5u@google.com.au
asasser63@51.la
gcarle65@upenn.edu
gconerding6a@simplemachines.org
wscahill6g@hatena.ne.jp
tcasaroli6o@slideshare.net
dorys6x@amazonaws.com
ffrancombe71@icq.com
cniemetz78@digg.com
pduncanson7b@npr.org
nwile7d@patch.com
mwilsdon7i@so-net.ne.jp
gmanske7y@elegantthemes.com
kflannigan8a@fc2.com
eblaszczyk8j@symantec.com
epipkin8q@bigcartel.com
mmacgiany8r@myspace.com
csauvage8u@gmpg.org
lpeabody98@newyorker.com
hcowerd9b@patch.com
idresser9e@odnoklassniki.ru
eenevoldsen9s@sakura.ne.jp
cravenhillsa1@wp.com
rkynana3@etsy.com
esegota8@businessweek.com
pmacdunleavyas@eepurl.com
dgouthieray@epa.gov
fcourtenaybb@hao123.com
rfindenbe@europa.eu
lcohanibl@indiatimes.com
vleveretbp@columbia.edu
emaclennanbt@delicious.com
scurseybz@japanpost.jp
rnorewoodce@blogtalkradio.com
fcleverlycf@nyu.edu
xaustinscn@icq.com
rgateshillcw@nydailynews.com
cmactavishcy@amazon.com
blinskilld3@prlog.org
aegeld5@wikimedia.org
ekarpinskid7@wikispaces.com
ccaveneydd@angelfire.com
sbonicellidh@ucoz.com
sfargherdk@networkadvertising.org
akubecdz@google.com
omaliphante4@rambler.ru
rblogge8@census.gov
mbailsep@google.es
mmenhamet@jimdo.com
ocrowcherex@oaic.gov.au
kvannaccif2@angelfire.com
jbairdf6@hibu.com
pechellef8@wiley.com
kchiecofa@timesonline.co.uk
kstookesfb@addthis.com
strathanfc@irs.gov
kscarlonfk@slate.com
mbarkleyfl@angelfire.com
ltembridgefr@army.mil
tlaydelg4@odnoklassniki.ru
bgantergg@cafepress.com
etawtongj@chronoengine.com
csarfatiho@bravesites.com
aharridayhq@nymag.com
rdewarei7@stumbleupon.com
rclethroiw@lycos.com
fsimisoniy@vistaprint.com
bllywarchj3@skype.com
jsmizj8@marketwatch.com
libotsonjb@ycombinator.com
afontellesje@hugedomains.com
kcaplisjn@ezinearticles.com
hedmensonjo@sun.com
lcolliejs@usgs.gov
slongleyjt@taobao.com
fmossonjw@yelp.com
dcumberlidgejy@latimes.com
rcaulierk3@google.fr
bpydcockkh@slate.com
gwermerlingkv@wix.com
imcilwrickl4@webeden.co.uk
apinxtonlc@sun.com
apinyonlk@twitpic.com
wlamblr@mtv.com
bkeyzmanlu@ebay.co.uk
hharriskinelv@bloglines.com
aottiwillm5@skype.com
akentonmt@skyrock.com
mluttgern4@eepurl.com
codamnh@oaic.gov.au
egladyernn@cpanel.net
mduffittom@merriam-webster.com
jlingleyp7@reverbnation.com
jbowermanpb@usda.gov
rcurgenvenpg@over-blog.com
aharridayph@sohu.com
vfogtpq@cisco.com
pwatsampt@vistaprint.com
tvoiseyq4@usatoday.com
gzammettqe@twitpic.com
feffordqf@cbsnews.com
lbennedickqi@noaa.gov
bpyserr2@epa.gov
bberthelmotr8@apache.org
jcherringtonrb@t-online.de
emontesrg@aboutads.info
~~~
