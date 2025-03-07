class User :
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement

    def __repr__(self):
        return f"< User {self.name}"

def email_engaged_user(user):
    try:
        user.score =  perform_calculation(user.engagement_metrics)
    except KeyError :
        print('Innocent values provided to our calculation function .')
    else:
        if user.score > 500 :
            send_engagement_notification(user)

def perform_calculation(metrics):
    return metrics['click'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f'Notifications sent to the {user} .')

my_user = User('Rolf',{'clicks ' :61 , 'hits' : 100})
email_engaged_user(my_user)

'''
def power_of_two():
    user_input = input("Please enter a number : ")
    try:
        n = float(user_input)
    except ValueError:
        print("Your input was invalid.Using default value of 0")
        return 0
    else :
        n_square = n ** 2

print(power_of_two())
print(power_of_two())
'''