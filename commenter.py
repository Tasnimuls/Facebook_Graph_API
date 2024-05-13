import facebook
import time

while True:
  try:
    # Authenticate with Facebook
    access_token = "my access token"
    graph = facebook.GraphAPI(access_token)

    # Retrieve posts
    posts = graph.get_object('/me/posts')
    print('Run')
    # Loop through each post
    for post in posts['data']:
        post_id = post['id']

        # Retrieve comments for the post
        comments = graph.get_object(f'/{post_id}/comments')

        # Loop through each comment
        for comment in comments['data']:
            comment_id = comment['id']

            # Check if the comment has replies
            replies = graph.get_object(f'/{comment_id}/comments')
            if not replies['data']:
                #commenter_name = comment['from']['name']
                commenter_name = comment.get('from', {}).get('name', 'Unknown')
                post_content = post.get('message', 'No content')
                quary = "Post:"+ post_content + "   " + commenter_name + ":" + comment['message']
                
                # Prompt user to input reply
                reply_message = "my reply"
                print(quary)
                print(reply_message)

                # Post reply
                graph.put_comment(object_id=comment_id, message=reply_message)
                print("Reply posted successfully!")
            else:
                print('no unreplied comment found')
    time.sleep(60)
  except:
    print('An error occured. Trying again.')
    time.sleep(60)
