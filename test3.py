
file = open('elon-musk.txt', 'r')

lines=0
lines=len(file.readlines())
print("Number of tweets: " + str(lines) + "\n")

file.seek(0)
longest_tweet=""
line_num=0
longest=0

for tweet in file.readlines():
    line_num += 1
    tweet_length=len(tweet.split())
    if tweet_length > longest:
        longest_tweet=tweet
        longest=tweet_length

print("Tweet with max number of words: " + longest_tweet)

file.seek(0)
line_num=0
my_response=""
status=0
count=0
user_list_A = []
user_list_B = []
user_list = []

for line in file.readlines():
    for word in line.split():
        if "@" in word:
            user_list_A.append(word.lower())

for user in user_list_A:
    user_name = ""
    punctuations = '''!()-[]{};:'"\,<>./?#$%^&*_~'''
    for char in user:
        if char not in punctuations:
            user_name = user_name + char
    user_list_B.append(user_name)

for user in user_list_B:
    if user is '@ ':
        user_list_B.remove(i)
    if user[0] is not '@':
        user_list_B.remove(user)
    
for user in user_list_B:
    final_user=""
    for char in user:
        if char is not '@':
            final_user = final_user + char
    user_list.append(final_user)


while status is 0:
    my_response = input("Enter a choice username: ").lower()
    if my_response is "":
        status=1
        print("No input. Exiting.")
    if "@" in my_response:
        search = ""
        for char in my_response:
            if char is not '@':
                search = search + char
        for user in user_list:
            if search in user and search[0] is user[0]:
                count = count + 1
    if count is 0:
        print("Not mentioned.\n")
    if count > 0:
        print("Mentioned " + str(count) + " times.\n")
    count=0

file.close()
