from program.representations import DictionaryMixin


class AddressBook:
    """Class AddressBook. program.contacts"""
    def __init__(self):
        self._employee_address = {
            1: Address('124 Aroyo Rd.', 'Scranton', 'PA', '23420'),
            2: Address('4534 Florida Av.', 'Scranton', 'PA', '23487'),
            3: Address('65 Abore St.', 'Scranton', 'PA', '20046'),
            4: Address('654 Haven Av', 'Scranton', 'PA', '20931'),
            5: Address('8849 Eighth st.', 'Scranton', 'PA', '20903'),
        }
        
    def get_address(self, employee_id):
        address = self._employee_address.get(employee_id)
        if not address:
            raise ValueError('invalad employee id')
        return address


class Address(DictionaryMixin):

    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        address = [self.street]
        if self.street2:
            address.append(self.street2)
        address.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(address)
