
import iso6346

class ShippingContainer:

    next_serial = 8334

    # Changing this to a class method
    @classmethod
    def generate_serial(cls):
        result = cls.next_serial
        ShippingContainer.next_serial += 1
        return result

    # create bic code for shipping container using iso6436
    @staticmethod
    def _create_bic_code(owner_code, serial):
        return iso6346.create(owner_code, str(serial).zfill(6))

    # class method to create a shipping with empty contents
    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    # class method to create a shipping with list of items
    @classmethod
    def create_list(cls, owner_code, list_items, **kwargs):
        return cls(owner_code, contents=list(list_items), **kwargs)

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._create_bic_code(owner_code, ShippingContainer.generate_serial())


class RefrigeratorShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    # Bic code generation for refrigerator shipping container
    @staticmethod
    def _create_bic_code(owner_code, serial):
        return iso6346.create(owner_code, str(serial).zfill(6), category="R")

    # Adding temperature to the constructor
    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > RefrigeratorShippingContainer.MAX_CELSIUS :
            raise ValueError("Temperature too hot")
        self.celsius = celsius
