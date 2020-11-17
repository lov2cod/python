

class ShippingContainer:

    next_serial = 8334

    # Moving out the serial number generation from init and created a static method
    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code,[])

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()


