App - Hall Of Fame

Built on - Django and postgresql as database. 

Key Feature - Login,Signup, Make your own youtube video playlist. Or search for video to add in your playlist. Edit,remove,update playlist or video. 

How it works - 

Model - Two model is used here. Hall and video. The hall model is used to store the title of the playlist and the user who created this. The User came from default django user model. 

The video model is to store the title,id,and hall as foreign key. The on cascade model on the foreign key is used so when a user remove a video it removes all the information from the user also. 


Views - For adding videos we have used the youtube search api key. I have attached my api key as comment in the view function. 
1.1 Home view is to view the home page which uses the model video. Shows video with the title. 
1.2 add_video - is a functional view that has been used here to add your videos to the playlist. To add videos we have used default django forms. Which is easy to create. First we checked the form data is valid or not then we have taken the video id for this we have used query selector. Then we saved the video. Also we have used decorator. 
1.3 Video search - Here is the fun part. This takes the data from the searchform. Then it gives back a json response. In the search video html files we have used ajax to send the search data here and get the response without reloading the page.

All the other views functions are usual like delete hall or delete video, edit takes the id matches the id and then get the data from the form then update the view. 
