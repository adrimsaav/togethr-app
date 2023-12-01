# Togethr

Welcome to **Togethr**, an innovative social networking platform that combines the best aspects of Instagram, Twitter, and Hinge. Designed for those who seek to share their moments and find others with similar interests, Togethr is the perfect place to connect, engage, and build lasting bonds.

## Features

- **Sign Up/Login**: Easy and secure sign-up/login process to get you started.
- **Create and Share Posts**: Share your experiences, interests, and moments just like you would on Instagram.
- **User Profiles**: Showcase your personality and interests on your profile, making it easier to find and connect with compatible individuals.
- **Account Settings**:Edit your profile pictures, change your bio, delete/edit posts that you created. 
- **Engage with the community**: Like, comment, and interact on posts, bringing the Twitter-like engagement to our platform.
- **Discover and Connect**: Browse profiles, follow/unfollow individuals, and connect with like-minded people.
- **Take Connections Offline**: Extend your online connections into real-world meet-ups and activities, fostering genuine bonds.


## Getting Started

1. **Create an Account**: Sign up to join the Togethr community.
2. **Explore**: Browse through user profiles and posts.
3. **Engage**: Start creating your own posts, comment on others', and build your network.
4. **Connect**: Follow users you find interesting and plan meet-ups to take your connections beyond the screen.

## Screenshots 

 **Home Page**
![image](https://github.com/adrimsaav/togethr-app/assets/87548545/5854b4ce-ec59-4c58-b754-567c9b2ce4e2)

**Sign Up**
![image](https://github.com/adrimsaav/togethr-app/assets/87548545/ee29afda-1b10-4fca-8e63-229efca5c54f)

**Log In**
![image](https://github.com/adrimsaav/togethr-app/assets/87548545/1d8af934-4e05-43f9-a68a-df7dc4192364)

**Timeline**
![image](https://github.com/adrimsaav/togethr-app/assets/87548545/91bc4807-9954-4275-9c94-6b430a10e5c1)


## Technologies Used

- **Python** 
- **Django** 
- **CSS** 
- **HTML** 
- **AWS** 

## App Deployment/Trello Board
1. https://trello.com/b/FKaIeiSF/project-3-twitter-hinge-app-togethr
2. Heroku
3. ERD
- ![image](https://github.com/adrimsaav/togethr-app/assets/87548545/40637627-a77a-40de-9730-ad6c8e1fceef)
 

## Next Steps/Future Implementations 
1. Users being able to DM each other
2. Adding pictures to posts via AWS
3. DM pop-up functionality
4. Further styling for UI
5. Hashtags/location settings
6. Blocking function 

## Challenging Code

**Kevin:**
- ![image](https://github.com/adrimsaav/togethr-app/assets/87548545/d1ea7a44-fb60-4ddd-ad7e-55e474da1c68)

- The most challenging code for me was getting AWS set up and implemented into the project. After watching the AWS Cat Collector version, I realized that the coding format for our project was set up differently compared to the video. In the video, users were able to insert an image after creating an object whereas our plan was to create the object and post the image simultaneously. This led to a bunch of troubleshooting, like from figuring out the correct paths, to merging the post view function with AWS function, to the images not loading upon clicking on post. Basically it was alot of referencing the Cat Collector video to thinking outside of the box and applying the concept to our project. 

**Nisal:**
The biggest challenge I had was with a delete profile function because not only was it not working correctly, but in the process of troubleshooting my migrations became unsynced. I spent an entire day just trying to fix the migrations so this one issue ended up taking away a lot of work time. In the end I wasn't even able to solve the issue on my own and needed help to figure it out. The solution was to drop my database and recreate it. 

![Delete_function_bad](https://github.com/adrimsaav/togethr-app/assets/145291849/bca516ec-94d1-441c-b415-44e519d6f4aa)
![Migration_error](https://github.com/adrimsaav/togethr-app/assets/145291849/5c9cf8e5-5f46-4f43-9696-8434a122e4fd)

The first picture was the code that we had to fix, while it seemed to work it was a little messy. 
The second picture is the error I would get regarding the messed up migrations.  

![object_DNE](https://github.com/adrimsaav/togethr-app/assets/145291849/832c3ea3-25a4-42a5-8346-9f04f94a3a5e)

The third picture is an interesting one because it shows that the profile and unique id for the user were deleted when the function was called, however it didn't delete their authentication. This was an error that was only on my end due to the migration errors.

![Delete_function_fixed](https://github.com/adrimsaav/togethr-app/assets/145291849/64893525-4f3d-4429-9483-54184c898a3a)

This last picture is the fixed version of the delete function that Keith helped us write. We mainly used function based views because that's what we were more comfortable with, however after seeing how much cleaner and reusable class based views are, I feel the need to practice class based views.

**Adriana:**

![Alt text](<Screenshot 2023-12-01 at 9.17.26 AM.png>)

Was difficult in the sense of handling the PostForm and CommentForm submission, it just contained a lot of steps and took me hours to get working.

## Key Takeaways 
- Communication is key in order to reach the finish line
- Everyone has strengths in different areas, so you should take advantage of other people's strengths and ask for help
- Exchanging phone numbers helps ALOT in terms of getting together to work on the project (also helps to wake them up because we would rotate on who naps)
- Even though this was an extremely long project, we did enjoy all of the late nights spent working/bonding together :)

---

- "Honestly one of the most rememberable projects that I've did " - Kevin
- "Lots of struggles throughout this project, but it was worth it" - Adriana
- "i havent slept in 3 days" - Nisal


---

Contributors: Nisal, Adriana, Kevin
