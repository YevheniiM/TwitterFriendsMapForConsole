from helpers import twitter_friends_request

def main():
    print("\n\n============== Welcome to my little server ==============")
    print("\nI really  worry  about  my personal  data, so... To use")
    print("this  program,  firstly, you  need to enter your personal")
    print("data to access your twitter API. \n")
    print("=========================================================")
    print("Very sorry  about  this problem, that  happens  because I")
    print("need to publish this program  to GitHub repository, which")
    print("is  public  (because I  don't have  7 external  dollars).")
    print("So,  that's not  because I  don't trust  you, but because")
    print("I don't trust everyone in  the Internet and I think, that")
    print("they can steal my data to use it in their personal needs.")
    print("=========================================================")
    print("To try my program which works with my data to access API")
    print("you can visit \"yevgesh.pythonanywhere.com\".")
    print("=========================================================")

    print("\n\nEnter your data here")

    name = input("Enter friend's name: ")
    count = input("Enter count of friends: ")
    twitter_friends_request.show_friends_on_the_map(name, count)


if __name__ == '__main__':
    main()
