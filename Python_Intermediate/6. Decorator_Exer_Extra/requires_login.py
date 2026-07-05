user_logged_in = False

def requires_login(func):
    def wrapper():
        if user_logged_in:
            return func()
        raise Exception("Error: Unauthenticated user")

    return wrapper

@requires_login
def view_profile():
    return("Profile.....")


try:
    #user_logged_in = True
    print(view_profile())
except Exception as e:
    print(e)
