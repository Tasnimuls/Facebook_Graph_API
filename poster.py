import facebook as fb
import time

while True:
  access_token = "My access token"
  #graph api object
  g_obj = fb.GraphAPI(access_token)

  #generating the content
  post = "my post content"

  print(post)
  print(g_obj.put_object("me", "feed", message=post))

  time.sleep(7200)
