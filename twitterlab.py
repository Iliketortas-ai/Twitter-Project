users = {}
posts = []
post_id = 1  


def create_user():
    """Ask for a username and bio, and add to users dict."""
    while True:
        username = input("Choose a username (letters/numbers/underscores only): ").strip()
        if not username:
            print("Username can't be blank. Try again.")
            continue
        if username in users:
            print("That username is already taken. Try another.")
            continue
        if not all(c.isalnum() or c in "_-" for c in username):
            print("Username may only contain letters, numbers, underscores,  or hyphens.")
            continue
        break

    bio = input("Write a short bio (one line): ").strip()
    users[username] = {"bio": bio, "followers": 0}
    print(f"User '{username}' created.\n")


def write_post():
    """Ask who is posting and the text, create post dict with next id and append to posts."""
    global post_id
    if not users:
        print("No users yet — create a user first.\n")
        return

    username = input("Who is posting? (enter username): ").strip()
    if username not in users:
        print("No such user. Check username or create the user first.\n")
        return

    text = input("What's on your mind? (max 280 characters): ").rstrip()
    if not text:
        print("Post cannot be blank.\n")
        return
    if len(text) > 280:
        text = text[:280]
        print("Text truncated to 280 characters.")

    post = {"id": post_id, "user": username, "text": text, "likes": 0}
    posts.append(post)
    print(f"Post created with id {post_id}.\n")
    post_id += 1


def view_feed():
    """Loop through posts and print them neatly (most recent first)."""
    if not posts:
        print("No posts yet. Be the first to post!\n")
        return

    print("\n--- FEED (most recent first) ---")
    for p in reversed(posts):  
        print(f"[{p['id']}] {p['user']}: {p['text']}")
        print(f"     Likes: {p['likes']}\n")
    print("--- end feed ---\n")


def like_post():
    """Ask for a post id and increase its likes by 1."""
    if not posts:
        print("No posts to like yet.\n")
        return

    try:
        pid = int(input("Enter the post ID you want to like: ").strip())
    except ValueError:
        print("Please enter a valid integer post ID.\n")
        return

    for p in posts:
        if p["id"] == pid:
            p["likes"] += 1
            print(f"You liked post {pid}. It now has {p['likes']} likes.\n")
            return

    print(f"No post found with id {pid}.\n")


# ---------- Extensions ----------

def search_feed():
    """Search posts for a word or phrase (case-insensitive) and print matches."""
    if not posts:
        print("No posts to search.\n")
        return

    query = input("Enter a word or phrase to search for: ").strip().lower()
    if not query:
        print("Search query can't be blank.\n")
        return

    matches = [p for p in posts if query in p["text"].lower() or query in p["user"].lower()]
    if not matches:
        print("No posts matched your search.\n")
        return

    print(f"\nFound {len(matches)} match(es):")
    for p in reversed(matches):  
        print(f"[{p['id']}] {p['user']}: {p['text']}  (Likes: {p['likes']})")
    print()


def show_most_liked():
    """Show the post(s) with the highest number of likes."""
    if not posts:
        print("No posts yet.\n")
        return

    max_likes = max(p["likes"] for p in posts)
    top_posts = [p for p in posts if p["likes"] == max_likes]

    print(f"\nTop liked post(s) — {max_likes} like(s):")
    for p in top_posts:
        print(f"[{p['id']}] {p['user']}: {p['text']}")
    print()


def edit_bio():
    """Allow a user to edit their bio."""
    if not users:
        print("No users yet.\n")
        return

    username = input("Which user would you like to edit (username): ").strip()
    if username not in users:
        print("User not found.\n")
        return

    print(f"Old bio: {users[username]['bio']}")
    new_bio = input("Enter a new bio: ").strip()
    users[username]["bio"] = new_bio
    print("Bio updated.\n")


def delete_post():
    """Allow the post's owner to delete a post by id."""
    if not posts:
        print("No posts yet.\n")
        return

    try:
        pid = int(input("Enter the post ID to delete: ").strip())
    except ValueError:
        print("Please enter a valid integer post ID.\n")
        return

    for i, p in enumerate(posts):
        if p["id"] == pid:
            owner = input("Enter your username to confirm deletion: ").strip()
            if owner != p["user"]:
                print("You can only delete your own posts.\n")
                return
            del posts[i]
            print(f"Post {pid} deleted.\n")
            return

    print(f"No post found with id {pid}.\n")




def show_menu():
    print("Choose an option:")
    print("1. Create a user")
    print("2. Write a post")
    print("3. View the feed")
    print("4. Like a post")
    print("5. Search the feed (extension)")
    print("6. Show most-liked post (extension)")
    print("7. Edit a user's bio (extension)")
    print("8. Delete a post (extension)")
    print("9. Exit")


def main():
    print("Welcome to Mini Twitter!\n")
    while True:
        show_menu()
        choice = input("Enter a number: ").strip()
        print()
        if choice == "1":
            create_user()
        elif choice == "2":
            write_post()
        elif choice == "3":
            view_feed()
        elif choice == "4":
            like_post()
        elif choice == "5":
            search_feed()
        elif choice == "6":
            show_most_liked()
        elif choice == "7":
            edit_bio()
        elif choice == "8":
            delete_post()
        elif choice == "9":
            print("Goodbye — thanks for using Mini Twitter!")
            break
        else:
            print("Invalid option. Please enter a number from the menu.\n")


if __name__ == "__main__":
    main()
