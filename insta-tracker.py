import instaloader

def get_followers_following(L, target_username):
    # Get the profile of the target username
    profile = instaloader.Profile.from_username(L.context, target_username)

    # Retrieve followers
    followers = set()
    for follower in profile.get_followers():
        followers.add(follower.username)

    # Retrieve following
    following = set()
    for followee in profile.get_followees():
        following.add(followee.username)

    return followers, following

if __name__ == "__main__":
    # Replace these with your Instagram username and password
    YOUR_USERNAME = 'YOUR_USERNAME'
    YOUR_PASSWORD = 'YOUR_PASSWORD'

    # Replace this with the target Instagram username
    TARGET_USERNAME = 'YOUR_TARGET_USERNAME'

    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Log in to your Instagram account
    L.login(YOUR_USERNAME, YOUR_PASSWORD)

    followers, following = get_followers_following(L, TARGET_USERNAME)
    followers_set = set(followers)
    followees_set = set(following)

    print(f"Followers of {TARGET_USERNAME} you don't follow back:")
    for follower in followers:
        if follower not in followees_set:
            print(follower)

    print(f"\nFollowing of {TARGET_USERNAME} they don't follow you back:")
    for followee in following:
        if followee not in followers_set:
            print(followee)
