# ==============================================================================
# user_class.py
# ==============================================================================
class User:
    """Represents a general user. Designed to be cooperative."""
    def __init__(self, first_name, last_name, **kwargs):
        """
        Initializes a User.
        It takes the arguments it needs (first_name, last_name) and forwards
        the rest of the arguments up the inheritance chain using super().
        """
        print("-> Calling User.__init__")
        # Call the __init__ of the next class in the MRO.
        # This ensures that other base classes are also initialized.
        super().__init__(**kwargs) 
        
        self.first_name = first_name
        self.last_name = last_name
        print(f"   - User '{self.first_name}' initialized.")

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\n--- User Profile for {self.first_name} {self.last_name} ---")


# ==============================================================================
# Privileges.py
# ==============================================================================
class Privileges:
    """Represents a set of privileges. Designed to be cooperative."""
    def __init__(self, **kwargs):
        """
        Initializes Privileges.
        This __init__ doesn't take any specific arguments, but it's crucial
        that it accepts **kwargs and calls super() to continue the chain.
        """
        print("-> Calling Privileges.__init__")
        # Call the __init__ of the next class in the MRO. In this hierarchy,
        # this will call object.__init__().
        super().__init__(**kwargs) 
        
        self.privileges = [
            "can view content",
            "can edit content",
            "can delete users"
        ]
        print("   - Privileges initialized.")

    def show_privileges(self):
        """Prints the list of privileges."""
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# ==============================================================================
# administrator.py (The child class)
# ==============================================================================
class Administrator(User, Privileges):
    """
    A special kind of User with administrative Privileges.
    Inherits from both User and Privileges.
    """
    def __init__(self, **kwargs):
        """
        Initializes an Administrator. 
        Notice how simple this is. We just pass all the arguments up
        the chain and super() handles calling User.__init__ and then
        Privileges.__init__ according to the MRO.
        """
        print("-> Calling Administrator.__init__")
        # This single call will trigger the entire cooperative chain.
        super().__init__(**kwargs) 
        print("   - Administrator initialized.")


# ==============================================================================
# Main execution block
# ==============================================================================
if __name__ == "__main__":
    print("Creating an Administrator instance...")
    
    # Python determines the Method Resolution Order (MRO):
    # Administrator -> User -> Privileges -> object
    print("MRO:", [c.__name__ for c in Administrator.__mro__])
    print("-" * 30)

    # Instantiate the Administrator using keyword arguments. This is important
    # because each __init__ in the chain will find the arguments it needs.
    admin = Administrator(first_name='Kamaraj', last_name='Nadar')

    print("-" * 30)

    # Now we can call methods from all parent classes.
    admin.describe_user()
    admin.show_privileges()

