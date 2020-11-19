
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
        # if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
        #     raise ValueError("Temperature too hot")
        self.celsius = celsius

    # property for celsius
    @property
    def celsius(self):
        return self._celsius

    # setter for celsius
    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratorShippingContainer.MAX_CELSIUS :
            raise ValueError("Temperature is too hot")
        self._celsius = value

    #celsius to fahrenheit
    @staticmethod
    def _c_to_f(celsius):
        return celsius * (9/5) + 32

    # fahrenheit to celsius
    @staticmethod
    def _f_to_c(fahrenheit):
        return fahrenheit - 32 * (5/9)

    # To get the fahrenheit
    @property
    def fahrenheit(self):
        return RefrigeratorShippingContainer._c_to_f(self._celsius)

    # Set the temp in celsius when passing fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratorShippingContainer._f_to_c(value)

