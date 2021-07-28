# coverage html
#coverage run <filename to run>

class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: int

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price



    def compute_tax(self, tax_exemption: int = 0) -> float:
        if tax_exemption < 0:
            raise ValueError("Tax exemption should be a positive number")
        tax_percentage = .05
        if self.electric:
            tax_percentage = .02
        return tax_percentage * (self.catalogue_price - tax_exemption)


    def can_lease(self, year_income: int)-> bool:
        if year_income < 0:
            raise ValueError("Can't have zero income")
        return self.catalogue_price <= 0.7 * year_income
        

