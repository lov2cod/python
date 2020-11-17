
import iso6346

class ShippingContainer:

    next_serial = 8334

    # Changing this to a class method
    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        ShippingContainer.next_serial += 1
        return result

    # create bic code for shipping container using iso6436
    @staticmethod
    def _create_bic_code(owner_code, serial):
        return iso6346.create(owner_code, str(serial).zfill(6))

    # class method to create a shipping with empty contents
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code,[])

    # class method to create a shipping with list of items
    @classmethod
    def create_list(cls, owner_code, list_items):
        return cls(owner_code, contents=list(list_items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = ShippingContainer._create_bic_code(owner_code, ShippingContainer._generate_serial())


