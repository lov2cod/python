
import iso6346

class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

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
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    # class method to create a shipping with list of items
    @classmethod
    def create_list(cls, owner_code, length_ft, list_items, **kwargs):
        return cls(owner_code, length_ft, contents=list(list_items), **kwargs)

    @property
    def volume_ft(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.bic = self._create_bic_code(owner_code, ShippingContainer.generate_serial())


class RefrigeratorShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME = 100

    # Bic code generation for refrigerator shipping container
    @staticmethod
    def _create_bic_code(owner_code, serial):
        return iso6346.create(owner_code, str(serial).zfill(6), category="R")

    # Adding temperature to the constructor
    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        # if celsius > RefrigeratorShippingContainer.MAX_CELSIUS:
        #     raise ValueError("Temperature too hot")
        self.celsius = celsius

    def _calc_volume(self):
        return (super()._calc_volume() - RefrigeratorShippingContainer.FRIDGE_VOLUME)

    # property for celsius
    @property
    def celsius(self):
        return self._celsius

    # setter for celsius
    @celsius.setter
    def celsius(self, value):
        return self._set_celsius(value)

    def _set_celsius(self, value):
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


class HeatedRefrigeratorShippingContainer(RefrigeratorShippingContainer):
    MIN_CELSIUS = -20


    def _set_celsius(self, value):
        if value < HeatedRefrigeratorShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold")
        super()._set_celsius(value)


