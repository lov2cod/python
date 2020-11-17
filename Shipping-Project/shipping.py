

class ShippingContainer:

    next_serial = 8334

    # Changing this to a class method
    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        ShippingContainer.next_serial += 1
        return result

    # This helps to create an object with empty contents
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code,[])

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()


